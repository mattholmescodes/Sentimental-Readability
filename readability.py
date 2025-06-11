import os
from flask import Flask, render_template, request, url_for, flash, get_flashed_messages, redirect
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.secret_key= os.getenv("SECRET_KEY")

def readability(text):

    # Count letters
    letters = sum(1 for c in text if c.isalpha())

    # Count number of words in text

    words = text.count(' ') + 1

    # Count number of sentences in text

    sentences = text.count('.') + text.count('!') + text.count('?')

    # Calculate number of letters per 100 words

    averageLetters = float((float(letters) / float(words)) * 100)

    # Calculate number of sentences per 100 words

    averageSentences = float((float(sentences) / float(words)) * 100)

    # Calculate Coleman-Liau

    colemanLiau = float(0.0588 * float(averageLetters) - 0.296 * float(averageSentences) - 15.8)

    # Print final results

    if colemanLiau < 1:
        return "Before Grade 1"
    elif colemanLiau > 16:
        return "Grade 16+"
    else:
        return f"Grade {round(colemanLiau)}"

@app.route("/", methods=["GET", "POST"])
def layout():
    result = None
    text = ""
    if request.method == "POST":
        text = request.form.get("text", "")
        result = readability(text)
        flash(result)
        return redirect(url_for("layout"))
    flashed = get_flashed_messages()
    result = flashed[0] if flashed else None
    return render_template("index.html", result=result)