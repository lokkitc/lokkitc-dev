from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter
from api.routers.users import user_router
from api.dependencies.auth import login_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API для работы с базой данных", description="API для работы с базой данных")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

main_router = APIRouter()
main_router.include_router(user_router)
app.include_router(main_router, prefix="/users", tags=["users"])
app.include_router(login_router, prefix="/auth", tags=["auth"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    print("\n\n\nServer is running on http://127.0.0.1:8000\n\n\n")
    print("\n\n\nPress Ctrl+C to stop the server\n\n\n")
