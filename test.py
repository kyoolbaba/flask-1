import requests

BASE_URL="http://127.0.0.1:5000"

response_1=requests.post(BASE_URL+"/hello_world")
response_2=requests.get(BASE_URL+"/greet/Milan")
response_3=requests.get(BASE_URL+"/biodata/Milan/24/bangalore")
print(response_1.json()   )
print(response_2.json()   )
print(response_3.json()   )