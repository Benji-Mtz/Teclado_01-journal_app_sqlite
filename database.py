import sqlite3

entries = []

connection = sqlite3.connect("data.db")
#  sqlite.Row to get named access to row fields ['date'] en lugar de [1]
connection.row_factory = sqlite3.Row

def create_table():
    # with connection do automatically connection.commit()
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")


def add_entry(entry_content, entry_date):
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES (?,?);", (entry_content, entry_date)
        )


def get_entries():
    #cursor = connection.cursor()
    #cursor.execute("SELECT * FROM entries;")
    
    cursor = connection.execute("SELECT * FROM entries;")
    #cursor.fetchone() # 1
    #cursor.fetchone() # 2
    return cursor
    
    
    