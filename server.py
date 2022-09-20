from fastapi import FastAPI
import uvicorn
from fastapi import Request

app = FastAPI()


@app.get('/')
def root():
    return {"message":"Server is up and running"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8100)
