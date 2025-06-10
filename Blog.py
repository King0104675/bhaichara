from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/yash")
def yash():
    return render_template('yash.html')

@app.route("/harsh")
def harsh():
    return render_template('harsh.html')

@app.route("/anirudh")
def anirudh():
    return render_template('anirudh.html')

if __name__ == "__main__":
    app.run(debug=True)
