# Zello Channel API – WebSocket Proof of Concept

A minimal Python script that connects to a Zello Work channel via WebSocket, authenticates as a user, and sends a text message.

---

## Prerequisites

- Python 3.8 or higher
- The `websockets` library (one-time install):

pip install websockets

---

## Configuration

Open `zello_demo.py` and update the four variables at the top of the file:

WEBSOCKET_URL = "wss://zellowork.io/ws/YOUR_NETWORK_NAME"
USERNAME = "your_username"
PASSWORD = "your_password"
CHANNEL = "your_channel_name"

| Variable | Where to find it |
|---|---|
| `WEBSOCKET_URL` | Replace `YOUR_NETWORK_NAME` with the network name from your Web Console URL |
| `USERNAME` | The user you created in the Web Console |
| `PASSWORD` | The password set for that user |
| `CHANNEL` | The channel name you created in the Web Console |

> **Note:** Use the staging credentials provided in the exercise brief.

---

## How to Run

python zello_demo.py

---

## What Success Looks Like

You should see two lines printed in your terminal:

{"seq": 1, "success": true}
{"seq": 2, "success": true}

Simultaneously, the te