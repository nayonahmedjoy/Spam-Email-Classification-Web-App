from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("spam_email_model.joblib")
vectorizer = joblib.load("tfidf_vectorizer.joblib")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    email_text = ""

    if request.method == "POST":
        email_text = request.form["email"]
        email_vector = vectorizer.transform([email_text])
        result = model.predict(email_vector)[0]
        prediction = result.upper()

    return render_template("index.html", prediction=prediction, email_text=email_text)

if __name__ == "__main__":
    app.run(debug=True)
