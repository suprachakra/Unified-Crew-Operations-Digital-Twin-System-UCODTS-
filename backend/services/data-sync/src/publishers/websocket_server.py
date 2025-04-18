"""
WebSocket Server – provides real-time client updates.
"""

import asyncio
import websockets
import logging

async def handler(websocket, path):
    try:
        await websocket.send("Connected to Real-Time Data Sync Service")
    except Exception as e:
        logging.error("WebSocket error: %s", e)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    start_server = websockets.serve(handler, "0.0.0.0", 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
