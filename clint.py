import socket

def start_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(('localhost', 12345))

    try:
        # Send some data
        message = "Hello, Server!"
        client_socket.sendall(message.encode())
        
        # Look for the response
        response = client_socket.recv(1024)
        print(f"Received from server: {response.decode()}")
    finally:
        # Clean up the socket
        client_socket.close()

if __name__ == "__main__":
    start_client()

