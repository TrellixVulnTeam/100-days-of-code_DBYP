import requests
from datetime import datetime

#TODO: Create your user account

USERNAME = "hjkang"
TOKEN = "XXXXXXXXXX"
GRAPH_ID = "graph1"

pixela_endpoint ="https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#TODO: Create a graph definition + Get the graph!

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai",
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# type(response.text)

#TODO: Post value to the graph

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime(year=2021, month=2, day=3)
today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today?"),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)


#TODO: Put value to the graph
#
# today = datetime(year=2021, month=2, day=3)
#
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# new_pixel_data = {
#     "quantity": "4.5",
# }
#
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


#TODO: Delete value

# today = datetime(year=2021, month=2, day=3)
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)