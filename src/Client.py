import socket
import json

def get_primes_from_server(start, end, host, port):
    """
    Function to get primes from the server.

    :param start: The starting number of the interval (inclusive)
    :param end: The ending number of the interval (inclusive)
    :param host: The host address of the server
    :param port: The port number of the server
    :return: A list of prime numbers in the interval received from the server
    """
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect with server
    client_socket.connect((host, port))

    # Convert the start and end values into a JSON string and send them as a tuple to the server
    client_socket.send(json.dumps((start, end)).encode('utf-8'))

    # Receive the primes from the server in parts
    data = b"" # Initializes an empty byte string to store the received data
    while True:
        part= client_socket.recv(1024) # Receives part of the list of primes from the server
        if not part:
            break
        data += part

    # Convert the received data from JSON string back into a list of primes
    primes = json.loads(data)

    client_socket.close()
    return primes