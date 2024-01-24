from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "name": "To-Do app with Python and PostgresSQL",
        "thumb": "img/to-do.png",
        "categories": ["python", "web"],
        "slug": "To-do-List",
    },
    {
        "name": "Weather app with API and Flask",
        "thumb": "img/weather.png",
        "categories": ["flask", "api"],
        "slug": "WeatherApp",
    },
    {
        "name": "Blog Site with Python and PostgresSQL",
        "thumb": "img/blog.png",
        "categories": ["full stack", "python"],
        "slug": "BlogZilla",
    },
]


@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)