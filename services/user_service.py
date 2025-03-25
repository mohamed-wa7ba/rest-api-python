from models.user_model import UserModel

class UserService:
    @staticmethod
    def add_user(user_data):
        return UserModel.create_user(user_data['name'], user_data['email'])
    @staticmethod
    def get_users():
        return UserModel.get_all_users()