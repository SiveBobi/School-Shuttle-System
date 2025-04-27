from .repository import Repository
from src.loan import Loan

class LoanRepository(Repository[Loan, str]):
    """Loan Repository extends the generic Repository for Loan objects."""
    pass
