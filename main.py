from fastapi import FastAPI, Form
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from fastapi import Request, Response
from fastapi.responses import RedirectResponse
from square.client import Client
import configparser
import json
import google.generativeai as palm

app = FastAPI()
templates = Jinja2Templates(directory="templates")
config = configparser.ConfigParser()
config.read("config.ini")
CONFIG_TYPE = config.get("DEFAULT", "environment").upper()
APPLICATION_ID = config.get(CONFIG_TYPE, "square_application_id")
LOCATION_ID = config.get(CONFIG_TYPE, "square_location_id")
ACCESS_TOKEN = config.get(CONFIG_TYPE, "square_access_token")

client = Client(
    access_token=ACCESS_TOKEN,
    environment=config.get("DEFAULT", "environment"),
)

palm.configure(api_key="AIzaSyDxoIWeGEGLFQKr0t01OMRZaIxOyr1I91o")

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

llm_result_db = ["N/A"]

@app.get("/")
async def read_root(request: Request):
    result = client.merchants.list_merchants()
    return templates.TemplateResponse("index.html", {"request":request, "business_name":result.body["merchant"][0]["business_name"], "output_text":llm_result_db[-1]})

@app.post("/submit")
async def submit_data(request: Request, data: str=Form(...)) :
    catalog = client.catalog.list_catalog()
    item_var_list = []
    for item in catalog.body["objects"]:
        for item_var in item["item_data"]["variations"]:
            item_var_list.append(item_var["id"])
    prompt = ""
    prompt += json.dumps(jsonable_encoder(catalog.body["objects"]))
    for object in item_var_list:
        count = client.inventory.retrieve_inventory_count(
            catalog_object_id = object
        )
        count = jsonable_encoder(count)
        prompt += json.dumps(count)
        prompt += "\n\n"
    inventory_changes = client.inventory.batch_retrieve_inventory_changes(
        body = {}
    )
    prompt += json.dumps(jsonable_encoder(inventory_changes))
    prompt += "\n\n\n"
    prompt += "The cost is in cents USD. The person interacting with the llm is the seller, not the buyer. Always display price or cost in the answer in dollars format USD. All questions will refer to the given information. All answers should pertain to the given information as well. Answer in full sentences only. When asked questions about inventory items, make sure to reference the given information directly."
    prompt += "\n\n\n"
    prompt += data
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0.3,
        max_output_tokens=1000,
    )
    llm_result_db.append(completion.result)
    return RedirectResponse("/", status_code=302)
