import requests
import json

BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"


def get_list():
    r = requests.get(BASE_URL+ENDPOINT) #  Get list
    print(r.status_code)
    data = r.json()
    for obj in data:
        if obj['id'] ==1:
            r2 = requests.get(BASE_URL+ENDPOINT+str(obj["id"])) # get one data
            print(r2.json())

    return r.json()



def create_update():
    new_data ={
        "user" :1,
        "content" : "Some new Update"
    }
    r = requests.delete(BASE_URL+ENDPOINT, data=new_data)
    print(r.status_code)

    return r.text

print(create_update())
# print(get_list())