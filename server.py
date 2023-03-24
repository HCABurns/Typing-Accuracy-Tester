import socket
import sqlite3
import threading

def client_processing(client_socket):
    
        #Connect to database
        con = sqlite3.connect('typingTester.db')
        #Get the users query.
        query = client_socket.recv(1024).decode('utf-8')
        print(query)
        #Get the query, execute query and send back the result.
        result = con.cursor().execute(query).fetchall()
        client_socket.sendall(str(result).encode('utf-8'))

        #Close the connection to the server
        #con.close()
        #Close the connection
        client_socket.close()

if __name__ == "__main__":
    #Setup a open port for client to connect to.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 55555
    server_socket.bind((host, port))

    #Listen for connections
    server_socket.listen(5)
    print("Server has been loaded")
    while True:
        print("Waiting for connection...")
        print(threading.active_count())
        #Accept a connection from the client
        client_socket, addr = server_socket.accept()
        print('Got connection from', addr)

        #Start a thread to process the query
        thread = threading.Thread(target=client_processing,args=[client_socket])
        thread.start()
        #Join the thread to the main thread once the result has been sent back to the user.
        #thread.join()
