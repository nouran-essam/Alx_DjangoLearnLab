### Retrieve a Book

To retrieve a single book by its ID, use the `get` method:

```python
from .models import Book

book = Book.objects.get(id=1)
print(book.title, book.author)
