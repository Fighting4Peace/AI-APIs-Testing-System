import requests
import json

your_task_id = "1695436788631564"

API_KEY = "43cda9a5d8e8e543bde0843fc2e303fcba972ddabd0f7a2b138f24d74ed7f4cb"
url = f"https://api.tigerbot.com/v1/text2image/{your_task_id}"

headers = {
    'Authorization': 'Bearer ' + API_KEY
}

response = requests.get(url, headers=headers)
print(json.dumps(response.json(), ensure_ascii=False, indent=4))
