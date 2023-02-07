from django.db import models


class Seasons(models.TextChoices):
    SUMMER = "Verão"
    AUTUMN = "Outono"
    WINTER = "Inverno"
    SPRING = "Primavera"
    DEFAULT = "Não especificado"


class User(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()
    favorite_season = models.CharField(
        max_length=25,
        choices=Seasons.choices,
        default=Seasons.DEFAULT,
    )
    # auto_now -> sempre vai ser gerado a partir de alterações de registros
    updated_at = models.DateTimeField(auto_now=True)
    # auto_now_add -> só vai ser gerado 1x (ao inserir o objeto no banco)
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self) -> str:
        return f"<User ({self.id}) - {self.email}>"
