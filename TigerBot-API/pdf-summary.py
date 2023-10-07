import requests
import json

API_KEY = "43cda9a5d8e8e543bde0843fc2e303fcba972ddabd0f7a2b138f24d74ed7f4cb"
url = "https://api.tigerbot.com/v1/summarization"

headers = {
    'Authorization': 'Bearer ' + API_KEY
}

payload = {}

# your_pdf_path = '/Users/gavincoder/Desktop/Yurun RE-GOA Bioinfomatics 2022.pdf'
your_pdf_path = '/Users/gavincoder/Desktop/文字文稿1.pdf'

files = {'file': open(your_pdf_path, 'rb')}

response = requests.post(url, headers=headers, data=payload, files=files)

print(json.dumps(response.json(), ensure_ascii=False, indent=4))
