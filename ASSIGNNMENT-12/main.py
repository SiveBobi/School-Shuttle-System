from fastapi import FastAPI
from api.book_api import router as book_router
from api.user_api import router as user_router
from api.loan_api import router as loan_router

app = FastAPI(title="📚 Library API", description="Book + User + Loan API with FastAPI")

app.include_router(book_router)
app.include_router(user_router)
app.include_router(loan_router)
