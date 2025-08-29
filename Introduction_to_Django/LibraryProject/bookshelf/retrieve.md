### Retrieve a Book

To retrieve a single book by its title, for example **"1984"**, use the `get` method:

```python
from .models import Book

book = Book.objects.get(title="1984")
print(book.title, book.author)
