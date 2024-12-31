
function getRecommendations() {
    const genreInput = document.getElementById('genreInput').value;
    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ genre: genreInput })
    })
    .then(response => response.json())
    .then(data => displayBooks(data))
    .catch(error => console.error('Error:', error));
}

function displayBooks(bookArray) {
    const bookList = document.getElementById('bookList');
    bookList.innerHTML = '';
    if (bookArray.length === 0) {
        bookList.innerHTML = '<p>No books found for the given genre.</p>';
    } else {
        bookArray.forEach(book => {
            const bookItem = document.createElement('div');
            bookItem.className = 'book-item';
            bookItem.innerHTML = `
                <img src="${book.image}" alt="${book.title}">
                <h3>${book.title}</h3>
                <p>by ${book.author}</p>
            `;
            bookList.appendChild(bookItem);
        });
    }
}
