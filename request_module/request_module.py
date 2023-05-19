import json
import requests

# ! Get req

res = requests.get(
    "https://vcdas-natours-app.onrender.com/api/v1/tours",
    timeout=10,
)
data = res.json()["data"]["doc"]
file = open(
    r"C:\Users\Vaskar\Desktop\Code_Files\Python\request_module\tours.json",
    "w+",
    encoding="utf-8",
)
json.dump(data, file, indent=2)
file.close()

# @ Separate file for each tour
for index, tour in enumerate(data):
    file = open(
        rf"C:\Users\Vaskar\Desktop\Code_Files\Python\request_module\{tour['name']}.json",
        "w+",
        encoding="utf-8",
    )
    json.dump(tour, file, indent=2)


# file.write(str(data["data"]["doc"]))
# print(len(data["data"]["doc"]))
# print(data["data"]["doc"][0]["name"])

# ! Post req
# res = requests.post(
#     "https://vcdas-natours-app.onrender.com/api/v1/users/login",
#     timeout=10,
#     data={"email": "admin@natours.io", "password": "test1234"},
# )
# # print(res.json())
# data = res.json()

# # Save response to a file
# fileUser = open(
#     r"C:\Users\Vaskar\Desktop\Code_Files\Python\request_module\login.json",
#     "w+",
#     encoding="utf-8",
# )
# json.dump(data, fileUser, indent=2)
