from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from api.router import main_router
from api.middleware.timing import TimingMiddleware
from config.logging_config import setup_logging

setup_logging()

app = FastAPI(
    title="API для работы с базой данных",
    description="API для работы с базой данных"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(TimingMiddleware)
app.include_router(main_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
    print("\nServer is running on http://127.0.0.1:8000\n")
    print("Press Ctrl+C to stop the server\n")
