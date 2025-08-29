### Update a Book

To update the details of an existing book, first retrieve it and then modify its fields:

```python
from .models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.author = "Eric Arthur Blair"
book.save()
print(book.title, book.author)
