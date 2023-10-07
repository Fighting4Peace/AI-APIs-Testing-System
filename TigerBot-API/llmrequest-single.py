import requests
import json

API_KEY="43cda9a5d8e8e543bde0843fc2e303fcba972ddabd0f7a2b138f24d74ed7f4cb"
url = "https://api.tigerbot.com/v1/chat/completions"

headers = {
    'Authorization': 'Bearer ' + API_KEY
}

payload = {
    "model": "tigerbot-70b-chat",
    "query": "请用英文词组。，linger about 造句10个英文句子"
}

response = requests.post(url, headers=headers, json=payload)
print(json.dumps(response.json(), ensure_ascii=False, indent=4))
