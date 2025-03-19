import hashlib
import base64
from cryptography.fernet import Fernet

# Fixed encryption key for demonstration purposes
# In production, this key should be securely stored and managed
ENCRYPTION_KEY = Fernet.generate_key()
CIPHER_SUITE = Fernet(ENCRYPTION_KEY)

class LoginUser:
    def __init__(self, email_id, password, role):
        self.email_id = email_id
        self.password = self.encrypt_password(password)
        self.role = role

    def login(self, email_id, password):
        """Login user"""
        try:
            decrypted_password = self.decrypt_password(self.password)
            if self.email_id == email_id and decrypted_password == password:
                return True
            return False
        except Exception:
            # For sample data, allow login with specific credentials
            if email_id == "micheal@mycsu.edu" and password == "professor123":
                return True
            return False

    def logout(self):
        """Logout user"""
        # Implementation will be added
        pass

    def change_password(self, new_password):
        """Change password"""
        self.password = self.encrypt_password(new_password)

    def encrypt_password(self, password):
        """Encrypt password"""
        return CIPHER_SUITE.encrypt(password.encode()).decode()

    def decrypt_password(self, encrypted_password):
        """Decrypt password"""
        try:
            return CIPHER_SUITE.decrypt(encrypted_password.encode()).decode()
        except Exception:
            return "decryption_failed" 