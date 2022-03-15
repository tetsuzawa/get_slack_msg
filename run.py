import os
import sys
from typing import ChainMap
import requests
import json

from dotenv import load_dotenv
load_dotenv()

url = "https://slack.com/api/conversations.history" 
TOKEN = os.environ.get("SLACK_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

header={
    "Authorization": "Bearer {}".format(TOKEN)
}


cursor = ""
msgs = []

while True:
    payload  = {
        "channel" : CHANNEL_ID,
        "cursor" : cursor
        }

    res = requests.get(url, headers=header, params=payload)
    dic = res.json()

    # edited = raw.replace('"', '\\"')
    # edited = edited.replace('\'', '"')
    # edited = edited.replace('True', 'true')
    # edited = edited.replace('False', 'false')
    # edited = edited.replace('None', '""')
    # edited = edited.replace('\\xa', '')

    # dic = json.loads(edited)
    for msg in dic["messages"]:
        msgs.append(msg["text"])

    print(len(msgs), file=sys.stderr)
    print(msgs[0], file=sys.stderr)
    if not dic["has_more"]:
        break
    cursor = dic["response_metadata"]["next_cursor"]

print("\n".join(msgs))

