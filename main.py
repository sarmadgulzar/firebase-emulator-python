from dotenv import load_dotenv
from google.cloud.firestore import Client

load_dotenv()
db = Client()

_, doc_ref = db.collection("users").add({"first_name": "John", "last_name": "Doe"})
