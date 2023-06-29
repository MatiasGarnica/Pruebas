import requests

url = "https://webhook.site/c283211e-41f6-4ebb-933a-c8485c592e11"

payload = {"plato": "pasta", "cantidad": 2}
query_params = {"nombre": "Paco"}
response = requests.post(url, data=payload, params = query_params)



