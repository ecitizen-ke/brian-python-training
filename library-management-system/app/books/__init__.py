from flask import Blueprint, request

books_bp = Blueprint('books_bp', __name__, )
books = []

# view to create a book


@books_bp.route('/books/create', methods=['POST'])
def index():
    book = {'id': len(books)+1, 'title': '', 'description': ''}
    book['title'] = request.get_json().get('title')
    book['description'] = request.get_json().get('description')
    books.append(book)
    return book

# view to display books


@books_bp.route('/books/display')
def display():
    return books

# view to update a book


@books_bp.route('/books/update/<int:id>', methods=['POST'])
def update(id):
    book = next((book for book in books if book["id"] == id), None)
    if not book:
        return 'book not found!'

    book['title'] = request.get_json().get('title')
    book['description'] = request.get_json().get('description')

    return book

# view to delete a book


@books_bp.route('/books/delete/<int:id>', methods=['DELETE'])
def delete(id):
    global books
    filterd_books = [book for book in books if book["id"] != id]

    books = filterd_books

    return books
