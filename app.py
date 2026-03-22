from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Danilo Bonommetti - Thriller</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background-color: #000;
                color: white;
            }

            .hero {
                height: 100vh;
                background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.9)),
                url('https://images.unsplash.com/photo-1501785888041-af3ef285b470');
                background-size: cover;
                background-position: center;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
            }

            .hero h1 {
                font-size: 3em;
                max-width: 800px;
            }

            .section {
                padding: 60px 20px;
                text-align: center;
                background: #111;
            }

            .books {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 40px;
                margin-top: 40px;
            }

            .book {
                max-width: 300px;
            }

            .book img {
                width: 100%;
                border-radius: 10px;
            }

            .btn {
                display: inline-block;
                margin-top: 15px;
                padding: 12px 20px;
                background: red;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
            }

            .btn:hover {
                background: darkred;
            }
        </style>
    </head>

    <body>

        <div class="hero">
            <h1>Thriller ad alta tensione tra montagne, pericolo e sopravvivenza</h1>
        </div>

        <div class="section">
            <h1>I miei thriller</h1>

            <div class="books">

                <div class="book">
                    <img src="https://i.imgur.com/C8pXDwC.jpeg">
                    <h2>Quota 3000 – Scontro fra le rocce</h2>
                    <p>Un thriller ad alta tensione tra le montagne, dove ogni passo può essere l’ultimo.</p>
                    <a href="https://amzn.eu/d/0dI3x2wD" target="_blank" class="btn">Acquista su Amazon</a>
                </div>

                <div class="book">
                    <img src="https://i.imgur.com/LLk2xv1.jpeg">
                    <h2>L’ombra del predatore</h2>
                    <p>Il sequel ancora più oscuro, dove il pericolo non si vede… ma è sempre presente.</p>
                    <a href="https://amzn.eu/d/01ST1DQa" target="_blank" class="btn">Acquista su Amazon</a>
                </div>

            </div>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
