from rest_framework.views import APIView, Response, Request, status
from .models import Person
from django.forms.models import model_to_dict
from .validators import NotKenzieEmailError, is_kenzie_domain
import ipdb


class PersonView(APIView):
    def get(self, request: Request) -> Response:
        persons = Person.objects.all()

        persons_list = []

        for person in persons:
            person_dict = model_to_dict(person)
            persons_list.append(person_dict)

        return Response(persons_list, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        try:
            is_kenzie_domain(request.data["email"])
        except NotKenzieEmailError as error:
            return Response(
                # {"error": "email must be a @kenzie.com email"},
                # {"error": error.args[0]},
                {"error": error.message},
                status.HTTP_400_BAD_REQUEST,
            )

        person = Person.objects.create(**request.data)
        person_dict = model_to_dict(person)

        return Response(person_dict, status.HTTP_201_CREATED)


class PersonDetailView(APIView):
    def get(self, request: Request, person_id: int) -> Response:
        # SELECT * FROM persons_person WHERE id = 1
        # SELECT * FROM persons_person WHERE id = '1'
        # ipdb.set_trace()
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response({"error": "person not found."}, status.HTTP_404_NOT_FOUND)

        person_dict = model_to_dict(person)

        return Response(person_dict, status.HTTP_200_OK)

    def patch(self, request: Request, person_id: int) -> Response:
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response({"error": "person not found."}, status.HTTP_404_NOT_FOUND)

        # ipdb.set_trace()

        # Forma 1
        # person.name = request.data.get("name", person.name)
        # person.cpf = request.data.get("cpf", person.cpf)
        # person.email = request.data.get("email", person.email)
        # person.birthdate = request.data.get("birthdate", person.birthdate)
        # person.married = request.data.get("married", person.married)

        # Forma 2
        # Dado a ser atualizado -> Objeto da classe Person
        # Os dados utilizados para atualizar o objeto -> request.data (dict)
        for key, value in request.data.items():
            setattr(person, key, value)

        # ipdb.set_trace()
        person.save()
        person_dict = model_to_dict(person)

        return Response(person_dict, status.HTTP_200_OK)

    def delete(self, request: Request, person_id: int) -> Response:
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response({"error": "person not found."}, status.HTTP_404_NOT_FOUND)

        person.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
