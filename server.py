import socket
import json
from search import Search

def start_server(host='127.0.0.1', port=5000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()
    print(f'Server listening on {host}:{port}')

    while True:
        conn, addr = s.accept()
        with conn:
            print(f'Connected by {addr}')
            filename = conn.recv(1024).decode('utf-8')
            try:
                word_search = Search(filename)
                word_search.clean()
                conn.sendall(b'{"status": "File added successfully"}\n')
            except FileNotFoundError as e:
                error_response = json.dumps({"error": str(e)}).encode('utf-8')
                conn.sendall(error_response)
                continue

            while True:
                try:
                    pattern = conn.recv(4096).decode('utf-8')
                    if not pattern:
                        print(f'Client {addr} disconnected.')
                        break

                    result = word_search.getLines(pattern)
                    response = json.dumps(result).encode('utf-8')
                    conn.sendall(response + b'\n')
                except Exception as e:
                    print(f'Error receiving data from {addr}: {e}')
                    break

if __name__ == '__main__':
    start_server()
