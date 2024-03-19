# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Jay Chan
# jayc10@uci.edu
# 54907952

import json
import time
from collections import namedtuple

# Namedtuple to hold the values retrieved from json messages.
DataTuple = namedtuple('DataTuple', ['type', 'message', 'token'])

def extract_json(json_msg:str) -> DataTuple:
  '''
  Call the json.loads function on a json string and convert it to a DataTuple object
  '''
  try:
    json_obj = json.loads(json_msg)
    type = json_obj['response']['type']
    message = json_obj['response']['message']
    token = json_obj['response']['token']
  except json.JSONDecodeError:
    print("Json cannot be decoded.")

  return DataTuple(type, message, token)


def join(username, password):
  join_msg = {"join": {"username": username,"password": password, "token":""}}
  return json.dumps(join_msg)


def post(token, entry):
  timestamp = time.time()
  post_msg = {"token":token, "post": {"entry": entry,"timestamp": timestamp}}
  return json.dumps(post_msg)


def bio(token, entry):
  timestamp = time.time()
  bio_msg = {"token":token, "bio": {"entry": entry,"timestamp": timestamp}}
  return json.dumps(bio_msg)


def directmessage(token, entry):
  timestamp = time.time()
  if entry == "new" or entry == "all":
    direct_msg = {"token": token, "directmessage": entry}
  else:
    direct_msg = {"token": token, "directmessage": {"entry": entry, "recipient":"ohhimark", "timestamp": timestamp}}
  return json.dumps(direct_msg)
