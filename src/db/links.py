class Links:
  def __init__(self, conn, receive):
    self.conn = conn
    self.cursor = conn.cursor()
    self.receive = receive

  def find(self, id):
    '''Selects row from the `Links` table based on the id passed in as argument
    and returns it to the console.'''
    self.cursor.execute(f'SELECT * FROM Links where id = {id}')
    content = self.cursor.fetchall()
    return content

  def insert(self, url, id):
    '''Inserts rows into the `Links` table based on the id and url passed in as argument'''
    self.cursor.execute(f'INSERT INTO Links (url, page_id) VALUES (%s, %s)', (url, id))
    self.conn.commit()

  def select(self):
    '''Selects all rows from the `Links` table
    and returns it to the console.'''
    self.cursor.execute('SELECT * FROM Links ')
    info = self.cursor.fetchall()
    return info

  def delete(self, id):
    '''Deletes row from the `Links` table based on the id passed in as argument.'''
    self.cursor.execute(f'DELETE FROM Links where page_id = {id}')
    self.conn.commit()