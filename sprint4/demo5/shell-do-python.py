from books.models import Book

books = Book.objects.all()
books
books.delete()
from accounts.models import Account

lucira = Account.objects.get(username="lucira")
lucira
lucira.books
lucira.books.all()
len(lucira.books.all())
lucira.books.count()


from books.models import Book, BookMark
from accounts.models import Account

lucira = Account.objects.get(username="lucira")
lucira

gustavo = Account.objects.get(username="gustavo")
gustavo

books = Book.objects.all()
books

lotr, dom_quixote, silmarillion, moby_dick = books
lotr
dom_quixote
silmarillion
moby_dick

bm1 = BookMark.objects.create(
    book=lotr,
    marker=lucira,
    chapter=1,
    note="Muito legal!!!",
)
validated_data = {'chapter': 14, 'note': 'Um capitulo mediano :|', 'book': lotr, 'marker': lucira,}
bm1 = BookMark.objects.create(**validated_data)
bm1

lucira
lucira.marked_books
lucira.marked_books.all()

lotr
lotr.markers
lotr.markers.all()

bm1.book
bm1.marker
lotr.book_marks
lotr.book_marks.all()

lucira.user_book_marks
lucira.user_book_marks.all()

bm2 = BookMark.objects.create(
    marker=gustavo, book=lotr, note="Meio chato esse capitulo", chapter=13
)
bm2.book
bm2.marker

gustavo
gustavo.user_book_marks.all()

lotr
lotr.book_marks.all()

gustavo.marked_books.all()
lotr.markers.all()

bm3 = BookMark.objects.create(
    marker=gustavo, book=moby_dick, note="Muito boooooom", chapter=15
)

gustavo.marked_books.all()
moby_dick.markers.all()

bm3.book
bm3.marker
gustavo.user_book_marks.all()
moby_dick.book_marks.all()
