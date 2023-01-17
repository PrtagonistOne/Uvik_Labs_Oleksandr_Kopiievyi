import sqlite3


def get_connection(db_file):
    try:
        return sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return None


def apply_sql(conn, sql_statement: str, row_values=None):
    c = conn.cursor()

    try:
        if row_values is not None:
            c.execute(sql_statement, row_values)
            conn.commit()
        else:
            c.execute(sql_statement)
            return c
    except Exception as e:
        print(e)

    c.close()
    return c.lastrowid


def get_read_connection_data(sql_statement: str) -> dict:
    conn = get_connection('posts.sqlite')

    conn.row_factory = sqlite3.Row
    rows = apply_sql(conn=conn, sql_statement=sql_statement).fetchall()
    return [dict(row) for row in rows]


def delete_record(sql_statement: str) -> None:
    conn = get_connection('posts.sqlite')

    with conn:
        apply_sql(conn=conn, sql_statement=sql_statement)


def perform_update(sql_statement: str, row_data: tuple) -> None:
    conn = get_connection('posts.sqlite')

    with conn:
        apply_sql(conn=conn, sql_statement=sql_statement, row_values=row_data)


def perform_create(sql_statement: str, post_data: dict) -> int:
    conn = get_connection('posts.sqlite')
    title = post_data['title']
    body = post_data['body']
    likes = post_data['likes']

    with conn:
        created_id = apply_sql(conn=conn, sql_statement=sql_statement, row_values=(title, body, likes))
    return created_id


if __name__ == "__main__":
    connection = get_connection("posts.sqlite")

    sql_create_post_table = """ CREATE TABLE IF NOT EXISTS post (
                                            id integer PRIMARY KEY,
                                            title text,
                                            body text NOT NULL,
                                            likes int
                                        ); """

    insert_post_sql = ''' INSERT INTO post(title,body,likes)
                  VALUES(?,?,?) '''

    if connection is not None:
        apply_sql(conn=connection, sql_statement=sql_create_post_table)
        apply_sql(conn=connection, sql_statement=insert_post_sql, row_values=('some title', 'some body', '10'))
    else:
        print('No connection was made!')