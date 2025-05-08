from model.user_model import UserModel
from utils.password_generator import generate_password

class UserController:
    def __init__(self):
        self.user_model = UserModel()

    def create_user(self, name, email, password=None):
        if not password:
            password = generate_password()
        self.user_model.add_user(name, email, password)
        return password

    def list_users(self):
        return self.user_model.get_users()