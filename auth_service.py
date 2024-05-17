import pyrebase
from config import firebase_config

class AuthService:
    def __init__(self):
        firebase = pyrebase.initialize_app(firebase_config)
        self.auth = firebase.auth()

    def login(self, email, password):
        try:
            user = self.auth.sign_in_with_email_and_password(email, password)
            return user
        except:
            return None

