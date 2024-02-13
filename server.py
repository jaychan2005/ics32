

import socket

#Our business logic!
def capitalizer(text):
    return text.upper()

def main():
    
    port = 6060
#Creating a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind
    server_socket.bind((socket.gethostname(), port))
#listen for clients (up to 5)
    server_socket.listen(5)

    print(f"Server is listening on {socket.gethostname()}: {port}")
    
    while True:
        client_socket, address = server_socket.accept() #accepting the client
        print(f"Connected to the client, {address}")
        
        #receive
        client_data = client_socket.recv(2048).decode('utf-8').strip()
        print (f"Received from the client: {client_data}")
        
        #call capitalize
        capitalized_text = capitalizer(client_data)
        
        #send
        
        client_socket.send(capitalized_text.encode('utf-8'))
        client_socket.close()




if __name__ == "__main__":
    main()