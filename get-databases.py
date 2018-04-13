import requests

url = "http://api.canlii.org/v1/caseBrowse/en/"

querystring = {"api_key":"6gauat4nerh7ysgvv2t77nu4"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "f884f222-9afa-3609-d881-5c4b65ca1230"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)