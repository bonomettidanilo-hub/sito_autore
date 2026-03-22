from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Danilo Bonometti</title>
        <style>
            body {
                margin:0;
                font-family: Arial;
                background:#000;
                color:white;
                text-align:center;
            }

            .hero {
                padding:80px 20px;
            }

            .highlight {
                color: gold;
                margin-top:10px;
                font-size:1.2em;
            }

            .description {
                max-width:800px;
                margin:30px auto;
                color:#ccc;
                line-height:1.6;
            }

            .books {
                display:flex;
                justify-content:center;
                gap:40px;
                flex-wrap:wrap;
                margin-top:50px;
            }

            .book img {
                width:250px;
                border-radius:10px;
            }

            .btn {
                display:inline-block;
                margin-top:15px;
                padding:10px 20px;
                background:red;
                color:white;
                text-decoration:none;
                border-radius:5px;
            }

            .reviews {
                margin-top:60px;
                padding:40px;
                background:#111;
            }

            .review {
                max-width:700px;
                margin:20px auto;
                font-style:italic;
                color:#ddd;
            }

            .author {
                margin-top:10px;
                font-weight:bold;
                color:#aaa;
            }
        </style>
    </head>

    <body>

        <div class="hero">
            <h2>Danilo Bonometti</h2>
            <h1>Thriller ad alta tensione tra montagne e missioni estreme</h1>

            <div class="highlight">
                Collana Action Tricolore
            </div>

            <div class="description">
                I romanzi fanno parte della collana <b>Action Tricolore</b>, una serie di thriller accomunati da protagonisti italiani altamente qualificati in ambito militare.
                Le storie si sviluppano in scenari realistici, tra operazioni speciali, ambienti estremi e missioni ad alto rischio.
            </div>
        </div>

        <div class="books">

            <div class="book">
                <img src="https://i.imgur.com/LLk2xv1.jpeg?v=11">
                <h2>Quota 3000 – Scontro tra le rocce</h2>
                <a href="https://amzn.eu/d/0dI3x2wD" target="_blank" class="btn">
                    Acquista su Amazon
                </a>
            </div>

            <div class="book">
                <img src="https://i.imgur.com/C8pXDwC.jpeg?v=11">
                <h2>L’ombra del predatore</h2>
                <a href="https://amzn.eu/d/01ST1DQa" target="_blank" class="btn">
                    Acquista su Amazon
                </a>
            </div>

        </div>

        <div class="reviews">
            <h2>Cosa dicono i lettori</h2>

            <div class="review">
                “Storia ben costruita e ambientazione molto realistica. Si percepisce la competenza dietro ogni dettaglio.”
            </div>

            <div class="review">
                “Azione continua, ma senza eccessi. La parte ambientata in montagna è particolarmente coinvolgente.”
            </div>

            <div class="review">
                “Lettura scorrevole e tesa fino alla fine. Ottimo equilibrio tra tecnica e narrazione.”
            </div>

            <div class="review">
                “C'è un nuovo sceriffo in città nel genere dei thriller militari e si chiama Danilo Bonometti. 
                Il suo libro ALTITUDE 10,000FT: Rock Siege ti porta dentro il 4° Reggimento Ranger Alpini dell'Italia 
                in una missione di salvataggio ambientata nelle Dolomiti - un terreno tanto accidentato e mortale quanto bello. 
                L'autore intreccia autenticità e azione in una trama piena di sorprese lungo il cammino. 
                Non vedo l'ora di leggere futuri romanzi dalla penna di Danilo Bonometti.”
                <div class="author">
                — Payne Harrison, autore bestseller del New York Times
                </div>
            </div>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
