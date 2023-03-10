from app.repositories.pet_repos import InMemoryPetRepository
from flask.testing import FlaskClient


def test_can_list_pets(client: FlaskClient):
    repository = InMemoryPetRepository()

    animal1 = {"name": "Fluffy", "age": 2, "species": "cat"}
    animal2 = {"name": "Penelope", "age": 4, "species": "dog"}

    repository.add(animal1)
    repository.add(animal2)

    response = client.get("/pets")

    assert response.status_code == 200
    assert response.json == [animal1, animal2]
