
import socket

#This client receives a string from the user, and sends it to the server.
#This server capitalizes the string and returns it back to the client

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #we are connecting to a host IP and port
    client_socket.connect((socket.gethostname(), 6060))

    #getting the input from the user
    message = input("Enter a string to be capitalized OR type (quit) to quit: ")
    print(f"message from the server: {message}")
    
    #send the message to the server
    client_socket.send(message.encode('utf-8'))
    
    #receive the message from the server
    capitalized_message = client_socket.recv(2048).decode('utf-8')
    
    
    print(capitalized_message)
    
    #close the socket
    client_socket.close()


if __name__ == "__main__":
    main()