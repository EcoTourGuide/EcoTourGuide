# firebase_config.py

import firebase_admin
from firebase_admin import credentials, auth, firestore, storage

# Path to your Firebase service account key file
SERVICE_ACCOUNT_KEY_PATH = 'EcoTourGuide/ecotourguide-8d78c-firebase-adminsdk-k1t7z-3a27f81e2a.json'

# Initialize the Firebase app
cred = credentials.Certificate(SERVICE_ACCOUNT_KEY_PATH)
firebase_admin.initialize_app(cred)

# Access Firestore, Auth, and Storage services
db = firestore.client()
auth = auth
storage = storage
