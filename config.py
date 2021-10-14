import os

DB_SETTINGS = {
    'dev': {
        'SOURCE_DB': {
            'SOURCE_DB_TYPE': 'mysql',
            'SOURCE_DB_HOST': '127.0.0.1',
            'SOURCE_DB_NAME': 'mydb',
            'SOURCE_DB_USER': os.getenv('DB_USER'),
            'SOURCE_DB_PASS': os.getenv('DB_PASSWORD')
        },
        'TARGET_DB_TYPE': {
            'TARGET_DB_TYPE': 'postgres',
            'TARGET_DB_HOST': '127.0.0.1',
            'TARGET_DB_NAME': 'mydb',
            'TARGET_DB_USER': os.getenv('DB_USER'),
            'TARGET_DB_PASS': os.getenv('DB_PASSWORD')
        }

    }
}