from flask import jsonify

dict = [{'username': 'admin', 'password': 'admin123'},
        {'username': 'brian', 'password': 'brian123'}
        ]


def view_users(app):
    @app.route('/users')
    def get_users():
        return jsonify(dict)
