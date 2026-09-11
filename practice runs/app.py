import chromadb
chroma_client = chromadb.Client()

collection_name = "test_collection"
collection = chroma_client.get_or_create_collection(collection_name) # checks if there is already a collection

documents = [
    {"id": "doc1", "text": "Hello, world!"},
    {"id": "doc2", "text": "How are you today?"},
    {"id": "doc3", "text": "Goodbye, see you later!"},
]

for doc in documents:
    collection.upsert(ids=doc["id"], documents=doc["text"])

# add inserts new items. will throw exception of an id already exists
# upsert updates if id already exists, if not creates new one

#define a query text
query_text = "Hello, World!"

results = collection.query(
    query_texts=[query_text],
    n_results = 3,
)

print(results)
# the closer the distances are to 0, the more they match semantically