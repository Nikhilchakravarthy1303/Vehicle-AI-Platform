import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="vehicle_incidents")

def add_incident_to_chroma(incident_id, description, incident):
    try:
        collection.add(
            documents=[description],
            ids=[str(incident_id)],
            metadatas=[incident]
        )
    except Exception as e:
        print(f"Error adding incident to ChromaDB: {e}")

