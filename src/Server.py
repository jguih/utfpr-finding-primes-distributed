import socket
import json
from FindPrimes import find_primes_in_interval  

def handle_client(client_socket):
    """
    Function to handle communication with the connected client.

    :param client_socket: Socket object representing the connection with the client, 
    used to send and receive data between the server and the client
    """
    # Receive data from the client and convert from bytes to string
    data = client_socket.recv(1024).decode('utf-8')
    start, end = json.loads(data)  # Converts the received JSON string into start and end values
    print(f"Calculating primes in range ({start}, {end})")

    # Find the primes for the given interval, passing the start and end values as a tuple
    primes = find_primes_in_interval((start, end)) 

    # Send the list of primes back to the client in parts
    response = json.dumps(primes) # Converts the primes list into a JSON string
    total_sent = 0
    while total_sent < len(response):
        # Send the remaining primes back to the client and convert string to bytes
        sent = client_socket.send(response[total_sent:].encode('utf-8'))
        total_sent += sent

    # Close connection socket with the client
    client_socket.close()

def start_server(host='127.0.0.1', port=12345):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the host and port
    server_socket.bind((host, port))
    # Listening for incoming client connections on the socket, with a maximum number of queued unaccepted connections
    server_socket.listen(5)
    print(f"Server started at {host}:{port}")
    
    while True:
        # Accept an incoming connection from a client
        client_socket, client_address = server_socket.accept() # Returns a new socket object to send/receive data and the address of the client
        print(f"Client connected from {client_address}")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()