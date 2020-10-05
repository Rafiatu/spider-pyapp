# first import all necessary dependencies.
from unittest import TestCase
from src.db import DB


class TestDatabase(TestCase):
  '''Class to test the database (db) functions'''
  def setUp(self):
    self.db = DB()

  def test_connection(self):
    '''tests that the connection function does it's work.'''
    connection = self.db.connect()
    self.assertIsNotNone(connection)

  def test_setup(self):
    '''tests that the setup function does what it was designed to do.'''
    self.db.setup()
    self.assertIsNone(self.db.setup())

  def test_seed(self):
    '''tests that the seed function does what it was designed to do.'''
    self.db.connect()
    self.db.setup()
    self.db.seed()
    self.assertIsNone(self.db.seed())

  def test_pages(self):
    '''tests that the pages function does what it was designed to do.'''
    self.db.connect()
    self.db.setup()
    self.db.seed()
    selecter = self.db.pages().select()
    self.assertIsNotNone(selecter)

  def test_links(self):
    '''tests that the links function does what it was designed to do.'''
    self.db.connect()
    self.db.setup()
    select_link = self.db.links().select()
    self.assertIsNotNone(select_link)

  def TearDown(self):
    '''the teardown function for all the tests.'''
    self.db.connect().close()