import requests
import json
import tools

array = []
arrayAux = []
searches = ["75889", "75890", "75891", "75892", "75893", "75894", "75895", "75896", "75897", "75898", "75899", "75900", "75901", "75902", "75903", "75904"]

response = requests.get(
    "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=f9p95s8eo8mjmt4oe80fc7u9r4&quantity=1000&from=0&level_id=GPS&order_way=ASC&order_id=100&filter_id=39263")
values = response.json()
tools.getNumId(array, values)

for b in searches:
    response = requests.get(
        "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=f9p95s8eo8mjmt4oe80fc7u9r4&order_id=100&order_way=ASC&level_id=GPS&from=0&quantity=1000&node_id="+b)
    values = response.json()
    tools.getNumId(array, values)

array.sort()

for e in array:
    arrayAux.append(tools.getData(e))

with open('claro.json', 'w') as outfile:
    for e in arrayAux:
        json.dump(e, outfile)
        outfile.write("\n")








