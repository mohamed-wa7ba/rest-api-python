from config.database import db_pool

def get_db_connection():
    return db_pool.get_connection()