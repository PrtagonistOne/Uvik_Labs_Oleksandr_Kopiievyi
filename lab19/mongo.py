import pprint

from pymongo import MongoClient
from user_data import user_1, user_2


def get_database():
    client = MongoClient()
    return client, client.myblogdb


if __name__ == "__main__":
    _client, dbname = get_database()
    collection_name = dbname['user']

    results_insert = collection_name.insert_many([user_1, user_2])
    print(f"Multiple users: {results_insert.inserted_ids}")

    for doc in collection_name.find():
        pprint.pprint(doc)

    filter_results = collection_name.find({'is_active': False})
    print(f'The amount of inactive users is {len(list(filter_results))}')

    collection_name.update_many({'id': 2},  {"$set": {"family_status": "married"}})
    for doc in collection_name.find({'id': 2}):
        pprint.pprint(doc)

    delete_results = collection_name.delete_many({"family_status": 'married'})
    print(delete_results.deleted_count, " documents deleted.")

    _client.close()
