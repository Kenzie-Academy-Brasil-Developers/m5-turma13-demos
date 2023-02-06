from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()

    def __repr__(self) -> str:
        return f"<User ({self.id}) - {self.email}>"
