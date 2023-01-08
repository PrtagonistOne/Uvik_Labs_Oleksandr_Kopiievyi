import sqlite3


def delete_record_by_id(id: int) -> None:
    conn = sqlite3.connect('posts.sqlite')

    sql = 'DELETE FROM unnamed WHERE key=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    conn.close()
