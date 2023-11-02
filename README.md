

# File Transfer with Client-Server Communication

This project consists of a Python client and server for transferring a text file from the client to the server using socket communication. The server receives the file name and its contents, while the client reads the file and sends it to the server.

## Prerequisites

- Python 3.x installed on both the client and server machines.

## Usage

1. First, run the server script on the server machine. Make sure to configure the IP address and port for the server machine in both scripts :

```bash
python server.py
```

2. Then, run the client script on the client machine. You will be prompted to enter the name of the text file you want to transfer. The client will read the file,and send it to the server:

```bash
python client.py
```

3. The server will receive the text file name and its contents in chunks. It will print each received chunk along with its packet number, and finally, it will print the entire received text file contents.

## Server (server.py)

The server script performs the following steps:

1. Establishes a socket connection and listens for incoming connections from clients.

2. Receives the text file name from the client.

3. Initializes a list to store packet chunks along with their packet numbers.

4. Loops to receive each packet, splits it into packet numbers and content, and appends the packet to the list.

5. Prints each received chunk along with its packet number.

6. Concatenates the received chunks to obtain the complete file contents.

7. Prints the received contents from the client.

8. Closes the connection.

## Client (client.py)

The client script performs the following steps:

1. Establishes a socket connection to the server.

2. Prompts the user to enter the name of a text file in the same directory that they want to transfer.

3. Sends the entered file name to the server.

4. Reads the contents of the specified text file.

5. Sends the contents to the server in chunks of 5 characters, with each chunk being printed along with its packet number.

6. Closes the connection after sending all chunks.




