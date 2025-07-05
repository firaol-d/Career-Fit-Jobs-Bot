from fastapi import FastAPI, Response
import asyncio
import logging
from scraper import main as scraper_main
from send_updates import send_job_updates

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/run-scraper")
async def run_scraper():
    try:
        await scraper_main()
        return {"status": "scraper started"}
    except Exception as e:
        logging.exception("Error running scraper")
        return Response(content=str(e), status_code=500)

@app.post("/send-updates")
async def run_send_updates():
    try:
        await send_job_updates()
        return {"status": "send updates started"}
    except Exception as e:
        logging.exception("Error sending updates")
        return Response(content=str(e), status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000)
