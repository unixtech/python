import os
import requests, json

with open('/root/sec/api_key_AutoInt') as sec:
    TOKEN = sec.readline()

DATABASEUID = '9a7fe539db2f499795ead0686f0eda42'

HEADERS = {
    'Authorization' : 'Bearer' + TOKEN,
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
