from repositories.book_repository import BookRepository
from repositories.user_repository import UserRepository
from repositories.loan_repository import LoanRepository
from repositories.reservation_repository import ReservationRepository

from repositories.inmemory.inmemory_book_repository import InMemoryBookRepository
from repositories.inmemory.inmemory_user_repository import InMemoryUserRepository
from repositories.inmemory.inmemory_loan_repository import InMemoryLoanRepository
from repositories.inmemory.inmemory_reservation_repository import InMemoryReservationRepository

# Later you can add:
# from repositories.filesystem.filesystem_book_repository import FileSystemBookRepository
# from repositories.database.database_book_repository import DatabaseBookRepository

class RepositoryFactory:
    @staticmethod
    def get_book_repository(storage_type: str) -> BookRepository:
        if storage_type.upper() == "MEMORY":
            return InMemoryBookRepository()
        elif storage_type.upper() == "FILESYSTEM":
            raise NotImplementedError("FileSystemBookRepository not implemented yet.")
        elif storage_type.upper() == "DATABASE":
            raise NotImplementedError("DatabaseBookRepository not implemented yet.")
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")

    @staticmethod
    def get_user_repository(storage_type: str) -> UserRepository:
        if storage_type.upper() == "MEMORY":
            return InMemoryUserRepository()
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")

    @staticmethod
    def get_loan_repository(storage_type: str) -> LoanRepository:
        if storage_type.upper() == "MEMORY":
            return InMemoryLoanRepository()
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")

    @staticmethod
    def get_reservation_repository(storage_type: str) -> ReservationRepository:
        if storage_type.upper() == "MEMORY":
            return InMemoryReservationRepository()
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")
