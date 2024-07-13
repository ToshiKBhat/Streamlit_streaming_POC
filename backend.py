from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

def generate():
    for i in range(1, 6):
        yield f"Chunk {i}\n"
        time.sleep(1)

@app.get("/stream")
def stream():
    return StreamingResponse(generate(), media_type="text/plain")

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("favicon.ico")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
