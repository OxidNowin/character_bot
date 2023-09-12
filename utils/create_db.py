# - *- coding: utf- 8 - *-
import psycopg
from config import DB_NAME, HOST, PASSWORD, USER


def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS users (
            tg_id BIGINT UNIQUE NOT NULL,
            username VARCHAR(255),
            name VARCHAR(255),
            surname VARCHAR(255),
            time TIMESTAMP DEFAULT now()
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS character (
            character_id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            hello_message TEXT
        )
        """,

        """
        CREATE TABLE IF NOT EXISTS dialog (
            dialog_id SERIAL PRIMARY KEY,
            tg_id BIGINT UNIQUE NOT NULL REFERENCES users(tg_id),
            character_id INT REFERENCES character(character_id)
        )
        """,
    )
    conn = psycopg.connect(user=USER, password=PASSWORD, host=HOST, dbname=DB_NAME)
    cur = conn.cursor()
    for com in commands:
        cur.execute(com)
    conn.commit()
    cur.close()
    conn.close()
