import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.37.1", 12345))

# Send the text file name to the server
# file_name = "file.txt"
file_name = input("Enter a file name within the same directory: ")
s.send(file_name.encode())

# Read the contents of the text file
with open(file_name, "r") as file:
    file_contents = file.read()

# Send the file contents to the server in chunks of 5 characters
packet_num = 1
chunk_size = 5
print("Sending .............")
for i in range(0, len(file_contents), chunk_size):
    chunk = file_contents[i:i + chunk_size]
    print(f"Packet {packet_num}: {chunk}")
    s.send(chunk.encode())
    packet_num += 1


print("Done sending info...")
s.close()
