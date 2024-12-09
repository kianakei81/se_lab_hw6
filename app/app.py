from flask import Flask, redirect, request
import requests

app = Flask(__name__)

@app.route('/items', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users_proxy_forwarding():
    # Forward the request to the /users Flask service
    response = requests.request(
        method=request.method,
        url=f"http://item:5001/items",
        headers={key: value for key, value in request.headers},
        json=request.get_json(silent=True),
    )
    return (response.text, response.status_code, response.headers.items())

@app.route('/items/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users_proxy(path):
    # Forward the request to the /users Flask service
    response = requests.request(
        method=request.method,
        url=f"http://item:5001/items/{path}",
        headers={key: value for key, value in request.headers},
        json=request.get_json(silent=True),
    )
    return (response.text, response.status_code, response.headers.items())

@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def items_proxy_forwarding():
    # Forward the request to the /items Flask service
    response = requests.request(
        method=request.method,
        url=f"http://user:5002/users",
        headers={key: value for key, value in request.headers},
        json=request.get_json(silent=True),
    )
    return (response.text, response.status_code, response.headers.items())

@app.route('/users/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def items_proxy(path):
    # Forward the request to the /items Flask service
    response = requests.request(
        method=request.method,
        url=f"http://user:5002/users/{path}",
        headers={key: value for key, value in request.headers},
        json=request.get_json(silent=True),
    )
    return (response.text, response.status_code, response.headers.items())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # Gateway running on port 8080

