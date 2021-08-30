import os
import requests, json


TOKEN = 'secret_zlggP130179TBBXSRekktfcohobq6q5ygklg8iKNzFw'

DATABASEUID = '9a7fe539db2f499795ead0686f0eda42'

HEADERS = {
    'Authorization' : 'Bearer' + TOKEN,
    'Notion-Version': '2021-05-13'
}


def readDataabse(DATABASEUID, HEADERS):
    READURL = f'https://api.notion.com/v1/databases/{DATABASEUID}'
    RESP = requests.request("GET", READURL, headers=HEADERS)
    print(RESP.text)


def createPage():
    pass


def updatePage():
    pass



readDataabse(DATABASEUID, HEADERS)
