##Inspiration
It's often easy to get lost in the complexity of the entire supply and demand process. Even though multiple UI's have been developed to help Square sellers navigate the process associated with tracking inventory count for corresponding catalog items, there isn't an easy way to quickly acquire this information. Oftentimes, the Square seller will have to manually check inventory counts and make sure there is enough of a product to successfully continue meeting demand.

##What it does
With BhavanaAI, Square sellers will be able to actually communicate with the AI that has full knowledge about the catalog and inventory associated with that certain Square seller. This will enable quick information retrieval, and lead to advanced analysis of the supply and demand process. More specifically, sellers can approximate how future demand will effect their current inventory amounts, and will not be understocked or overstocked. Square sellers will be able to monitor their real time supply and demand while considering recent orders and when items were restocked.

##How we built it
I built BhavanaAI using Google's PaLM API and 3 Square API's: the Orders API, the Inventory API, and the Catalog API. Additionally, I used python and FastAPI to take care of web dev, as well as basic HTML and CSS for page format and styling.

##Challenges we ran into
The main challenge was tying in all the Square API's and feeding the resulting information as input to the Google PaLM API. This was crucial to the construction of BhavanaAI because the AI needs to be aware of several aspects of information, such as recent orders, current inventory counts, restocking information, and all associated catalog items and item variations.

##Accomplishments that we're proud of
Having an AI that is able to link different aspects of Catalog, Order, and Inventory information together is an accomplishment for me. Additionally, adding a more specific prompt to the AI enabled more accurate information being displayed as output.

##What we learned
I learned quite a bit about the process of bringing an applied AI product to life after going through an entire mini-cycle of the software development process. It was very important to realize that having a pre-trained LLM AI is only part of the process. Feeding the additional information as an input prompt or fine-tuning the model is much better for the accuracy and efficiency of the results.

What's next for BhavanaAI
Next comes the implementation of additional generative AI embedded into the BhavanaAI interface that would help create graphs and charts enlightening Square sellers about which products did well in the supply and demand chain, and which products can be changed in terms of inventory count or design to generate more orders for those products, or switch to a different product entirely and change some business strategy for more revenue.
