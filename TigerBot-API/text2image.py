import requests
import json

API_KEY = "43cda9a5d8e8e543bde0843fc2e303fcba972ddabd0f7a2b138f24d74ed7f4cb"
url = "https://api.tigerbot.com/v1/text2image"

headers = {
    'Authorization': 'Bearer ' + API_KEY
}

payload = {
    "text": "参天大树",
    "modifiers": ["油画", "哑光"],
    "width": 768,
    "height": 768,
    "n_iter": 1,
    "seed": 0
}

response = requests.post(url, headers=headers, json=payload)
print(json.dumps(response.json(), ensure_ascii=False, indent=4))
