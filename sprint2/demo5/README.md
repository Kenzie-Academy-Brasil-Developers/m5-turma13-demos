# Comandos executados na shell do Django

```python
from persons.models import Person
Person
person_dict = {'name': 'Chrystian', 'cpf': '1111', 'email': 'chrystian@mail.com', 'birthdate': '1990-03-03'}
person_dict
p1 = Person(**person_dict)
p1.save()
p1.name
p1.id
p1.email
p1
from
from persons.models import Person
person_dict = {'name': 'Alexandre', 'cpf': '1112', 'email': 'ale@mail.com', 'birthdate': '1990/03/03'}
p2 = Person(**person_dict)
p2
from persons.models import Person
person_dict = {'name': 'Alexandre', 'cpf': '1112', 'email': 'ale@mail.com', 'birthdate': '1990-03-03'}
person_dict
p1 = Person(**person_dict)
p1
p1.save()
p1
person_dict = {'name': 'Chrystian', 'cpf': '1111', 'email': 'chrystian@mail.com', 'birthdate': '03-03-1993'}
p2 = Person(**person_dict)
p2
p2.save()
person_dict = {'name': 'Chrystian', 'cpf': '1111', 'email': 'chrystian@mail.com', 'birthdate': '1993-03-03'}
p2 = Person(**person_dict)
p2.save()
p2
person_dict = {'name': 'Lucira', 'cpf': '1115', 'email': 'lucira@mail.com', 'birthdate': '1993-03-17'}
Person.objects
p3 = Person.objects.create(**person_dict)
from persons.models import Person
persons = Person.objects.all()
persons
persons[0]
persons[1]
persons[3]
persons[2]
persons[0]
persons[0].name
persons[0].birthdate
persons
alexandre = Person.objects.filter(birthdate='1993-03-03')
alexandre
chrystian = Person.objects.filter(birthdate='1993-03-03')
chrystian
chrystian.name
chrystian[0].name
alexandre = Person.objects.filter(id=1)
alexandre
alexandre[0].birthdate = '1993-03-03'
alexandre[0]
alexandre[0].birthdate
alexandre[0].save()
person_dict = {'name': 'Lucira2', 'cpf': '11155', 'email': 'lucira2@mail.com', 'birthdate': '1993-03-03'}
lucira = Person.objects.create(**person_dict)
chrystian = Person.objects.filter(birthdate='1993-03-03')
chrystian
lucira = Person.objects.get(id=3)
lucira
chrystian
chrystian.first()
lucira = Person.objects.get(birthdate='1993-03-03')
lucira = Person.objects.get(birthdate='1993-12-17')
chrystian = Person.objects.filter(birthdate='1993-12-11')
chrystian
lucira = Person.objects.get(id=3)
lucira
lucira.name
lucira.name = 'Luciraaaaaaaaa'
lucira.name
lucira.save()
lucira
lucira.delete()
not_married = Person.objects.filter(married=False)
not_married
not_married.delete()
person_dict = {'name': 'Lucira2', 'cpf': '11155', 'email': 'lucira2@mail.com', 'birthdate': '1993-03-03'}
lucira = Person.objects.create(**person_dict)
queryset = Person.objects.all()
queryset
len(queryset)
queryset.count()
```
