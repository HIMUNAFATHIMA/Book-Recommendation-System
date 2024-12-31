from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data: List of books
books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic", "image": "images/11.webp"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Classic", "image": "images/to.jpg"},
    {"title": "1984", "author": "George Orwell", "genre": "Dystopian", "image": "images/19.jpg"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance", "image": "images/pri.jpg"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Classic", "image": "images/ca.jpg"},
    {"title": "The Hunger Games", "author": "Suzanne Collins", "genre": "Dystopian", "image": "images/hun.jpg"},
    {"title": "Twilight", "author": "Stephenie Meyer", "genre": "Romance", "image": "images/t.webp"},
    {"title": "Ponniyin Selvan", "author": "Kalki Krishnamurthy", "genre": "Historical Fiction", "image": "images/pon.jpg"},
    {"title": "Sivagamiyin Sabatham", "author": "Kalki Krishnamurthy", "genre": "Historical Fiction", "image": "images/siva.webp"},
    {"title": "Parthiban Kanavu", "author": "Kalki Krishnamurthy", "genre": "Historical Fiction", "image": "images/kalki.webp"},
    {"title": "Karna", "author": "R. K. Narayan", "genre": "Mythology", "image": "images/Rk.webp"},
    {"title": "Kamba Ramayanam", "author": "Kambar", "genre": "Epic Poetry", "image": "images/rama.webp"},
    {"title": "Alai Osai", "author": "Kalki Krishnamurthy", "genre": "Fiction", "image": "images/alai.webp"},
    {"title": "Sila Nerangalil Sila Manithargal", "author": "Jayakanthan", "genre": "Fiction", "image": "images/sila.webp"},
    {"title": "Pavithra", "author": "Balakumaran", "genre": "Fiction", "image": "images/pavi.webp"},
    {"title": "Vishnupuram", "author": "Jeyamohan", "genre": "Fiction", "image": "images/vis.webp"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    title = data.get('title', '').lower()
    author = data.get('author', '').lower()
    
    if author:
        recommended_books = [book for book in books if author in book['author'].lower()]
    elif title:
        recommended_books = [book for book in books if title in book['genre'].lower()]
    else:
        recommended_books = []
        
    return jsonify(recommended_books)

if __name__ == '__main__':
    app.run(debug=True)
