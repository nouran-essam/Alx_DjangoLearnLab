### Delete a Book

To delete a specific book from the database:

```python
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print("Book deleted successfully")
