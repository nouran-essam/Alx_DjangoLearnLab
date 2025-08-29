from bookshelf.models import Book

# Get the book instance
book = Book.objects.get(title="1984")

# Update title and save
book.title = "Nineteen Eighty-Four"
book.save()
book
<Book: Nineteen Eighty-Four by George Orwell (1949)>
