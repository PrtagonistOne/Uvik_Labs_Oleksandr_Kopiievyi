from sqlitedict import SqliteDict


def get_connection():
    return SqliteDict("posts.sqlite")


def save_and_close_connection(db) -> None:
    db.commit()
    db.close()


def save_to_db(post_data: dict) -> None:
    db = get_connection()
    id_counter = len(db) + 1

    db[id_counter] = post_data

    save_and_close_connection(db)


def update_record(post_data: dict, id: int) -> None:
    db = get_connection()

    if db.get(id) is not None:
        db[id] = post_data

    save_and_close_connection(db)


def partial_update(post_data: dict, id: int) -> None:
    db = get_connection()

    if db.get(id) is not None:
        patch_data = db[id].copy()
        patch_data.update(post_data)
        db[id] = patch_data

    save_and_close_connection(db)


if __name__ == "__main__":
    db1 = SqliteDict("posts.sqlite")

    db1[1] = {
        'id': 1,
        'title': 'Some text',
        'body': 'Body',
        'likes': 10
    }

    db1[2] = {
        'id': 2,
        'title': 'Some text 2',
        'body': 'Body 2',
        'likes': 10
    }

    db1[3] = {
        'id': 3,
        'title': 'Some text 3',
        'body': 'Body 3',
        'likes': 12
    }

    db1.commit()
    db1.close()
