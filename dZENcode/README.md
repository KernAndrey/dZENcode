# Test task for dZENcode

This is a Django-based web application for creating and managing comments. It allows users to create new comments, reply to existing comments, and view comments in a threaded manner.

## Installation

To run this project, you will need Python 3 and Django 3 installed on your machine. Once you have those dependencies installed, you can clone this repository and navigate to the project directory.

## Usage

To start the development server, run the following command in the terminal:

```
python manage.py runserver
```

To run this project use docker compose:
1. First, make sure you have Docker Compose installed on your machine. You can download it from the official Docker website: https://docs.docker.com/compose/install/
2. Clone or download the project source code from the repository.
3. Navigate to the project root directory in your terminal or command prompt.
4. Start the containers by running the following command in your terminal or command prompt:
```
docker-compose up --build
```
5. Wait for the containers to start up and initialize. This may take a few minutes.
6. Once the containers are running, you should be able to access the project at http://localhost:8000 in your web browser.


To create a new comment, click on the "New Comment" button and fill out the form. If you are clicking to "New comment" from another comment directory child comment will be added. You can also view comments capital comments on home page or child comments by clicking to comment text. 

# Author

Andrii Kern
kernandrey1@gmail.com
@andreykern - Telegram