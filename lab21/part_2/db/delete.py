from .db_utils import delete_record


def delete_record_by_id(_id: int) -> None:
    delete_sql_statement = f'''DELETE FROM post WHERE id={_id}'''
    delete_record(sql_statement=delete_sql_statement)


if __name__ == "__main__":
    delete_record_by_id(_id=11)
