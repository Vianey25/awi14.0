import pyrebase
import firebase_config as token

firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth()

email="uno@gmail.com"
password="123456"

user = auth.sign_in_with_email_and_password(email, password)
print(user)