from bookshelf.models import Book

# Get the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion
Book.objects.all()
(1, {'bookshelf.Book': 1})
<QuerySet []>
