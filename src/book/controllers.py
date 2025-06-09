from flask import jsonify
from .service import (
    create_book_service,
    get_books_service,
    get_book_service,
    update_book_service,
    delete_book_service,
)
from .validation import BookCreateSchema, BookUpdateSchema


def create_book_controller(data: BookCreateSchema, file, cover_image):
    book = create_book_service(data, file, cover_image)
    return jsonify(book), 201


def get_books_controller():
    books = get_books_service()
    return jsonify(books)


def get_book_controller(book_id: int):
    book = get_book_service(book_id)
    if not book:
        return jsonify({"error": "Libro no encontrado"}), 404
    return jsonify(book)


def update_book_controller(
    book_id: int, data: BookUpdateSchema, file=None, cover_image=None
):
    book = update_book_service(book_id, data, file, cover_image)
    if not book:
        return jsonify({"error": "Libro no encontrado"}), 404
    return jsonify(book)


def delete_book_controller(book_id: int):
    result = delete_book_service(book_id)
    return jsonify(result)
