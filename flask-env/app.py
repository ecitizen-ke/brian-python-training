from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TESTING'] = True
print(app.config['DEBUG'])

if __name__ == '__main__':
    app.run()
