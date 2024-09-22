import socket
import json

def main():
    server_address = ('127.0.0.1', 5000)

    clnt_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clnt_socket.connect(server_address)

    filename = input("Enter the filename to search for: ")
    clnt_socket.sendall(filename.encode('utf-8'))
    response = clnt_socket.recv(2048).decode('utf-8')
    print("Received response:", response)

    while True:
        word = input("Enter the word to search (or 'exit' to quit): ")
        if word.lower() == 'exit':
            break
        clnt_socket.sendall(word.encode('utf-8'))
        response = clnt_socket.recv(4096).decode('utf-8')
        try:
            result = json.loads(response)
            print("mapping results:", result)
        except json.JSONDecodeError as e:
            print("Error decoding JSON response:", e)
    clnt_socket.close()

if __name__ == '__main__':
    main()
