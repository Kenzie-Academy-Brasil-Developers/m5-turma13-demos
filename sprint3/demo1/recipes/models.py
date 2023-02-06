from django.db import models


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)

    # user.recipe_set
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="recipes",
    )

    def __repr__(self) -> str:
        return f"<Recipe ({self.id}) - {self.name}>"
