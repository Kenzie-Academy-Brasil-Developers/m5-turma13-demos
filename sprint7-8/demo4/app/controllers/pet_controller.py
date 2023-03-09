from flask import request
from http import HTTPStatus
from app.repositories.pet_repos.in_memory_repo import InMemoryPetRepository
from app.repositories.pet_repos.mongo_repo import MongoPetRepository


# repository = InMemoryPetRepository()
repository = MongoPetRepository(database="t13-pet", collection="pets")


def list_pets():
    pets = repository.list()
    return pets


def create_pet():
    pet_data = request.get_json()
    # pet_data["_id"] = increment_id()

    # pets.append(pet_data)

    # return pet_data, 201
    pet = repository.add(pet_data)

    return pet, HTTPStatus.CREATED


def retrieve_pet(pet_id: str):
    # for pet in pets:
    #     if str(pet["_id"]) == pet_id:
    #         return pet

    pet = repository.retrieve(pet_id)

    if not pet:
        return {"detail": "pet not found."}, HTTPStatus.NOT_FOUND

    return pet


def update_pet(pet_id: str):
    pet_data = request.get_json()

    # for pet in pets:
    #     if str(pet["_id"]) == pet_id:
    #         pet.update(pet_data)
    #         return pet
    pet = repository.update(pet_id, pet_data)

    if not pet:
        return {"detail": "pet not found."}, HTTPStatus.NOT_FOUND

    return pet


def destroy_pet(pet_id: str):
    # for pet in pets:
    #     if str(pet["_id"]) == pet_id:
    #         pets.remove(pet)
    #         return pet

    pet = repository.delete(pet_id)

    if not pet:
        return {"detail": "pet not found."}, HTTPStatus.NOT_FOUND

    return pet
