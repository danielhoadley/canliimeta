import pandas as pd
import requests

df = pd.read_csv('scc-2000.csv')

output_file = open('scc-2000-metadata.json', 'a')

for id in df['caseId/en']:
    url = 'http://api.canlii.org/v1/caseBrowse/en/csc-scc/' + id

    querystring = {"api_key": "6gauat4nerh7ysgvv2t77nu4"}

    headers = {
        'cache-control': "no-cache",
        'postman-token': "09e93bf4-7d92-f13a-a577-e57f84174b05"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    output_file.write(response.text + '\n')