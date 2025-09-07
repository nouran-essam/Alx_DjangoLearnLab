import os
import sys
import django

# نضيف مسار المشروع (المكان اللي فيه manage.py)
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

# نحدد إعدادات مشروع Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

# إعداد Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
try:
    author = Author.objects.get(name="John Doe")
    books_by_author = Book.objects.filter(author=author)
    print("Books by John Doe:", [book.title for book in books_by_author])
except Author.DoesNotExist:
    print("Author 'John Doe' not found. Please add data first.")

# 2. List all books in a library
try:
    library = Library.objects.get(name="Central Library")
    books_in_library = library.books.all()
    print("Books in Central Library:", [book.title for book in books_in_library])
except Library.DoesNotExist:
    print("Library 'Central Library' not found. Please add data first.")

# 3. Retrieve the librarian for a library
try:
    library = Library.objects.get(name="Central Library")
    librarian = library.librarian
    print("Librarian of Central Library:", librarian.name)
except (Library.DoesNotExist, Librarian.DoesNotExist):
    print("Librarian or Library not found. Please add data first.")
