import os.path as Path
import sqlite3

SQL_SELECT_ALL = """
    SELECT id, original_url, short_url, created FROM shortener
"""

SQL_SELECT_URL_BY_PK = SQL_SELECT_ALL + " WHERE id=?"

SQL_SELECT_URL_BY_ORIGINAL = SQL_SELECT_ALL+ " WHERE original_url=?"

SQL_SELECT_URL_BY_SHORT = SQL_SELECT_ALL+ " WHERE short_url=?"

SQL_INSERT_URL = """
    INSERT INTO shortener (original_url) VALUES (?)
"""

SQL_UPDATE_SHORT_URL = """
    APDATE shortener SET short_url=? WHERE id=?
"""


def connect(db_name=None):
	if db_name is None:
		db_name = ':memory:'

	conn = sqlite3.connect(db_name)
#магия
	return conn

def initialize(conn, creation_shema):
    with conn, open(creation_shema) as f:
        conn.executescript(f.read()) 


def add_url(conn, url, domain=''): 
    """Сохраняет новый URL-адресс в базу"""

def find_all(conn):
	"""Возвращает все URL Адреса из базы"""

def find_url_by_pk(conn, pk):
	"""Возвращает URL по первичному ключу"""

def find_url_by_shrt(conn, short_url):
	"""Возвращает URL  ПО оригинальному URL-y""""