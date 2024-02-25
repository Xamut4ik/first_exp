import sqlite3
def delete_messages():
    conn = sqlite3.connect("news.db")
    c = conn.cursor()
    c.execute('DELETE FROM article WHERE id = 1')
    conn.commit()
    conn.close()

delete_messages()