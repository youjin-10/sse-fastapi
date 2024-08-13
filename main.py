from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

async def number_generator():
    for i in range(10):
        yield f"data: {random.randint(0, 100)}\n\n"
        await asyncio.sleep(7)

@app.get("/stream")
async def stream_numbers():
    return StreamingResponse(number_generator(), media_type="text/event-stream")