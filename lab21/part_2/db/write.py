from .db_utils import perform_update, perform_create
from .read import get_post_by_id


def dynamic_update(post_data: dict, _id: int) -> dict:
    dynamic_set_str = ','.join(f"{key} = ?" for key in post_data)
    update_sql_statement = f''' UPDATE post SET {dynamic_set_str} WHERE id = {_id}'''

    perform_update(sql_statement=update_sql_statement, row_data=(tuple(post_data.values())))
    return get_post_by_id(_id=_id)


def create_record(post_data: dict) -> dict:
    insert_post_sql = '''INSERT INTO post(title,body,likes) VALUES(?,?,?)'''

    created_id = perform_create(sql_statement=insert_post_sql, post_data=post_data)
    return get_post_by_id(_id=created_id)


if __name__ == "__main__":
    print(dynamic_update({'body': 'partially updated body', 'likes': 1}, 1))
    print(create_record({'title': 'new title', 'body': 'new body', 'likes': 12}))
