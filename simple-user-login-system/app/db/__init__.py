import mysql.connector

from app import create_app

app= create_app()


class Connection:
    """This class provides connection to our database"""

    def __init__(self):
        self.host = app.config['HOST']
        self.db = app.config['DB']
        self.user = app.config['USER']
        self.password = app.config['PASSWORD']

        # Create a db connection
        self.conn = mysql.connector.connect(
            host=self.host, database=self.db, user=self.user, password=self.password
        )

        # Create cursor
        self.cursor = self.conn.cursor()
        