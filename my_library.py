from flask import Flask, request, render_template, redirect, url_for
from forms import LibraryForm
from models import books
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = "nininini"

@app.route("/", methods=["GET", "POST"])
def library_list():
    form = LibraryForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            books.create(form.data)
            books.save_all()
        return redirect(url_for("library_list"))

    return render_template("library.html", form=form,  books=books.all(),error=error)
#


@app.route("/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
    book = books.get(book_id - 1)
    form = LibraryForm(data=book)

    if request.method == "POST":
        if form.validate_on_submit():
            books.update(book_id - 1, form.data)
        return redirect(url_for("library_list"))
    return render_template("book.html", form=form, book_id=book_id)


if __name__ == "__main__":
    app.run(debug=True)