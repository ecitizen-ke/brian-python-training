from flask import Blueprint, request

authors_bp = Blueprint('authors_bp', __name__, )
authors = []

# view to create a book


@authors_bp.route('/authors/create', methods=['POST'])
def create_author():
    author = {'id': len(authors)+1, 'name': ''}
    author['name'] = request.get_json().get('name')
    authors.append(author)
    return author
# view to display authors


@authors_bp.route('/authors/display', methods=['GET'])
def display_authors():
    return {'authors': authors}
# view to delete an author


@authors_bp.route('/authors/update/<int:id>', methods=['POST'])
def update_authors(id):
    author = next((author for author in authors if author["id"] == id), None)
    if not author:
        return 'author not found!'

    author['name'] = request.get_json().get('name')

    return {'author': author}
# veiw to delete author


@authors_bp.route('/authors/delete/<int:id>', methods=['DELETE'])
def delete_authors(id):
    filter_authors = [author for author in authors if author["id"] != id]
    books = filter_authors
    return books
