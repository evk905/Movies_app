import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

dsn = {
    "dbname": os.getenv("DB_NAME", "movies_database"),
    "user": os.getenv("DB_USER", "app"),
    "password": os.getenv("DB_PASSWORD", "123qwe"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", 5432),
}


def create_schema_content():
    try:
        with psycopg2.connect(**dsn) as connection:
            with connection.cursor() as cursor:
                cursor.execute("CREATE SCHEMA IF NOT EXISTS content")
                connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

create_schema_content()
