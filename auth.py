import streamlit as st
import pyrebase
import firebase_admin
from firebase_admin import credentials, auth as admin_auth
import json
from firebase_admin import firestore

# Firebase configuration (replace with your own config)
firebase_config = dict(st.secrets["firebase"])

# Initialize Pyrebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Firebase Admin SDK setup
if not firebase_admin._apps:
    cred = credentials.Certificate(dict(st.secrets["firebase_admin"]))
    firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Streamlit session state keys
USER_KEY = "user"
ID_TOKEN_KEY = "id_token"

# Sign Up
def sign_up(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        st.session_state[USER_KEY] = user
        st.success("Successfully signed up!")
        return user
    except Exception as e:
        error_message = json.loads(e.args[1])['error']['message']
        if error_message == 'EMAIL_EXISTS':
            st.error("The email address is already in use by another account.")
        elif error_message == 'WEAK_PASSWORD : Password should be at least 6 characters':
            st.error("The password is too weak. It should be at least 6 characters long.")
        else:
            st.error(f"Error: {error_message}")
        return None

# Sign In
def sign_in(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        st.session_state[USER_KEY] = user
        st.session_state[ID_TOKEN_KEY] = user['idToken']
        st.success("Successfully signed in!")
        return user
    except Exception as e:
        error_message = json.loads(e.args[1])['error']['message']
        if error_message == 'EMAIL_NOT_FOUND':
            st.error("There is no user record corresponding to this email.")
        elif error_message == 'INVALID_PASSWORD':
            st.error("The password is invalid or the user does not have a password.")
        else:
            st.error(f"Error: {error_message}")
        return None

# Sign Out
def sign_out():
    if USER_KEY in st.session_state:
        del st.session_state[USER_KEY]
        del st.session_state[ID_TOKEN_KEY]
    st.success("Successfully signed out!")

# Get the current user
def get_current_user():
    return st.session_state.get(USER_KEY)

# Get ID token
def get_id_token():
    return st.session_state.get(ID_TOKEN_KEY)
