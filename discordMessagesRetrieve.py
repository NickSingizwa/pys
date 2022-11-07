import requests
import json

def retrieve_messages(channelId):
    headers = {
        'authorization': ''    # Enter your token here
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelId}/messages?limit=10',headers=headers)
    jsonn = json.loads(r.text)

    for value in jsonn:
        print(value['content'],'\n')

retrieve_messages('')    # Enter your channel ID here