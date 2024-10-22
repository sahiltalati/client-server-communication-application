# Import socket module
from socket import * 
import sys  # In order to terminate the program
import datetime
from _thread import *
import threading  # In order to allow simultaneous client communications

# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)

class Client:
    def __init__(self, number, date):
        if number < 10:
            self.name = f"Client0{number}"
        else:
            self.name = f"Client{number}"

        self.timeAccept = date
        self.timeFinish = None

    def __str__(self):
        return f"Name: {self.name}, Time Accepted: {self.timeAccept}, Time Finished: {self.timeFinish}"

    def setTimeFinish(self, timeFinish):
        self.timeFinish = timeFinish


# Create the date
def create_date():
    time = datetime.datetime.now()
    return time


# Print cache
def print_cache(list_of_clients):
    cache_content = ""
    for client in list_of_clients:
        cache_content += f"""
Client Name: {client.name}
Accept date: {client.timeAccept}
Finish date: {client.timeFinish}
"""
    return cache_content


# Threaded client communication
def threaded(connection_socket, client_obj):
    print(f'accepting from {client_obj.name}')
    connection_socket.send(client_obj.name.encode())

    with connection_socket:
        sentence = ""

        while sentence != "exit":
            sentence = connection_socket.recv(1024).decode()

            # Prints cache
            if sentence == "status":
                response = print_cache(list_of_clients)
                connection_socket.send(response.encode())

            # Closes the connection
            elif sentence == "exit":
                connection_socket.close()
                client_obj.setTimeFinish(create_date())
                with active_clients_lock:
                    active_clients.remove(client_obj)
                return

            # Continue operation
            else:
                response = f"{sentence} ACK"
                connection_socket.send(response.encode())


# Server setup
server_socket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
server_port = 1234

# Bind the socket to server address and server port
server_socket.bind(("", server_port))
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Listen for up to 3 connections at a time
server_socket.listen(3)

print('The server is ready to receive')

count = 1
list_of_clients = []
active_clients = []  # Track active clients
max_clients = 3
active_clients_lock = threading.Lock()  # Lock to manage active_clients

all_threads = []

while True:
    connection_socket, addr = server_socket.accept()

    # Acquire the lock to ensure thread safety
    with active_clients_lock:
        # Check if there are available slots
        if len(active_clients) < max_clients:
            # Create new client information
            date = create_date()
            new_client = Client(count, date)
            list_of_clients.append(new_client)
            active_clients.append(new_client)
            count += 1

            # Start the new client thread
            thread = threading.Thread(target=threaded, args=(connection_socket, new_client))
            thread.start()
            all_threads.append(thread)
        else:
            # If the client limit is reached, reject the connection
            print("Maximum clients reached. Connection rejected.")
            connection_socket.send("Server is full. Try again later.".encode())
            connection_socket.close()

# Close the server socket
server_socket.close()
for thread in all_threads:
    thread.join()
sys.exit()  # Terminate the program after sending the corresponding data
