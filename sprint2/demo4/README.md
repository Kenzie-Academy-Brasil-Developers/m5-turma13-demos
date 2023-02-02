# Comandos executados na shell do Django

```python
from persons.models import Person

person_dict = {'name': 'Chrystian', 'cpf': '1111', 'email': 'chrystian@mail.com', 'birthdate': '1990-03-03'}
p1 = Person(**person_dict)
p1.save()
p1.name
p1.id
p1.email
p1
```
