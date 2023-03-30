from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

book_list = [
    {"title": "Test", "author": "Author", "pages": "Pages", "read": "fiction", "details": "own", "how": "friend"}
]


@app.route("/index", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", pageTitle="Book Library", books=book_list
    )


@app.route("/add", methods=["POST"])
def add():
    print("inside add function")
    if request.method == "POST":

        form = request.form

        title = form["title"]
        author = form["author"]
        pages = form["pages"]
        read = form["read"]
        how = form["how"]
        # details = form["details"]
        details = form.getlist("details")

        print(title)
        print(author)
        print(pages)
        print(read)
        print(how)
        print(details)

        details_string = ", ".join(details)


        book_dict = {
            "title": title,
            "author": author,
            "pages": pages,
            "read": read,
            "how": how,
            # "details": details,
            "details": details_string,
        }
        
        print(book_dict)
        book_list.append(book_dict)
        print(book_list)
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
    
@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template(
        "about.html", pageTitle="About Page", books=book_list
    )

@app.route("/base", methods=["GET", "POST"])
def base():
    return render_template(
        "base.html", pageTitle="Base Page", books=book_list
    )

if __name__ == "__main__":
    app.run(debug=True)
