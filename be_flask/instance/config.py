import os

SECRET = os.environ.get('SECRET') or "12345"

# MONGO CONFIG
MONGO_HOST = os.environ.get('MONGO_HOST') or 'localhost'
MONGO_PORT = int(os.environ.get('MONGO_PORT') or 27017)
MONGO_DBNAME = os.environ.get('MONGO_DBNAME') or 'todo'

# MONGO COLLECTIONS
MONGO_COL_TODO = 'todo'
MONGO_COL_USERS = 'users'
