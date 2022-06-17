import requests, json


'''
Okay, Schemas are good amount of work.
'''

DB_ID = '2b53f71e99054f4c939cf51327858697'
URL = f'https://api.notion.com/v1/databases/{DB_ID}'
query_URL = f'https://api.notion.com/v1/databases/{DB_ID}/query'
TOKEN = 'secret_F6s4xQmPNzSexRdpG0w6vOAcU9al4MObvjTjG1ixQI4'

createUrl = 'https://api.notion.com/v1/pages'
searchUrl = 'https://api.notion.com/v1/search'
payload = {"page_size": 10}
headers ={
    "Accept": "application/json",
    "Notion-Version": "2022-02-22",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"

}


def readDatabase(readUrl: str = URL, payload: dict = payload, headers: dict = headers) -> dict:
    res = requests.get(readUrl, headers=headers)
    print(res.status_code)
    data = res.json()

    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)


def queryDatabase(queryUrl: str = query_URL, payload: dict= payload, headers: dict = headers, write=True):
    res = requests.post(queryUrl, json=payload, headers=headers)
    data = res.json()
    print(write)

    if write == True:
        with open('./db1.json', 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False)
    else:
        print(res.status_code)


def createPage(createUrl: str, headers: dict = headers) -> dict:
    payload = {
        "object": "page","cover": None, "icon": None, "parent": {"type": "database_id", "database_id": "2b53f71e-9905-4f4c-939c-f51327858697"}, "archived": False, 
        "properties": {"Date_Published": {"id": "%3Eji~", "type": "date", "date": {"start": "2022-05-01", "end": None, "time_zone": None}}, "Author": {"id": "uWBD", "type": "rich_text", "rich_text": [{"type": "text", "text": {"content": "Rajiv Malhotra", "link": None}, "annotations": {"bold": False, "italic": False, "strikethrough": False, "underline": False, "code": False, "color": "default"}, "plain_text": "Rajiv Malhotra", "href": None}]}, "Book_Name": {"id": "title", "type": "title", "title": [{"type": "text", "text": {"content": "Invading Sacred", "link": None}, "annotations": {"bold": False, "italic": False, "strikethrough": False, "underline": False, "code": False, "color": "default"}, "plain_text": "Invading Sacred", "href": None}]}}
    }

    res = requests.post(createUrl, json=payload, headers=headers)
    print(res.status_code)
    print(res.json())


def searchPage(headers: dict = headers) -> dict:
    payload: dict = {
        "page_size": 1,
        "query": "Invading the sacred"
    }
    res = requests.post(searchUrl, json=payload, headers=headers)
    print(res.status_code)
    print(res.text)
    


if __name__ == "__main__":
    queryDatabase()
