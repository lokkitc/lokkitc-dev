from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter
from api.routers.users import user_router
from api.dependencies.auth import login_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI(title="API для работы с базой данных", description="API для работы с базой данных")
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(login_router, prefix="/auth", tags=["auth"])

@app.get("/debug/static-path")
async def debug_static_path():
    static_dir = BASE_DIR / "static"
    return {
        "base_dir": str(BASE_DIR),
        "static_dir": str(static_dir),
        "static_dir_exists": static_dir.exists(),
        "static_contents": [str(f) for f in static_dir.glob("**/*") if f.is_file()] if static_dir.exists() else []
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    print("\n\n\nServer is running on http://127.0.0.1:8000\n\n\n")
    print("\n\n\nPress Ctrl+C to stop the server\n\n\n")
