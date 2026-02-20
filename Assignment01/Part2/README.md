# CALC // Neural Calculator

A sleek, production-grade calculator web app built with **Flask + Python + HTML/CSS/JS**.

## Stack
- **Backend**: Python 3 + Flask (REST API for computation)
- **Frontend**: Vanilla HTML5, CSS3, JavaScript (no frameworks)

## Features
- Full arithmetic: `+`, `−`, `×`, `÷`
- Percentage calculation
- Sign toggle (+/−)
- Calculation history (last 5 results, clickable)
- Keyboard support
- Secure server-side evaluation (sandboxed `eval`)
- Animated cyberpunk UI with grid background, floating orbs, and glow effects

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Then open: http://localhost:5050

## Project Structure

```
calculator/
├── app.py              # Flask backend + /calculate API endpoint
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Frontend (HTML + CSS + JS in one file)
└── README.md
```

## API

**POST** `/calculate`

Request body:
```json
{ "expression": "12 + 34 * 2" }
```

Response:
```json
{ "result": "80", "error": false }
```
