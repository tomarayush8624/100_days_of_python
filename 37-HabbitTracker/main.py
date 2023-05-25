import requests
import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_TOKENS = "dsfsdfsadfsadfsadf"
PIXELA_USERNAME = "knight47"

pixela_params = {
    "token": PIXELA_TOKENS,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=pixela_params)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"
graph_id = "knight47-coding"
# graph_config = {
#     "id": "knight47-coding",
#     "name": "coding fun",
#     "unit": "minutes",
#     "type": "float",
#     "color": "sora",
#     "timezone": "Asia/Kolkata",
# }
# header = {
#     "X-USER-TOKEN": PIXELA_TOKENS,
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

current_date = f"{datetime.date.today()}".replace("-", "")
post_pixel_endpoint = f"{graph_endpoint}/{graph_id}"
header = {
    "X-USER-TOKEN": PIXELA_TOKENS,
}

# post_config = {
#     "date": current_date,
#     "quantity": "72",
# }
#
# response = requests.post(url=post_pixel_endpoint, headers=header, json=post_config)
# print(response.text)

put_endpoint = f"{post_pixel_endpoint}/{current_date}"

put_config = {
    "quantity": "12"
}

# response = requests.put(url=put_endpoint, headers=header, json=put_config)
response = requests.delete(url=put_endpoint, headers=header)
print(response.text)