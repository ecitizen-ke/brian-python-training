from app import create_app
from flask import Flask
from app.books import books_bp
from app.authors import authors_bp
from dotenv import load_dotenv
load_dotenv()

app = create_app()
app.register_blueprint(books_bp)
app.register_blueprint(authors_bp)

if __name__ == "__main__":
    app.run(debug=True)
