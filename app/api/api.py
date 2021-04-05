from fastapi import APIRouter

from api.endpoints import quiz, post_quiz

api_router = APIRouter()

api_router.include_router(
    quiz.router,
    tags=['quiz'],
    prefix='/quiz'
)
api_router.include_router(
    post_quiz.router,
    tags=['post_quiz'],
    prefix='/post_quiz'
)
