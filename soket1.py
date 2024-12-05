import socket

def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind(('localhost', 12345))

    # Listen for incoming connections
    server_socket.listen(1)
    print("Server listening on port 12345...")

    while True:
        # Wait for a connection
        connection, client_address = server_socket.accept()
        try:
            print(f"Connection from {client_address}")
            # Receive data from the client
            data = connection.recv(1024)
            print(f"Received: {data.decode()}")
            # Send data back to the client
            connection.sendall(data)  # Echo back the received data
        finally:
            # Clean up the connection
            connection.close()

if __name__ == "__main__":
    start_server()

