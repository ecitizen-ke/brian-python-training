from app import create_app
from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()

from app.views.user import user_bp




app = create_app()
app.register_blueprint(user_bp)

env=os.getenv("ENV")
print(f'you are working on {env} environment')
print(app.config['DB'])
print(app.config['PASSWORD'])
print(app.config['USER'])



if __name__ == "__main__":
    app.run(debug=True)
    