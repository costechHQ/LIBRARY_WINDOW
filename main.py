from library.books import ( 
    get_all_books, get_book, add_book, update_book, delete_book, get_borrowed_books 
) 
from library.users import authenticate, is_chief_librarian 

current_user = None 

def response(code, message): 
    return f"{code}: {message}" 

def login(): 
    """Requests user credentials with up to 3 attempts."""
    global current_user 
    for attempt in range(3): 
        username = input("Username: ").strip() 
        password = input("Password: ").strip() 
        user = authenticate(username, password) 
        if user is not None: 
            current_user = user 
            print(response(200, "Done, here you are.")) 
            return True 
        print("Invalid credentials. Try again.")
    print(response(400, "Who are you? Sign in first.")) 
    return False 

def handle_request(method, book_no=None, title=None, author=None, status=None): 
    if current_user is None: 
        return response(401, "Who are you? Sign in first.") 
    
    method = method.upper() 
    
    if method == "GET": 
        if book_no == "borrowed": 
            return response(200, get_borrowed_books()) 
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
        return response(200, "Done, here you are.") 
        
    if method == "DELETE": 
        if not is_chief_librarian(current_user): 
            return response(403, "I know who you are, and you are not allowed to do this.") 
        if book_no is None: 
            return response(400, "I cannot read this slip.") 
        deleted = delete_book(book_no) 
        if not deleted: 
            return response(404, "There is no such book") 
        return response(200, "Done, here you are.") 
        
    return response(400, "I cannot read this slip.") 

def main(): 
    if not login(): 
        return 
        
    print("\nLibrary window is open.") 
    print("Commands: GET, POST, PUT, DELETE") 
    print("Type EXIT to close.\n") 
    
    while True: 
        method = input("Method: ").strip().upper() 
        
        if method == "EXIT": 
            print("Goodbye.") 
            break 
            
        if method == "GET": 
            print("\nGET options:") 
            print("1. Get all books") 
            print("2. Get one book") 
            print("3. Get borrowed books") 
            choice = input("Choose an option: ").strip() 
            
            if choice == "1": 
                result = handle_request("GET") 
            elif choice == "2": 
                book_no_input = input("Book number: ").strip() 
                try: 
                    book_no = int(book_no_input) 
                except ValueError: 
                    print(response(400, "I cannot read this slip.")) 
                    continue 
                result = handle_request("GET", book_no=book_no) 
            elif choice == "3": 
                result = handle_request("GET", book_no="borrowed") 
            else: 
                result = response(400, "I cannot read this slip.") 
            print(result) 
            continue 

        if method in ["POST", "PUT", "DELETE"]:
            book_no = None
            if method in ["PUT", "DELETE"]:
                book_no_input = input("Book number: ").strip() 
                try: 
                    book_no = int(book_no_input) 
                except ValueError: 
                    print(response(400, "I cannot read this slip.")) 
                    continue 
            
            title = None
            author = None
            status = None
            
            if method in ["POST", "PUT"]:
                title = input("Title: ").strip() or None 
                author = input("Author: ").strip() or None 
            if method == "PUT":
                status = input("Status: ").strip() or None 
                
            result = handle_request(method, book_no, title, author, status) 
            print(result)
        else:
            print(response(400, "I cannot read this slip."))

if __name__ == "__main__": 
    main()
