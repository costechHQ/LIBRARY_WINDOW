from library.books import (
    get_all_books,
    get_book,
    add_book,
    update_book,
    delete_book
)

from library.users import authenticate, is_chief_librarian

current_user = None

def response(code, message):
    return f"{code}: {message}"

def login():
    """requests for user's credentials"""
    global current_user

    username = input("Username: ")
    password = input("Password: ")

    user = authenticate(username, password)

    if user is None:
        print(response(401, "Who are you? Sign in first."))
        return False

    current_user = user
    print(response(200, "Done, here you are."))
    return True

def handle_request(method, book_no=None, title=None, author=None, status=None):
    if current_user is None:
        return response(401, "Who are you? Sign in first.")

    method = method.upper()

    if method == "GET":
        if book_no is None:
            return response(200, get_all_books())

        book = get_book(book_no)

        if book is None:
            return response(404, "There is no such book")

        return response(200, book)

    if method == "POST":
        if not title or not author:
            return response(400, "I cannot read this slip.")

        book = add_book(title, author)

        return response(201, "Create - a new thing now exists")

    if method == "PUT":
        if book_no is None:
            return response(400, "I cannot read this slip.")

        book = update_book(book_no, title, author, status)

        if book is None:
            return response(404, "There is no such book")

        return response (200, "Done, here you are.")

    if method == "DELETE":
        if not is_chief_librarian(current_user):
            return response(
                403,
                "I know who you are, and you are not allowed to do this."
            )

        if book_no is None:
            return response(400, "I cannot read this slip.")

        deleted = delete_book(book_no)

        if not deleted:
            return response(404, "There is no such book")

        return response(200, "Done, here you are.")

    return response(400, "I cannot read this slip")

def main():
    if not login():
        return

    print("\nLibrary window is open.")
    print("Commands: GET, POST, PUT, DELETE")
    print("Type EXIT to close.\n")

    while True:
        method = input("Method: ").strip()

        if method.upper() == "EXIT":
            print("Goodbye.")
            break

        book_no_input = input("Book number (press Enter if not needed): ").strip()

        if book_no_input:
            try:
                book_no = int(book_no_input)
            except ValueError:
                print(response(400, "I cannot read this slip"))
                continue
        else:
            book_no = None

        title = input("Title (press Enter if not needed): ").strip()
        author = input("Author (press Enter if not needed): ").strip()
        status = input("status (press Enter if not needed): ").strip()

        result = handle_request(
            method,
            book_no,
            title or None,
            author or None,
            status or None
        )

        print(result)

if __name__ == "__main__":
    main()