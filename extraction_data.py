from mastodon import Mastodon
import json
from datetime import datetime
from hdfs import InsecureClient
import os


# importing the package 
#from snakebite.client import Client 

access_token_env = os.environ.get("access_token")
access = Mastodon(api_base_url="https://mastodon.social",access_token=access_token_env)

#res = access.timeline_home(limit=None)
results = access.timeline_public(limit=None)

def datetime_encoder(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} is not JSON serializable")

json_str = json.dumps(results, default=datetime_encoder)
# json_obj = json.loads(json_str)
# print(type(json_obj))
# with open("data/sample.json", "w") as outfile:
#     outfile.write(json_str)

# Encode the JSON string as bytes
json_bytes = json_str.encode('utf-8')

with open("data/sample.json", "w") as outfile:
    outfile.write(json_str)


#  define location
hdfs_destination_path = '/data/sample.json'

# Create an HDFS client
hdfs_client = InsecureClient('http://localhost:9870/', user='jane')

with hdfs_client.write(hdfs_destination_path, overwrite=True) as writer:
    writer.write(json_bytes)

print(f"Data written to HDFS at: {hdfs_destination_path}")
