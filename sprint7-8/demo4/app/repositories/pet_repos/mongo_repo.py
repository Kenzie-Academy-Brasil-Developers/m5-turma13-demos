from .pet_repo_interface import PetRepositoryInterface
import pymongo
import ipdb
from bson.objectid import ObjectId


class MongoPetRepository(PetRepositoryInterface):
    def __init__(
        self,
        host="localhost",
        port=27017,
        database="default_db",
        collection="default_collection",
    ) -> None:
        self.client = pymongo.MongoClient(host=host, port=port)
        # use t13-demo
        self.db = self.client[database]
        self.collection = self.db[collection]

    def __serialize(self, item: dict) -> dict:
        item.update({"_id": str(item["_id"])})

        return item

    def add(self, item: dict) -> dict:
        # ipdb.set_trace()

        inserted_id = self.collection.insert_one(item).inserted_id

        return self.retrieve(inserted_id)

    def list(self) -> list:
        items = self.collection.find()

        if items:
            return [self.__serialize(item) for item in items]

        return items

    def retrieve(self, item_id: str) -> dict | None:
        found_item = self.collection.find_one({"_id": ObjectId(item_id)})

        return self.__serialize(found_item)

    # TODO:
    # Terminar update e delete
    def update(self, item_id: str, data_to_update: dict) -> dict | None:
        return super().update(item_id, data_to_update)

    def delete(self, item_id: str) -> dict | None:
        return super().delete(item_id)
