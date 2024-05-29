import os
from flask import Flask, render_template
from dotenv import load_dotenv, dotenv_values
load_dotenv()


# print(os.getenv('MY_SECRET_KEYS'))
# print(os.getenv('COMBINED'))
# print(os.getenv('MAIL'))
# config = dotenv_values('.env')
# print(config)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return f'Hello {os.getenv("SECRET_NAME")}, human live for a maximum of {os.getenv("MEANING_OF_LIFE")} years'


@app.route('/admin')
def admin():
    password = input("Enter your password")
    if (password == os.getenv('admin_password')):
        return render_template('admin.html')


if __name__ == '__main__':
    app.run(debug=True)
