
---

## 4. **delete.md**
```markdown
### Delete a Book

To delete a specific book from the database:

```python
from .models import Book

book = Book.objects.get(title="1984")
book.delete()
print("Book deleted successfully")
