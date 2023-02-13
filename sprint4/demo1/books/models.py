from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.DateField()

    # Account -> Book (1:N)
    owner = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="books",
        null=True,
    )

    def __str__(self) -> str:
        return f"<Book [{self.id}] - {self.title}>"
