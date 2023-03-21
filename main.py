from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
# initialize the app with the extension
db.init_app(app)

all_books = []

#Creating new table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

with app.app_context():
    db.create_all()


def add_to_books(title_, author_, rating_):
    with app.app_context():
        new_book = Book(title=title_, author=author_, rating=rating_)
        db.session.add(new_book)
        db.session.commit()


@app.route('/')
def home():
    global all_books
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    global all_books
    if request.method == "POST":
        get_title = request.form["name"]
        get_author = request.form["author"]
        get_rating = request.form["rating"]

        add_to_books(get_title, get_author, get_rating)

        all_books = db.session.query(Book).all()
        return redirect(url_for("home"))
    return render_template('add.html')

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == "POST":
        book_id = request.form['id']
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit.html", book=book_selected)

@app.route("/delete", methods=['GET', 'POST'])
def delete_book():
    book_id = request.args.get('id')
    query_to_delete = Book.query.get(book_id)
    db.session.delete(query_to_delete)
    db.session.commit()


    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)

