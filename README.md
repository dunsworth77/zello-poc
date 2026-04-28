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

Make sure you have Python 3.8 or higher installed. Open a terminal in the folder containing `zello.demo.py` and run:

```bash
python zello.demo.py
```

If you are on a Mac or Linux machine and `python` defaults to Python 2, use:

```bash
python3 zello.demo.py
```

The script will automatically connect to the WebSocket endpoint, authenticate, and send a text message to the configured channel.

---

## What Success Looks Like

**In your terminal** you should see two JSON responses printed:

{"seq": 1, "success": true}
{"seq": 2, "success": true}

The first confirms authentication was successful. The second confirms the text message was delivered to the channel.

**In the Zello app**, the message will appear in real time inside the channel you configured. If you are logged in as the admin user on the app, you will see the message arrive from the user account defined in the script.

**If something goes wrong**, check the following:
- Confirm your network name in the URL is correct
- Confirm the user is added to the channel in the Web Console
- Confirm the channel name in the script exactly matches the Web Console (case sensitive)