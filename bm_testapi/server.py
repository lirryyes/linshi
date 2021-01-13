import uvicorn
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routers import api

app = FastAPI()



origins = [
    "http://localhost",
    "http://localhost:9528",
    "http://localhost:9530", "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router, prefix="/api", tags=["api"])




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8060)