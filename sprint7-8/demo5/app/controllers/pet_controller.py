from http import HTTPStatus

from flask import request

from app.repositories.pet_repos import InMemoryPetRepository, MongoPetRepository

repository = InMemoryPetRepository()
# repository = MongoPetRepository(database="t13-pet", collection="pets")


def list_pets():
    pets = repository.list()
    return pets


def create_pet():
    pet_data = request.get_json()
    pet = repository.add(pet_data)

    return pet, HTTPStatus.CREATED


def retrieve_pet(pet_id: str):
    # try:
    #     pet = repository.retrieve(pet_id)
    # except NotFoundError as error:
    #     return {"detail": error.message}, error.status_code

    pet = repository.retrieve(pet_id)

    return pet


def update_pet(pet_id: str):
    pet_data = request.get_json()
    # try:
    #     pet = repository.update(pet_id, pet_data)
    # except NotFoundError as error:
    #     return {"detail": error.message}, error.status_code
    pet = repository.update(pet_id, pet_data)
    return pet


def destroy_pet(pet_id: str):
    # try:
    #     pet = repository.delete(pet_id)
    # except NotFoundError as error:
    #     return {"detail": error.message}, error.status_code
    pet = repository.delete(pet_id)
    return pet
