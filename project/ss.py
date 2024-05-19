import sqlite3


def delete_messages():
    conn = sqlite3.connect("users_admin.db")
    c = conn.cursor()
    c.execute('DELETE FROM news WHERE id = 4')
    conn.commit()
    conn.close()

delete_messages()