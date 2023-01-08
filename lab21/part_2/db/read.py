from .write import get_connection, save_and_close_connection


def get_all_post_data() -> list:
    db = get_connection()
    post_values = list(db.values())
    save_and_close_connection(db)
    return post_values


def get_one_post_datum(id: int) -> dict:
    db = get_connection()
    try:
        post_value = db[id]
    except KeyError:
        post_value = {"error_message": f'ID #{id} not found'}

    save_and_close_connection(db)
    return post_value


def get_post_data_by_likes(likes: int) -> list:
    db = get_connection()

    post_value = []
    for id, post_datum in db.items():
        post_value.extend(
            db[id]
            for key, val in post_datum.items()
            if key == 'likes' and val == likes
        )
    return post_value


if __name__ == "__main__":
    print(get_all_post_data())
    print(get_one_post_datum(1))
    print(get_post_data_by_likes(10))
