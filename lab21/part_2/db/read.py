from .db_utils import get_read_connection_data


def get_all_post_data() -> list:
    # sourcery skip: inline-immediately-returned-variable
    get_all_sql_statement = '''SELECT * FROM post'''
    return get_read_connection_data(sql_statement=get_all_sql_statement)


def get_post_by_id(_id: int) -> dict:
    # sourcery skip: inline-immediately-returned-variable
    get_all_sql_statement = f'''SELECT * FROM post WHERE id={_id}'''
    try:
        post_record = get_read_connection_data(sql_statement=get_all_sql_statement)[0]
    except IndexError:
        post_record = {'Error message': 'Record not found'}
    return post_record


def get_post_by_data(post_data: dict) -> list:
    dynamic_where_sql_str = ' AND '.join(f"{key}='{value}'" for key, value in post_data.items())
    get_post_data_sql = f'''SELECT * FROM post WHERE {dynamic_where_sql_str}'''

    return get_read_connection_data(sql_statement=get_post_data_sql)


if __name__ == "__main__":
    print(get_all_post_data())
    print(get_post_by_id(_id=1))
    print(get_post_by_data({'likes': 10, 'title': 'some title'}))
