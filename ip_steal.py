from flask import Flask, request, render_template, jsonify 
import socket

app = Flask(__name__)

def send_ip_to_socket(ip_address):
    """
    Sends the IP address to a TCP socket server on localhost:8080
    """
    HOST = "0.0.0.0"
    PORT = 8018
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(ip_address.encode())
            
    except ConnectionRefusedError:
        print(f"Could not connect to {HOST}:{PORT}")

@app.route("/")
def index():
    """
    Displays the visitor's real IP address (works with ngrok or proxies).
    """
    if "X-Forwarded-For" in request.headers:
        ip_address = request.headers.get("X-Forwarded-For").split(",")[0].strip()
    else:
        ip_address = request.remote_addr

    # Send IP to socket server
    send_ip_to_socket(ip_address)

    return jsonify("Page could not be found")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    
