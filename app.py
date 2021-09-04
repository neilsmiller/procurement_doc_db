from pymongo import MongoClient, TEXT
import fitz  # this is PyMuPDF

client = MongoClient()
client

db = client.procurement

attachment = db.attachment

attachment

attachment1 = {"author": "Neil Miller"}

result = attachment.insert_one(attachment1)
print("The insertedid is {}".format(result.inserted_id))

with fitz.open(
    "C:\\Users\\19739\\Downloads\\1331L519R13OS0005_BAS_Final_RFP-1.pdf"
) as doc:
    rfp_text = ""
    for page in doc.pages(start=0, stop=15, step=1):
        rfp_text += page.getText()

Draft_RFP = {
    "tile": "Draft RFP",
    "date": "July 12, 2019",
    "solid": "1331L520C13OS0005",
    "text": rfp_text,
}

with fitz.open(
    "C:\\Users\\19739\\Downloads\\BAS_Draft_Performance_Work_Statement.pdf"
) as doc:
    pws_text = ""
    for page in doc.pages(start=0, stop=15, step=1):
        pws_text += page.getText()


Draft_PWS = {
    "tile": "Draft PWS",
    "solid": "1331L520C13OS0005",
    "date": "July 12, 2019",
    "text": pws_text,
}

result = attachment.insert_many([Draft_RFP, Draft_PWS])

# attachment.create_index([('text', TEXT)], default_language = 'english')
attachment.create_index(name="fulltext", keys=[("text", TEXT)])


# def search_for_product(search_text):
#     db.attachment.find({"text": search_text}).limit(10)


# r = search_for_product("/.*warehouse.*/")
# print(r)
