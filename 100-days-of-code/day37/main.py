# Day 37
# HTTP Requests

import requests
from datetime import datetime

USERNAME = "leofranco"
TOKEN = "k8sd7g612hg79"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url="https://pixe.la/v1/users", json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding graph",
    "unit": "Day",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1",
}

new_pixel_data = {
    "quantity": "2",
}



# pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)


# POST
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# PUT

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# response = requests.put(url=update_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# DELETE

# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# 
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
