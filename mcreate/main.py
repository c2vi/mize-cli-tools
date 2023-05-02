
import websocket
import sys
import json

sock = websocket.WebSocket()
sock.connect("ws://localhost:9432/api/socket")

if not sys.stdin.isatty():
    # read from tty, parse as json and add as item
    string = sys.stdin.read()
    msg = {
        "cmd": "item.create",
        "item": json.loads(string)
        }
    sock.send(json.dumps(msg))
    id_msg = json.loads(sock.recv())
    print("Created Item with id: ", id_msg["id"])

else: 
    msg = {
        "cmd": "item.create",
        "item": {}
        }
    sock.send(json.dumps(msg))
    id_msg = json.loads(sock.recv())
    print("Created Item with id: ", id_msg["id"])


