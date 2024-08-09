Welcome to the Library - Api!
=============================

Summary
--------

*The project consists of developing a RESTful API for managing a book library. The API must allow the management of users, books and user authentication to access certain functionalities.* 


Modules
-------

-   [app.py](https://github.com/joacasallas/library_api/blob/main/app.py)
-   [config.py](https://github.com/joacasallas/library_api/blob/main/config.py)
-   [models.py](https://github.com/joacasallas/library_api/blob/main/models.py)
-   [routes.py](https://github.com/joacasallas/library_api/blob/main/routes.py)
-   [services.py](https://github.com/joacasallas/library_api/blob/main/services.py)
-   [tests/test_app.py](https://github.com/joacasallas/library_api/blob/main/tests/test_app.py)


### General

- Users:  
    - Register a new user.  
    - Authenticate a user with JWT (JSON Web Tokens).  
    - Get the profile from the authenticate user.  


- Books:
    - Create a new book.  
    - Get a list with all the books stored.  
    - Get the information from a book_id.  
    - Update the information with an specific id.  
    - Delete a book  

### Execution  
Running: `$ python3 app.py`

Tests: `python3 -m unittest discover tests`


## Autor:  joacasallas :information_desk_person:  
contact:  joacasallas@gmail.com