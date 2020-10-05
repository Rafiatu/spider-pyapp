# first import all necessary dependencies.
import psycopg2
from decouple import config
from src.db.pages import Pages
from src.db.links import Links


class DB:
  @classmethod
  def pre_connect(cls):
    '''pre-connect function drops the database if it already exists,
    it then creates the database.
    '''
    try:
      connection = psycopg2.connect(
        dbname=None,
        port=config('DB_PORT'),
        host=config('DB_HOST'),
        user=config('DB_USER'),
        password=config('DB_PASSWORD')
      )
      connection.autocommit = True
      cursor = connection.cursor()
      cursor.execute('DROP DATABASE IF EXISTS webscrapedb')
      cursor.execute('CREATE DATABASE webscrapedb')
      return connection
    except Exception as error:
      print(error)

  @classmethod
  def connect(cls):
    '''Connects to the database and
    returns the connection object'''
    try:
      connection = psycopg2.connect(
        dbname=config('DB_NAME'),
        host=config('DB_HOST'),
        user=config('DB_USER'),
        password=config('DB_PASSWORD'),
        port=config('DB_PORT')
      )
      connection.autocommit = True
      return connection
    except Exception as error:
      print(error)

  @classmethod
  def setup(cls):
    '''setup function creates the needed tables in the database.
    Returns None'''
    try:
      conn = cls.connect().cursor()
      with open('src/schemas/structure.sql', 'r') as structure:
        file = structure.read()
        conn.execute(file)
    except Exception as e:
      print(e)

  @classmethod
  def seed(cls):
    '''seed function passes into the pages table, its content.
    Returns None'''
    conn = cls.connect().cursor()
    with open('src/schemas/seed.sql', 'r') as seed:
      seed_file = seed.read()
      conn.execute(seed_file)

  @classmethod
  def links(cls):
    # Returns a reference to the links interface
    conn = cls.connect()
    receive = cls.pages().select()
    link = Links(conn, receive)
    return link

  @classmethod
  def pages(cls):
    # Returns a reference to the pages interface
    conn = cls.connect()
    page = Pages(conn)
    return page