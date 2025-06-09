import os
from werkzeug.utils import secure_filename
from .validation import BookCreateSchema, BookUpdateSchema
from ..models.book import Book
from ..database.database import SessionLocal

BOOKS_DIR = "src/static/books"
COVERS_DIR = "src/static/covers"
os.makedirs(BOOKS_DIR, exist_ok=True)
os.makedirs(COVERS_DIR, exist_ok=True)


def save_file_locally(file, folder, allowed_exts):
    filename = secure_filename(file.filename)
    ext = filename.split(".")[-1].lower()
    if ext not in allowed_exts:
        raise ValueError(f"Formato no permitido: {ext}")
    file_path = os.path.join(folder, filename)
    file.save(file_path)
    return file_path


def book_to_dict(book):
    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "description": book.description,
        "file_path": book.file_path,
        "cover_image": book.cover_image,
    }


def create_book_service(data: BookCreateSchema, file, cover_image):
    db = SessionLocal()
    try:
        file_path = save_file_locally(file, BOOKS_DIR, ["epub"])
        cover_path = None
        if cover_image:
            cover_path = save_file_locally(
                cover_image, COVERS_DIR, ["jpg", "jpeg", "png", "webp"]
            )
        book = Book(
            title=data.title,
            author=data.author,
            description=data.description,
            file_path=file_path,
            cover_image=cover_path,
        )
        db.add(book)
        db.commit()
        db.refresh(book)
        return book_to_dict(book)
    finally:
        db.close()


def get_books_service():
    db = SessionLocal()
    try:
        books = db.query(Book).all()
        return [book_to_dict(b) for b in books]
    finally:
        db.close()


def get_book_service(book_id: int):
    db = SessionLocal()
    try:
        book = db.query(Book).filter(Book.id == book_id).first()
        if not book:
            return None
        return book_to_dict(book)
    finally:
        db.close()


def update_book_service(
    book_id: int, data: BookUpdateSchema, file=None, cover_image=None
):
    db = SessionLocal()
    try:
        book = db.query(Book).filter(Book.id == book_id).first()
        if not book:
            return None
        if data.title is not None:
            book.title = data.title
        if data.author is not None:
            book.author = data.author
        if data.description is not None:
            book.description = data.description
        if file:
            book.file_path = save_file_locally(file, BOOKS_DIR, ["epub"])
        if cover_image:
            book.cover_image = save_file_locally(
                cover_image, COVERS_DIR, ["jpg", "jpeg", "png", "webp"]
            )
        db.commit()
        db.refresh(book)
        return book_to_dict(book)
    finally:
        db.close()


def delete_book_service(book_id: int):
    db = SessionLocal()
    try:
        book = db.query(Book).filter(Book.id == book_id).first()
        if not book:
            return {"error": "Libro no encontrado"}
        db.delete(book)
        db.commit()
        return {"detail": "Libro eliminado"}
    finally:
        db.close()
