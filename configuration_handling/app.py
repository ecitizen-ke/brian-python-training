from app import app
from dotenv import load_dotenv
load_dotenv = load_dotenv
import os

env=os.getenv("ENV")
print(f'you are working on {env} environment')
@app.route('/')
def hello_world():
    print(app.config['DB_NAME'])
    
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)