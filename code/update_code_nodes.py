import json
import os
import requests

api_key = os.environ["TAKTILE_API_KEY"]
api_url = "https://api.taktile.com/api/v1/code_nodes"

with open("code-node-map.json") as f:
    mapping = json.load(f)

for filename, node_id in mapping.items():
    with open(filename, "r") as f:
        code = f.read()

    response = requests.put(
        f"{api_url}/{node_id}",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={"code": code}
    )

    if response.status_code == 200:
        print(f" Updated {filename} to node {node_id}")
    else:
        print(f"  Failed to update {filename}: {response.text}")
