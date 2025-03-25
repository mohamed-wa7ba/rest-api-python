from flask import Flask
from controllers.user_controller import init_user_routes

app = Flask(__name__)

init_user_routes(app)

if __name__ == '__main__':
    app.run(debug=True)