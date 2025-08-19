class Book:
    """Class to represent a book in the library."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  # False = Available, True = Borrowed

class Node:
    """Node of a linked list, holding a Book and pointer to the next node."""
    def __init__(self, book):
        self.book = book
        self.next = None

class Library:
    """Linked-list based library inventory."""
    def __init__(self):
        self.head = None  # Start with an empty list

    def add_book(self, title, author):
        """Add a new book to the end of the linked list."""
        new_book = Book(title, author)
        new_node = Node(new_book)
        if not self.head:
            self.head = new_node
        else:
            # Traverse to the end and append the new node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_book(self, title):
        """Find a book node by title. Return the node or None if not found."""
        current = self.head
        while current:
            if current.book.title == title:
                return current
            current = current.next
        return None

    def search_books(self, keyword):
        """
        Search for books whose title or author contains the keyword (case-insensitive).
        Returns a list of matching Book objects.
        """
        current = self.head
        results = []
        while current:
            if (keyword.lower() in current.book.title.lower() or
                keyword.lower() in current.book.author.lower()):
                results.append(current.book)
            current = current.next
        return results

    def list_books(self):
        """Return a list of all books as (title, author, borrowed_status) tuples."""
        books = []
        current = self.head
        while current:
            books.append((current.book.title, current.book.author, current.book.is_borrowed))
            current = current.next
        return books

class Stack:
    """Simple stack implementation for undo functionality."""
    def __init__(self):
        self.items = []

    def push(self, item):
        """Push an action tuple onto the stack."""
        self.items.append(item)

    def pop(self):
        """Pop the last action from the stack, or None if empty."""
        if self.items:
            return self.items.pop()
        return None

    def is_empty(self):
        """Check if stack is empty."""
        return len(self.items) == 0

def main():
    library = Library()
    undo_stack = Stack()

    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Undo Last Action")
        print("5. Search Book")
        print("6. List All Books")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
            print(f"Book '{title}' by {author} added to inventory.")

        elif choice == '2':
            title = input("Enter title to borrow: ")
            node = library.find_book(title)
            if node is None:
                print(f"Book '{title}' not found in inventory.")
            elif node.book.is_borrowed:
                print(f"Book '{title}' is already borrowed.")
            else:
                node.book.is_borrowed = True
                undo_stack.push(("borrow", node))
                print(f"You have borrowed '{title}'.")

        elif choice == '3':
            title = input("Enter title to return: ")
            node = library.find_book(title)
            if node is None:
                print(f"Book '{title}' not found in inventory.")
            elif not node.book.is_borrowed:
                print(f"Book '{title}' was not borrowed.")
            else:
                node.book.is_borrowed = False
                undo_stack.push(("return", node))
                print(f"You have returned '{title}'.")

        elif choice == '4':
            # Undo the most recent borrow/return action
            action = undo_stack.pop()
            if action is None:
                print("No actions to undo.")
            else:
                act_type, node = action
                if act_type == "borrow":
                    node.book.is_borrowed = False
                    print(f"Undo: '{node.book.title}' is now available again.")
                elif act_type == "return":
                    node.book.is_borrowed = True
                    print(f"Undo: '{node.book.title}' is marked as borrowed again.")

        elif choice == '5':
            keyword = input("Enter title or author to search: ")
            results = library.search_books(keyword)
            if results:
                print("Search results:")
                for book in results:
                    status = "Borrowed" if book.is_borrowed else "Available"
                    print(f"- '{book.title}' by {book.author} [{status}]")
            else:
                print("No matching books found.")

        elif choice == '6':
            books = library.list_books()
            if books:
                print("\nAll books in inventory:")
                for title, author, is_borrowed in books:
                    status = "Borrowed" if is_borrowed else "Available"
                    print(f"- '{title}' by {author} [{status}]")
            else:
                print("No books in inventory.")

        elif choice == '7':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
