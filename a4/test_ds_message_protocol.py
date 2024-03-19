import ds_client
import json

def main():
    server = "168.235.86.101"
    port = 3021
    username = "saitama"
    password = "opm"
    message = "message!"

    response = ds_client.send(server, port, username, password, message)
    print(response)
    
    # test
    response = json.loads(response)
    assert response == {"response": {"type": "ok", "message": "Direct message sent"}}


if __name__ == '__main__':
    main()
