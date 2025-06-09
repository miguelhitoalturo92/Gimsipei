from flask import Blueprint, request, jsonify
from .controllers import (
    create_book_controller,
    get_books_controller,
    get_book_controller,
    update_book_controller,
    delete_book_controller,
)
from .validation import BookCreateSchema, BookUpdateSchema
from pydantic import ValidationError

book_bp = Blueprint("books", __name__, url_prefix="/books")


@book_bp.route("/", methods=["POST"])
def create_book():
    try:
        data = BookCreateSchema(**request.form)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    file = request.files.get("file")
    cover_image = request.files.get("cover_image")
    if not file:
        return jsonify({"error": "Archivo del libro es requerido"}), 400
    return create_book_controller(data, file, cover_image)


@book_bp.route("/", methods=["GET"])
def list_books():
    return get_books_controller()


@book_bp.route("/<int:book_id>", methods=["GET"])
def get_book(book_id):
    return get_book_controller(book_id)


@book_bp.route("/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    try:
        data = BookUpdateSchema(**request.form)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    file = request.files.get("file")
    cover_image = request.files.get("cover_image")
    return update_book_controller(book_id, data, file, cover_image)


@book_bp.route("/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    return delete_book_controller(book_id)
