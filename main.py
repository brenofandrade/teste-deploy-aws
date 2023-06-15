from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()

@app.get("/healthy")
async def healthy_check():
    return JSONResponse({'healthcheck' : 'Everything OK!'})