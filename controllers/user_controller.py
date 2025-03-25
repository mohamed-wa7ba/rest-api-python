from flask import jsonify, request
from services.user_service import UserService
from utils.responses import success_response, error_response

def init_user_routes(app):
    @app.route('/api/users', methods=['GET', 'OPTIONS'])  
    def get_users():
        users = UserService.get_users()
        return success_response(users)

    @app.route('/api/user', methods=['POST', 'OPTIONS'])  
    def add_user():
        if request.method == 'OPTIONS':
            return _handle_options_request()
            
        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data:
            return error_response("Missing data", 400)
        
        UserService.add_user(data)
        return success_response("User added successfully", 201)

    def _handle_options_request():
        response = jsonify()
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response