import requests

url = "http://api.canlii.org/v1/caseBrowse/en/csc-scc/"

querystring = {"offset":"0","resultCount":"2000","decisionAfter":"2000-01-01","api_key":"6gauat4nerh7ysgvv2t77nu4"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "343930e3-21e8-0f23-1c5e-e88ec8d1afc8"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

output_file = open('scc-2000.json', 'w')
output_file.write(response.text)

