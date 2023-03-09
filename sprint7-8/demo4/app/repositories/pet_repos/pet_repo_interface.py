from abc import ABC, abstractmethod


class PetRepositoryInterface(ABC):
    @abstractmethod
    def add(self, item: dict) -> dict:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list:
        raise NotImplementedError

    @abstractmethod
    def retrieve(self, item_id: str) -> dict | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, item_id: str, data_to_update: dict) -> dict | None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, item_id: str) -> dict | None:
        raise NotImplementedError
