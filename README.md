Features

-> Add Books: Prompt the user for a title and author. The program creates a new Book and appends it to the end of the linked list.

-> Borrow Books: Prompt for a title. If found and currently available, the book’s status is set to borrowed and the action is pushed onto the undo stack.

-> Return Books: Prompt for a title. If found and currently borrowed, the book’s status is set to available and the action is pushed onto the stack.

-> Undo Last Action: Pops the most recent action from the stack and reverses it. If the last action was a borrow, the book becomes available again; if it was a return, the book is marked borrowed. .

-> Search Books: Prompt for a keyword. The program traverses the linked list and prints any books whose title or author contains the keyword (case-insensitive).

-> List All Books: Displays every book in the inventory with its status (“Available” or “Borrowed”).

-> Menu Interface: A simple console menu lets the user choose actions by entering 1–7. The program loops until the user chooses to exit. All interactions are done via console input.

overview of this project

Book Class

Represents a single book with:

title (string)

author (string)

is_borrowed (boolean → True if borrowed, False if available)

Node Class

A node in the Linked List.

Each node stores a Book object and a pointer (next) to the next node.

Library Class (Linked List Inventory)

Manages all books in the form of a linked list.

Functions:

add_book(title, author) → adds a book to the inventory.

find_book(title) → searches for a book by title.

search_books(keyword) → finds books by title/author keyword.

list_books() → lists all books with their status.

Stack Class (Undo History)

Stores borrow/return actions so the last action can be undone.

Functions:

push(item) → saves an action.

pop() → retrieves the most recent action.

is_empty() → checks if stack is empty.

Main Program (Menu System)

Runs an infinite loop until user exits.

Options provided:

Add Book

Borrow Book

Return Book

Undo Last Action

Search Book

List All Books

Exit
