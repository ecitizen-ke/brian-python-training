from flask import jsonify

def view_index(app):
    @app.route('/')
    def index():
        return '<h1> hello, world! </h1>'
