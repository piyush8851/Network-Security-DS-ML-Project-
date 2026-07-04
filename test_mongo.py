from pymongo import MongoClient
uri = "mongodb+srv://piyushchaudhary6397:Piyush%40001@cluster0.mbmmpks.mongodb.net/?appName=Cluster0"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)