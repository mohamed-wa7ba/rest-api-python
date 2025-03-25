from flask import jsonify, request
from services.user_service import UserService
from utils.responses import success_response, error_response

def init_user_routes(app):
    @app.route('/users', methods=['GET'])
    def get_users():
        users = UserService.get_users()
        return success_response(users)

    @app.route('/user', methods=['POST'])
    def add_user():
        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data:
            return error_response("Missing data", 400)
        
        UserService.add_user(data)
        return success_response("User added successfully", 201)