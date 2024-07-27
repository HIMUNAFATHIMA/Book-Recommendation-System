# Book Recommendation System

## Description

The Book Recommendation System is a web application designed to help users discover new books based on their input of book titles or authors. Users can enter a title or author, and the system will provide a list of recommended books from a predefined list.

## Features

- **User-Friendly Interface**: A clean and intuitive interface for entering book titles or authors.
- **Real-Time Recommendations**: Receive book recommendations instantly based on user input.
- **Dynamic Display**: Recommended books are displayed with cover images and author information.
- **Responsive Design**: The application is responsive and works well on various devices, thanks to Bootstrap.
- **JSON API**: The backend API accepts JSON requests and returns recommendations in JSON format.

## Technologies Used

- **Backend**: Flask - a lightweight WSGI web application framework in Python.
- **Frontend**: HTML, CSS, JavaScript, jQuery, and Bootstrap.
- **Template Engine**: Jinja2 for rendering HTML templates.

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/your-username/book-recommendation-system.git
    cd book-recommendation-system
    ```

2. **Create a Virtual Environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```sh
    pip install Flask
    ```

4. **Run the Application**:
    ```sh
    python app.py
    ```

5. **Access the Application**:
    Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

1. Open the application in your web browser.
2. Enter a book title or author in the input fields.
3. Click the "Get Recommendations" button.
4. View the recommended books displayed on the page.

