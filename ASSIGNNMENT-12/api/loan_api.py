from fastapi import APIRouter, HTTPException
from services.loan_service import LoanService
from repositories.inmemory.inmemory_loan_repository import InMemoryLoanRepository
from repositories.inmemory.inmemory_book_repository import InMemoryBookRepository
from repositories.inmemory.inmemory_user_repository import InMemoryUserRepository
from src.loan import Loan

router = APIRouter(prefix="/api/loans", tags=["Loans"])

loan_service = LoanService(
    InMemoryLoanRepository(),
    InMemoryBookRepository(),
    InMemoryUserRepository()
)

@router.post("/")
def create_loan(loan: Loan):
    try:
        loan_service.create_loan(loan)
        return {"message": "Loan created"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
