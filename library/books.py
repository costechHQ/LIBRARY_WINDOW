from .storage import load_books, save_books

books = [
    {
        "no": 1,
        "title": "Things fall apart",
        "author": "Chinua Acheba",
        "status": "on shelf"
    },

    {
        "no": 2,
        "title": "Purple Hibiscus",
        "author": "Chimamanda Adichie",
        "status": "borrowed"
    },
    {
        "no": 3,
        "title": "The Famished Road",
        "author": "Ben Okri",
        "status": "on shelf"
    },
    {
        "no": 4,
        "title": "Sozaboy",
        "author": "Ken Saro-Wiwa",
        "status": "on shelf"
    },
    {
        "no": 5,
        "title": "Jagua Nana",
        "author": "Cyprian Ekwensi",
        "status": "borrowed"
    },
    {
        "no": 6,
        "title": "The Joys of Motherhood",
        "author": "Buchi Emecheta",
        "status": "on shelf"
    },
    {
        "no": 7,
        "title": "Arrow of God",
        "author": "Chinua Achebe",
        "status": "on shelf"
    },
    {
        "no": 8,
        "title": "Stay with me",
        "author": "Ayobami Adebayo",
        "status": "borrowed"
    },
    {
        "no": 9,
        "title": "The Fishermen",
        "author": "Chigozie Obioma",
        "status": "on shelf"
    },
    {
        "no": 10,
        "title": "Half of a yellow sun",
        "author": "Chimamanda Adichie",
        "status": "onshelf"
    }
]

saved_books = load_books()

if saved_books is not None:
    books = saved_books
else:
    save_books(books)

def get_all_books():
    """displays all the books in the list"""
    return books

def get_book(book_no):
    """this function recieves a book number"""
    for book in books:
        if book["no"] == book_no:
            return book
    return None

def add_book(title, author):
    """impementing POST"""
    new_no = max(book["no"] for book in books) + 1

    new_book = {
        "no": new_no,
        "title": title,
        "author": author,
        "status": "on shelf"
    }

    books.append(new_book)
    save_books(books)

    return new_book

def update_book(book_no, title=None, author=None, status=None):
    """this function updates book(PUT)"""

    book = get_book(book_no)

    if book is None:
        return None

    if title is not None:
        book["title"] = title

    if author is not None:
        book["author"] = author

    if status is not None:
        book["status"] = status

    save_books(books)

    return book

def delete_book(book_no):
    """This function handles DELETE"""
    book = get_book(book_no)

    if book is None:
        return False

    books.remove(book)
    save_books(books)

    return True
