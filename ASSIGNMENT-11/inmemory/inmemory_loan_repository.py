from typing import Optional, List
from repositories.loan_repository import LoanRepository
from src.loan import Loan

class InMemoryLoanRepository(LoanRepository):
    def __init__(self):
        self._storage = {}

    def save(self, loan: Loan) -> None:
        self._storage[loan.loan_id] = loan

    def find_by_id(self, loan_id: str) -> Optional[Loan]:
        return self._storage.get(loan_id)

    def find_all(self) -> List[Loan]:
        return list(self._storage.values())

    def delete(self, loan_id: str) -> None:
        if loan_id in self._storage:
            del self._storage[loan_id]
