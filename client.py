import socket

#Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 55555
client_socket.connect((host, port))
#Send query
command = "Select * FROM Scores;"
client_socket.sendall(command.encode('utf-8'))

#Get the response and return it 
scores = client_socket.recv(1024).decode('utf-8')
#Close the client socket
client_socket.close()

print(scores)


