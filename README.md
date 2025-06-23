# CS50 Readability (Flask)

Taken from CS50's Sentimental Readability, this is a flask app which computes the reading grade of text excerpts using the Coleman-Liau index

## Features

- **3D Flip-Card UI**: A card that flips to reveal the grade after submission, then flips back to allow new entries.
- **Responsive Design**: Works on both mobile and desktop.
- **Customizable Styles**: Uses CSS gradients, fonts from Google Fonts, and smooth transitions.

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/mattholmescodes/readability-checker.git
cd readability-checker
```

2. **Create a virtual environment**
```bash
python3 -m venv venv
```

3. **Activate the virtual environment**
on macOS / Linux:
```bash
source venv/bin/activate
```

on Windows (PowerShell):
```
.\venv\Scripts\Activate.ps1
```

4. **Set up environment variables**

Create a .env file at the project root with at least:
```bash
SECRET_KEY=<a-random-hex-string>
```

You can generate one with:
```bash
python3 - <<EOF
import secrets; print("SECRET_KEY=" + secrets.token_hex(16))
EOF
```

5. **Configure Flask**
```bash
export FLASK_APP=readability.py # macOS / Linux
$Env:FLASK_APP = "readability.py" # Windows PowerShell
```

6. **Run the application**
```bash
flask run
```

7. **Visit in your browser**
```bash
Open http://127.0.0.1:5000
```