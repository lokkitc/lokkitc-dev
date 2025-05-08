from fastapi import APIRouter
from api.routers import users, movies, comments
from api.routers.auth import login_router

main_router = APIRouter()

main_router.include_router(login_router, prefix="/auth", tags=["auth"])
main_router.include_router(users.user_router, prefix="/users", tags=["users"])
main_router.include_router(movies.movie_router, prefix="/movies", tags=["movies"])
main_router.include_router(comments.comment_router, prefix="/comments", tags=["comments"])
