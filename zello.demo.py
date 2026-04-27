import asyncio
import json
import websockets

WEBSOCKET_URL = "wss://zellowork.io/ws/demoaccount2025"
USERNAME = "david"
PASSWORD = "ellie"
CHANNEL = "Is this thing on"

async def run():
    async with websockets.connect(WEBSOCKET_URL) as ws:

        await ws.send(json.dumps({
            "command": "logon",
            "seq": 1,
            "username": USERNAME,
            "password": PASSWORD,
            "channels": [CHANNEL]
        }))
        print(await ws.recv())

        await asyncio.sleep(1)

        await ws.send(json.dumps({
            "command": "send_text_message",
            "seq": 2,
            "channel": CHANNEL,
            "text": "Hey eveyone, lunch on me today!"
        }))
        print(await ws.recv())

asyncio.run(run())