# client-server-communication-application
TCP Client-Server Chat Application
This repository contains a simple client-server communication (chat) application built using TCP sockets in Python. The server manages multiple clients, assigns them unique names, echoes back their messages with an acknowledgment, and maintains an in-memory cache of connected clients during the session.

Features
Client Naming: Clients are automatically assigned names in the form Client01, Client02, and so on.
Limited Connections: The server can handle up to 3 clients simultaneously (configurable).
Message Echo with ACK: Clients can send any message, and the server will echo the message back, appending the word "ACK".
Status Query: Clients can request the server to display the current cache (connected clients and connection times) by sending a status message.
Graceful Exit: Clients can terminate the connection by sending an exit message.
Requirements
Python 3.x
Sockets module (comes with Python standard library)
Usage
1. Clone the Repository
bash
Copy code
git clone <repository-url>
cd <repository-folder>
2. Server
To start the server, run:

bash
Copy code
python server.py
The server will listen for incoming client connections and can serve up to 3 clients at once.

3. Client
To start a client, run:

bash
Copy code
python client.py
Each client will connect to the server and receive a unique name. Clients can send messages via CLI, which the server will echo back with "ACK". Additionally, clients can send:

status: to get the current cache of connected clients.
exit: to terminate the connection.
Example Communication
Start the server.
Launch multiple clients.
Each client will be assigned a name, such as Client01, Client02, etc.
Clients can send messages:
Client sends: Hello, Server!
Server responds: Hello, Server! ACK
Clients can request the server's cache by sending status.
Clients can terminate the connection by sending exit.
In-Memory Cache
The server maintains a cache that includes:

Client name
Date and time when the connection was established
Date and time when the connection was terminated
This cache is only stored in memory and is reset upon restarting the server.

Configuration
The maximum number of clients is hardcoded as 3. You can adjust this in the server code if needed.
How It Works
Server:

The server listens on a TCP socket for incoming connections.
When a client connects, it assigns a unique name and stores the connection details in the cache.
It responds to client messages, echoing them back with "ACK".
The server supports up to 3 simultaneous connections.
Client:

The client connects to the server using a TCP socket.
After receiving a unique name, the client can send messages via the command line.
The client can query the server's cache with status or close the connection with exit.
To-Do
 Add error handling for connection timeouts or unexpected disconnections.
 Implement a more dynamic way to set the maximum number of clients.
License
This project is licensed under the MIT License.

