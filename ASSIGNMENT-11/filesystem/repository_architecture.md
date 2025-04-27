classDiagram
    class Repository~T, ID~ {
        +save(entity)
        +find_by_id(id)
        +find_all()
        +delete(id)
    }

    class BookRepository
    class InMemoryBookRepository
    class FileSystemBookRepository

    Repository <|-- BookRepository
    BookRepository <|-- InMemoryBookRepository
    BookRepository <|-- FileSystemBookRepository
