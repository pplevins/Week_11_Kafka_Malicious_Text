import uvicorn
from fastapi import FastAPI

from app.api import router as tweets_router

app = FastAPI(
    title="Tweets Database API",
    summary="A FastAPI backend service for retrieving tweets from MongoDB collections.",
)

app.include_router(tweets_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
