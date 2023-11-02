#  MUKAGA ISAAC DAVIS 21/U/ITD/5156/PD
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.37.1", 12345))

s.listen(10)
c, addr = s.accept()
print('Connected to client with {} .'.format(addr))

# Receive the text file name from the client
file_name = c.recv(1024).decode()

# Initialize a list to store packet chunks along with their packet numbers
received_chunks = []
print("Receiving......")
packet_num = 1  # Initialize the packet number

while True:
    chunk = c.recv(1024).decode()
    if not chunk:
        break

    # Print each received chunk along with its packet number
    print(f"Packet {packet_num}: {chunk}")

    received_chunks.append(chunk)

    packet_num += 1  # Increment the packet number for the next chunk

# Concatenate the received chunks to obtain the complete file contents
received_contents = ''.join(received_chunks)

# Print the received contents from the client
print("Received contents from the client:")
print(received_contents)

c.close()
s.close()
