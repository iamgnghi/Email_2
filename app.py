from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # lấy dữ liệu từ form
        firstname = request.form.get("firstname", "")
        lastname = request.form.get("lastname", "")
        email = request.form.get("email", "")
        dob = request.form.get("dob", "")
        source = request.form.get("source", "")
        announcement = request.form.get("announcement")  # None nếu không check
        email_announcement = request.form.get("email_announcement")  # None nếu không check
        contact = request.form.get("contact", "")

        # render trực tiếp sang result.html, không cần query string
        return render_template(
            "result.html",
            firstname=firstname,
            lastname=lastname,
            email=email,
            dob=dob,
            source=source,
            announcement=announcement,
            email_announcement=email_announcement,
            contact=contact
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
