# DESIGN PATTERN - Repository
class InMemoryRepository:
    items = []
    counter = 0

    @classmethod
    def __increment_id(cls):
        """
        public, private, protected
        """
        cls.counter += 1
        return cls.counter

    def add(self, item: dict) -> dict:
        item["_id"] = self.__increment_id()
        self.items.append(item)

        return item

    def list(self) -> list:
        return self.items

    def retrieve(self, item_id: str) -> dict | None:
        for item in self.items:
            if str(item["_id"]) == item_id:
                return item

    def update(self, item_id: str, data_to_update: dict) -> dict | None:
        found_item = self.retrieve(item_id)

        if found_item:
            found_item.update(data_to_update)

            return found_item

    def delete(self, item_id: str) -> dict | None:
        found_item = self.retrieve(item_id)

        if found_item:
            self.items.remove(found_item)
            return found_item
