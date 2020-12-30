import requests
import json
import os




AUTH_ENDPOINT = "http://127.0.0.1:8000/auth/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

headers ={
    "Content-Type": "application/json",
    # "Authorization" : "JWT " + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMywidXNlcm5hbWUiOiJzYW5kaHlhMTMiLCJleHAiOjE2MDkyNjAwODcsImVtYWlsIjoic2FuZGh5YTEzQGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNjA5MjU5Nzg3fQ.4ubQ8256jHMxBvZQBQZQNQs9g6ox0PvGeAil_-inXhU"

}

data ={
    "username" : "sandhya",
    "password" : "sandhya@365",
}

r = requests.post(AUTH_ENDPOINT,data=json.dumps(data),headers=headers)

token = r.json()["token"]
print(token)

BASE_ENPOINT =  "http://127.0.0.1:8000/status/"
ENDPOINT = BASE_ENPOINT +"28/"


headers2 ={
    # "Content-Type": "application/json",
    "Authorization" : "JWT " + token,

}
data2 ={
    "content" : "this is new data"
}

# r2 = requests.put(ENDPOINT,data=data2,headers=headers2)
# r2 = requests.post(BASE_ENPOINT,data=data2,headers=headers2)


# print(r2.text)

r3 = requests.get(ENDPOINT,headers=headers2)
print(r3.text)



# ENDPOINT = "http://127.0.0.1:8000/status/"
# AUTH_ENDPOINT = "http://127.0.0.1:8000/auth/register/"
# REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

# headers ={
#     "Content-Type": "application/json",
#     "Authorization" : "JWT " + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMywidXNlcm5hbWUiOiJzYW5kaHlhMTMiLCJleHAiOjE2MDkyNjAwODcsImVtYWlsIjoic2FuZGh5YTEzQGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNjA5MjU5Nzg3fQ.4ubQ8256jHMxBvZQBQZQNQs9g6ox0PvGeAil_-inXhU"

# }

# data ={
#     "username" : "sandhya13",
#     "email" : "sandhya13@gmail.com",
#     "password" : "sandhya@365",
#     "password2" : "sandhya@365"
# }

# r = requests.post(AUTH_ENDPOINT,data=json.dumps(data),headers=headers)


# print(r.text)


# ENDPOINT = "http://127.0.0.1:8000/status/"
# AUTH_ENDPOINT = "http://127.0.0.1:8000/auth/"
# REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

# headers ={
#     "Content-Type": "application/json"
# }
# # headers ={
# #     "Content-Type": "application/json",
# #     "Authorization" : "JWT " + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InNhbmRoeWEiLCJleHAiOjE2MDkxNjI0OTgsImVtYWlsIjoic2FuZGh5YUBnbWFpbC5jb20iLCJvcmlnX2lhdCI6MTYwOTE2MjE5OH0.KHQBMotTRYysPJfVdzB7UWFEuCYw9GwqeFyncl-vH1s"
# # }
# data ={
#     "username" : "sandhya@gmail.com",
#     "password" : "sandhya@365"
# }

# r = requests.post(AUTH_ENDPOINT,data=json.dumps(data),headers=headers)

# token = r.json()

# print(token)


# ENDPOINT = "http://127.0.0.1:8000/status/"
# AUTH_ENDPOINT = "http://127.0.0.1:8000/auth/jwt/"
# REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"


# image_path = os.path.join(os.getcwd(),"image.jpg")

# headers ={
#     "Content-Type": "application/json"
# }

# data ={
#     "username" : "sandhya",
#     "password" : "sandhya@365"
# }

# r = requests.post(AUTH_ENDPOINT,data=json.dumps(data),headers=headers)

# token = r.json()["token"]

# print(token)

# refresh_data ={
#     "token" : token,
#     "username" : "sandhya",
#     "password" : "sandhya@365"
# }


# new_response = requests.post(REFRESH_ENDPOINT,data=json.dumps(refresh_data),headers=headers)


# new_token = new_response.json()

# print(new_token)



# r = requests.post(AUTH_ENDPOINT,data=data)

# print(r.json()["token"])







# get_data_endpoint = ENDPOINT + str(6)
# post_data = json.dumps({"content":"content new update"})


# r = requests.get(get_data_endpoint)
# print(r.text)


# r2 = requests.get(ENDPOINT)
# print(r2.text)

# post_headers = {
#     "Content-Type" : "application/json",
#     "Authorization" : "JWT " + token,
# }
# post_response = requests.post(ENDPOINT, data= post_data, headers = post_headers)

# print(post_response.text)

# put_response = requests.put(ENDPOINT+str(18)+"/", data= post_data, headers = post_headers)

# print(put_response.text)

# def do_img(method="get",data={}, is_json=True,img_path=None):
#     headers = {}
#     if is_json:
#         headers["content-type"] = "application/json"
#         data = json.dumps(data)
#     if img_path is not None:
#         with open(image_path ,"rb") as image:
#             file_data ={
#                 "image" : image
#             }
#             r = requests.request(method,ENDPOINT,data=data,files=file_data,headers=headers)
#     else:
#         r = requests.request(method,ENDPOINT,data=data,headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r

# do_img(method="post", data ={"user":1,"content":""},is_json=False,img_path=image_path)


# do_img()


# Passing ID with URL
# def do(method="get",data={},id=3, is_json=True):
#     if is_json:
#         data = json.dumps(data)
#     r = requests.request(method,ENDPOINT+"?id="+str(id),data=data)
#     print(r.text)
#     return r


# Passing ID with body(data)
# def do(method="get",data={}, is_json=True):
#     headers = {}
#     headers["content-type"] = "application/json"
#     if is_json:
#         data = json.dumps(data)
#     r = requests.request(method,ENDPOINT,data=data,headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r

# do(data={"id":113})

# do(method="delete",data={"id":5,})
# do(method="put",data={"id":5,"user":1,"content":"cooollll content"})
# do(method="post",data={"user":1,"content":"cooollll content"})



