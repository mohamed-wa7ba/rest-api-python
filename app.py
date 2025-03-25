from flask import Flask
from config.cors import init_cors  
from controllers.user_controller import init_user_routes

app = Flask(__name__)


init_cors(app)

init_user_routes(app)

if __name__ == '__main__':
    app.run(debug=True)