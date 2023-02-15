from django.db import models






class Book(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.DateField()

    # Account -> Book (1:N)
    owner = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="books",
    )

    markers = models.ManyToManyField(
        "accounts.Account",
        through="books.BookMark",
        related_name="marked_books",
    )

    def __repr__(self) -> str:
        return f"<Book [{self.id}] - {self.title}>"


class BookMark(models.Model):
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="book_marks",
    )

    marker = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="user_book_marks",
    )

    chapter = models.IntegerField()
    note = models.TextField()

    def __repr__(self) -> str:
        return f"<BookMark [{self.id}] - {self.note}>"
