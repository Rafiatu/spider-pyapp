class Pages:
  def __init__(self, conn):
    self.conn = conn
    self.cursor = conn.cursor()

  def fetch(self, id):
    '''Selects row from the `Pages` table based on the id passed in as argument
    and returns it to the console.'''
    self. id = id
    self.cursor.execute(f'SELECT url FROM Pages where id = {self.id}')
    url = self.cursor.fetchall()
    return url

  def select(self):
    '''Selects all rows from the `Pages` table based on the id passed in as argument
    and returns it to the console.'''
    self.cursor.execute('SELECT * from Pages')
    urls = self.cursor.fetchall()
    return urls

  def update(self, url, value):
    '''Updates rows in the `Pages` table based on the id passed in as argument,
    and boolean value passed in. Returns it to the console.'''
    self.cursor.execute(f'UPDATE Pages SET is_scraping = {value} WHERE id = {url}')
    self.conn.commit()
