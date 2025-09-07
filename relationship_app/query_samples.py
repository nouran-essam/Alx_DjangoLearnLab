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

# استعلام كل مؤلفين باسم John Doe
authors = Author.objects.filter(name="John Doe")
for author in authors:
    books_by_author = Book.objects.filter(author=author)
    print(f"كتب المؤلف {author.name}:")
    for book in books_by_author:
        print(book.title)

# استعلام كل الكتب في مكتبة Central Library
libraries = Library.objects.filter(name="Central Library")
for lib in libraries:
    print(f"\nالكتب في مكتبة {lib.name}:")
    for book in lib.books.all():
        print(book.title)

# استعلام أمين المكتبة
for lib in libraries:
    try:
        librarian = Librarian.objects.get(library=lib)
        print(f"\nأمين مكتبة {lib.name}:")
        print(librarian.name)
    except Librarian.DoesNotExist:
        print(f"\nلا يوجد أمين لمكتبة {lib.name}")
