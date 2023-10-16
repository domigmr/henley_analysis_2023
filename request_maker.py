import requests
import json

url = "https://www.hrr.co.uk/wp-json/hrr/v1/results"


full_results = []

for page_number in range(1,232):

    querystring = {"result-page": str(page_number)}

    payload = ""
    headers = {"cookie": "AWSALB=m1T6EISLwEKsBScTqQ8kaQ0mCULNZ13f3B4t4ke81CSKTETHm6O4EWjgytojtr9r4zMk595XzvrYbpCY5mIcD2lRlMUn4yprCfpPndsPNpVpYFAMItmwztmZRncM; AWSALBCORS=m1T6EISLwEKsBScTqQ8kaQ0mCULNZ13f3B4t4ke81CSKTETHm6O4EWjgytojtr9r4zMk595XzvrYbpCY5mIcD2lRlMUn4yprCfpPndsPNpVpYFAMItmwztmZRncM"}

    response = json.loads((requests.request("GET", url, data=payload, headers=headers, params=querystring)).text)

    results = response['results']

    for result in results:
        result['Boat Class'] = result['trophy']['class']['name']

        result['Barrier LL'] = result['barrier']['loserLeading']
        result['Barrier ER'] = result['barrier']['equalsRecord']
        result['Barrier NR'] = result['barrier']['newRecord']
        result['barrier'] = result['barrier']['split']

        result['Fawley LL'] = result['fawley']['loserLeading']
        result['Fawley ER'] = result['fawley']['equalsRecord']
        result['Fawley NR'] = result['fawley']['newRecord']
        result['fawley'] = result['fawley']['split']


        result['Finish ER'] = result['finish']['equalsRecord']
        result['Finish NR'] = result['finish']['newRecord']
        result['finish'] = result['finish']['split']

        result['winner'] = result['winner']['shortName']
        result['loser'] = result['loser']['shortName']

        result['trophy'] = result['trophy']['shortName']

        full_results.append(result)

json_filepath = '/home/domigmr/PersonalProjects/Misc/Henley/henley1.json'

with open(json_filepath, "w") as final:
    json.dump(full_results, final)

