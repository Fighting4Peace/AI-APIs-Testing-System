import requests
import json

# 根据任务id查询任务状态
your_task_id = "4298"

API_KEY = "43cda9a5d8e8e543bde0843fc2e303fcba972ddabd0f7a2b138f24d74ed7f4cb"
url = f"https://api.tigerbot.com/v1/summarization/{your_task_id}"

headers = {
    'Authorization': 'Bearer ' + API_KEY
}

response = requests.get(url, headers=headers)
print(json.dumps(response.json(), ensure_ascii=False, indent=4))
