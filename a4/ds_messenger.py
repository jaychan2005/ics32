import socket
import ds_protocol
import json

class DirectMessage:
  def __init__(self):
    self.recipient = None
    self.message = None
    self.timestamp = None


class DirectMessenger:
  def __init__(self, dsuserver=None, username=None, password=None):
    self.dsuserver = dsuserver
    self.username = username
    self.password = password
    self.token = None
		
  def send(self, message:str, recipient:str) -> bool:
    # must return true if message successfully sent, false if send failed.
    try:
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((self.dsuserver, 3021))
        send = client.makefile('w')
        recv = client.makefile('r')
        join_msg = ds_protocol.join(self.username, self.password)
        send.write(join_msg + '\r\n')
        send.flush()
        resp = recv.readline()
        resp = ds_protocol.extract_json(resp) # extract
        self.token = resp[2]
        
        if resp[0] == 'ok':
          msg = ds_protocol.directmessage(self.token, message, recipient)
          client.sendall(msg.encode('utf-8'))
      return True
    except Exception as error:
      print(f"An error occurred: {error}")
      return False

		
  def retrieve_new(self) -> list:
    # must return a list of DirectMessage objects containing all new messages
     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((self.dsuserver, 3021))
        send = client.makefile('w')
        recv = client.makefile('r')
        join_msg = ds_protocol.join(self.username, self.password)
        send.write(join_msg + '\r\n')
        send.flush()
        resp = recv.readline()
        resp = ds_protocol.extract_json(resp) # extract
        self.token = resp[2]
        
        if resp[0] == 'ok':
          msg = ds_protocol.directmessage(self.token, "new")
          client.sendall(msg.encode('utf-8'))
          srv_msg = client.recv(4096)
          new = json.loads(srv_msg.decode('utf-8'))
          return new["response"]["messages"]
 
 
  def retrieve_all(self) -> list:
    # must return a list of DirectMessage objects containing all messages
     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((self.dsuserver, 3021))
        send = client.makefile('w')
        recv = client.makefile('r')
        join_msg = ds_protocol.join(self.username, self.password)
        send.write(join_msg + '\r\n')
        send.flush()
        resp = recv.readline()
        resp = ds_protocol.extract_json(resp) # extract
        self.token = resp[2]
        
        if resp[0] == 'ok':
          msg = ds_protocol.directmessage(self.token, "all")
          client.sendall(msg.encode('utf-8'))
          srv_msg = client.recv(4096)
          all = json.loads(srv_msg.decode('utf-8'))
          return all["response"]["messages"]