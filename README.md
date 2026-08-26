# Mr Bello's Library Window

A Python library management system built with modules, authentication, CRUD operations, and persistent storage.

## Features

- User authentication
- Three failed login attempts lock a user
- Member and Chief Librarian roles
- Get all books
- Get a single book
- Get borrowed books
- Add books
- Update books
- Delete books — Chief Librarian only
- Persistent JSON storage
- Response codes: `200`, `201`, `400`, `401`, `403`, `404`
- Request/audit logging

## Project Structure

```text
library_window/
main.py
 library/
        __init__.py
        books.py
        users.py
        storage.py
        request_log.py

## Run
uv run main.py

## Users
Username	Password	Role

## Response Codes
200 — Successful request
201 — Resource created
400 — Invalid request
401 — Authentication required
403 — Permission denied
404 — Book not found


## Purpose

This project demonstrates Python fundamentals including:

Functions

- Modules and packages
- Lists and dictionaries
- Loops and conditionals
- File handling
- JSON persistence
- Authentication
- Authorization
- CRUD operations
- Audit logging