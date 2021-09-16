#!/usr/bin/env python3
import socket, time, sys
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

# TODO: get_remote_ip() method
def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting ...')
        sys.exit()

    print(f'IP address of {host} is {remote_ip}')
    return remote_ip

# TODO: handle_request() method
def handle_request(proxy_end, conn):
    time.sleep(0.5)
    send_full_data = conn.recv(BUFFER_SIZE)
    proxy_end.sendall(send_full_data)
    proxy_end.shutdown(socket.SHUT_WR)
    data = proxy_end.recv(BUFFER_SIZE)
    conn.send(data)


def main():
     # TODO: establish localhost, extern_host (google), port, buffer size
    extern_host = 'www.google.com'
    extern_port = 80
    
    # create socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        print("Starting proxy server")
        # allow reused addresses, bind, and set to listening mode
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(5) # possibly change this 

        while True:
            # connect proxy_start
            conn, addr = proxy_start.accept()
            print("Connected by ", addr)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                # TODO: get remote IP of Google, connect proxy_end to it
                print(f"Connecting to {extern_host}")
                remote_ip = get_remote_ip(extern_host)
                proxy_end.connect((remote_ip, extern_port))

                # allow for multiple conections with a Process Daemon
                p = Process(target=handle_request, args=(proxy_end, conn))
                p.daemon = True
                p.start()
                print("Started process", p)

            conn.close()

if __name__ == '__main__':
    main()
