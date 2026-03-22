from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Quota 3000 Thriller</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #0b0f19;
            color: white;
        }

        .hero {
            padding: 100px 20px;
            text-align: center;
            background: url('https://images.unsplash.com/photo-1501785888041-af3ef285b470') no-repeat center;
            background-size: cover;
        }

        .hero h1 {
            font-size: 42px;
            margin-bottom: 20px;
        }

        .hero p {
            font-size: 18px;
            margin-bottom: 30px;
        }

        .btn {
            background-color: #dc2626;
            padding: 15px 25px;
            color: white;
            text-decoration: none;
            font-weight: bold;
            border-radius: 5px;
        }

        .btn:hover {
            background-color: #b91c1c;
        }

        .section {
            padding: 50px 20px;
            max-width: 900px;
            margin: auto;
        }

        .book {
            margin-bottom: 60px;
        }

        .book h2 {
            font-size: 28px;
            margin-bottom: 10px;
        }

        .book p {
            font-size: 16px;
            margin-bottom: 15px;
        }

        blockquote {
            font-style: italic;
            font-size: 20px;
            text-align: center;
            margin-top: 50px;
        }

        footer {
            text-align: center;
            padding: 20px;
            background: #020617;
            margin-top: 40px;
        }
    </style>
</head>

<body>

<div class="hero">
    <h1>Un thriller ad alta tensione tra le montagne italiane</h1>
    <p>Un’operazione militare fallita. Un uomo braccato. Sopravvivere è l’unica missione.</p>
    <a class="btn" href="https://amzn.eu/d/0dI3x2wD" target="_blank">Inizia dal primo libro</a>
</div>

<div class="section">

    <div class="book">
        <h2>📘 Libro 1 — Quota 3000: Scontro fra le rocce</h2>
        <p>
        Un’operazione militare si trasforma in una trappola mortale.
        Tra neve, roccia e silenzio, il nemico osserva e colpisce.
        Non c’è via di fuga.
        </p>
        <a class="btn" href="https://amzn.eu/d/0dI3x2wD" target="_blank">Acquista ora</a>
    </div>

    <div class="book">
        <h2>📕 Libro 2 — L’ombra del predatore</h2>
        <p>
        Il pericolo non è finito.
        Qualcuno continua a cacciare nell’ombra.
        E questa volta, nessuno è al sicuro.
        </p>
        <a class="btn" href="https://amzn.eu/d/01ST1DQa" target="_blank">Continua la serie</a>
    </div>

    <blockquote>
        “There’s a new sheriff in town…” – Payne Harrison
    </blockquote>

</div>

<footer>
    <p>© 2026 - D. Bonomettiauthor</p>
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)