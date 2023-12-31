import requests
import config

import requests
import json


def create_notion_page(title):
    url = "https://api.notion.com/v1/pages/"

    payload = json.dumps(
        {
            "parent": {"database_id": config.DATABASE_ID},
            "properties": {
                "Task name": {
                    "title": [{"text": {"content": title}}]
                }
            },
        }
    )
    headers = {
        "Content-Type": "application/json",
        "Notion-Version": "2022-02-22",
        "Authorization": f"Bearer {config.NOTION_API_KEY}"
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    response.raise_for_status()
    return response.json()


# Usage example
# database_id =
# title = "New Page Title"
# properties = {
#     "Title": {"title": [{"type": "text", "text": {"content": title}}]}
# }

# response = create_notion_page("ahhahah")
# print(response)
# print(response)
