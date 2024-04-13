# tests file
import unittest
from backend.App import createApp
from backend.App.models import db
from sqlalchemy.sql import text

class DatabaseConnectionTest(unittest.TestCase):
    def setUp(self):
        HOSTNAME = "127.0.0.1"
        PORT = 3306
        USERNAME = "root"
        PASSWORD = "2003721gavin?"
        FLASK_DB = "comp3030j"
        """Set up a test application and push an application context."""
        self.app = createApp()  # Use the app factory
        self.app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{FLASK_DB}?charset=utf8mb4'
        self.app.config['TESTING'] = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Tear down the test application context and drop all tables."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_connection(self):
        """Test that we can connect to the database."""
        with db.engine.connect() as connection:
            result = connection.execute(text('SELECT 1'))
        self.assertEqual(result.fetchone()[0], 1, "Database connection failed or SELECT 1 did not return 1")

if __name__ == '__main__':
    unittest.main()
