# - *- coding: utf- 8 - *-
import psycopg

from config import DB_NAME, HOST, PASSWORD, USER


async def is_user(tg_id):
    async with await psycopg.AsyncConnection.connect(user=USER, password=PASSWORD, host=HOST, dbname=DB_NAME) as aconn:
        async with aconn.cursor() as cur:
            await cur.execute('SELECT * FROM users WHERE tg_id = %s', (tg_id,))
            user_id = await cur.fetchone()
            return user_id


async def add_user(tg_id, username):
    async with await psycopg.AsyncConnection.connect(user=USER, password=PASSWORD, host=HOST, dbname=DB_NAME) as aconn:
        async with aconn.cursor() as cur:
            await cur.execute('INSERT INTO users (tg_id, username) VALUES (%s, %s)', (tg_id, username,))
            await aconn.commit()


async def get_hello_message(tg_id, name):
    async with await psycopg.AsyncConnection.connect(user=USER, password=PASSWORD, host=HOST, dbname=DB_NAME) as aconn:
        async with aconn.cursor() as cur:
            await cur.execute('SELECT character_id, hello_message FROM character WHERE name = %s', (name,))
            data = await cur.fetchone()
            char_id, hello_message = data
            await cur.execute('UPDATE dialog SET character_id = %s WHERE tg_id = %s', (char_id, tg_id,))
            await aconn.commit()
            return hello_message


async def set_dialog(tg_id):
    async with await psycopg.AsyncConnection.connect(user=USER, password=PASSWORD, host=HOST, dbname=DB_NAME) as aconn:
        async with aconn.cursor() as cur:
            await cur.execute('INSERT INTO dialog (tg_id) VALUES (%s)', (tg_id,))
            await aconn.commit()


async def get_dialog_name(tg_id):
    async with await psycopg.AsyncConnection.connect(user=USER, password=PASSWORD, host=HOST, dbname=DB_NAME) as aconn:
        async with aconn.cursor() as cur:
            await cur.execute('SELECT name '
                              'FROM character c '
                              'INNER JOIN dialog d '
                              'ON c.character_id = d.character_id '
                              'WHERE d.tg_id = %s', (tg_id,))
            data = await cur.fetchone()
            return data
