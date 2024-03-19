# Test code for part 1

import ds_client

def main():
    server = "168.235.86.101"
    port = 3021
    username = "saitama"
    password = "opm"
    message = "message!"

    response = ds_client.send(server, port, username, password, message)
    print(response)
    
    # test
    assert response == True


if __name__ == '__main__':
    main()
