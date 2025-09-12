from flask import Flask, request, jsonify
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "library_db"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASS", "")
    )
    return conn


# --- ROUTES ---

# Read all books
@app.route('/books', methods=['GET'])
def get_books():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Books;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)


# Read one book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Books WHERE BookID = %s;', (book_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        return jsonify(row)
    return jsonify({"error": "Book not found"}), 404


# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    title = data.get('title')
    isbn = data.get('isbn')
    genre = data.get('genre')
    year = data.get('yearpublished')
    authorid = data.get('authorid')

    if not title or not isbn:
        return jsonify({"error": "Title and ISBN are required"}), 400

    conn = get_db_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            '''
            INSERT INTO Books (Title, ISBN, Genre, YearPublished, AuthorID)
            VALUES (%s, %s, %s, %s, %s) RETURNING BookID;
            ''',
            (title, isbn, genre, year, authorid)
        )
        row = cur.fetchone()
        new_id = row[0] if row else None
        conn.commit()
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        cur.close()
        conn.close()

    if new_id:
        return jsonify({"BookID": new_id, "message": "Book created successfully"}), 201
    else:
        return jsonify({"error": "Insert failed"}), 400



# Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    title = data.get('title')
    genre = data.get('genre')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE Books SET Title = %s, Genre = %s WHERE BookID = %s;',
                (title, genre, book_id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Book updated successfully"})


# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM Books WHERE BookID = %s;', (book_id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Book deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)
