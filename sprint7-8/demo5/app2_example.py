from http import HTTPStatus

from flask import Flask, request

# MINHA_CONST = 10

app = Flask(__name__)

pets = []
COUNTER = 0


def increment_id():
    # COUNTER = 0
    global COUNTER
    COUNTER += 1
    # COUNTER = COUNTER + 1
    return COUNTER


@app.get("/pets")
def list_pets():
    return pets


@app.post("/pets")
def create_pet():
    pet_data = request.get_json()
    pet_data["_id"] = increment_id()

    pets.append(pet_data)

    # return pet_data, 201
    return pet_data, HTTPStatus.CREATED


@app.get("/pets/<pet_id>")
def retrieve_pet(pet_id: str):
    for pet in pets:
        if str(pet["_id"]) == pet_id:
            return pet

    return {"detail": "pet not found."}, HTTPStatus.NOT_FOUND


@app.patch("/pets/<pet_id>")
def update_pet(pet_id: str):
    pet_data = request.get_json()

    for pet in pets:
        if str(pet["_id"]) == pet_id:
            pet.update(pet_data)
            return pet

    return {"detail": "pet not found."}, HTTPStatus.NOT_FOUND


@app.delete("/pets/<pet_id>")
def destroy_pet(pet_id: str):
    for pet in pets:
        if str(pet["_id"]) == pet_id:
            pets.remove(pet)
            return pet

    return {"detail": "pet not found."}, HTTPStatus.NOT_FOUND
