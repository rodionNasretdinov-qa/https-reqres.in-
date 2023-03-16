import requests

# URL "https://reqres.in"

# валидный запрос 
response = requests.get("https://reqres.in/api/users/2") 
print(response) 

if response.status_code == 200:
    print ('ok')
else :
    print ('not ok')

# не валидный запрос
response = requests.get("https://reqres.in/api/users/2")
print(response) 

if response.status_code == 201:
    print ('ok')
else :
    print ('not ok')
  
response = requests.get("https://reqres.in/api/users/2") 
print(response.text) 
