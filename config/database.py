import os
from dotenv import load_dotenv
from mysql.connector import pooling

load_dotenv()

class DatabaseConfig:
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '12345678')
    MYSQL_DB = os.getenv('MYSQL_DB', 'shop')
    POOL_SIZE = int(os.getenv('DB_POOL_SIZE', '5'))

# إنشاء connection pool
db_pool = pooling.MySQLConnectionPool(
    pool_name="my_pool",
    pool_size=DatabaseConfig.POOL_SIZE,
    host=DatabaseConfig.MYSQL_HOST,
    user=DatabaseConfig.MYSQL_USER,
    password=DatabaseConfig.MYSQL_PASSWORD,
    database=DatabaseConfig.MYSQL_DB
)