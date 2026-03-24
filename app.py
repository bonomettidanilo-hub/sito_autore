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
                height:100vh;
                background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.9)),
                url('https://i.imgur.com/E8RiFb6.jpeg');
                background-size: cover;
                background-position: center;
                display:flex;
                flex-direction:column;
                align-items:center;
                justify-content:center;
                padding:20px;
            }

            .lang-switch {
                position:absolute;
                top:20px;
                right:20px;
            }

            .lang-switch button {
                margin:5px;
                padding:8px 12px;
                border:none;
                background:red;
                color:white;
                cursor:pointer;
            }

            .reviews-hero {
                margin-top:20px;
                max-width:700px;
                font-style:italic;
                color:#ddd;
            }

            .highlight-review {
                margin-top:20px;
                font-weight:bold;
                color:#fff;
            }

            .author {
                margin-top:10px;
                font-size:0.9em;
                color:#ccc;
            }

            .videos {
                margin-top:40px;
            }

            .bio {
                margin-top:60px;
                max-width:800px;
                margin-left:auto;
                margin-right:auto;
                line-height:1.6;
                padding:20px;
            }

            .bio img {
                width:180px;
                border-radius:100px;
                margin-bottom:20px;
            }

            .books {
                display:flex;
                justify-content:center;
                gap:40px;
                flex-wrap:wrap;
                margin-top:30px;
            }

            .book img {
                width:220px;
                border-radius:10px;
            }

            .btn {
                display:inline-block;
                margin-top:15px;
                padding:12px 25px;
                background:red;
                color:white;
                text-decoration:none;
                border-radius:5px;
                font-weight:bold;
            }

            .it { display:block; }
            .en { display:none; }

        </style>

        <script>
            function setLanguage(lang) {
                let itElements = document.getElementsByClassName('it');
                let enElements = document.getElementsByClassName('en');

                for (let el of itElements) {
                    el.style.display = (lang === 'it') ? 'block' : 'none';
                }

                for (let el of enElements) {
                    el.style.display = (lang === 'en') ? 'block' : 'none';
                }
            }
        </script>

    </head>

    <body onload="setLanguage('it')">

        <div class="lang-switch">
            <button onclick="setLanguage('it')">🇮🇹 IT</button>
            <button onclick="setLanguage('en')">🇬🇧 EN</button>
        </div>

        <div class="hero">

            <h2>Danilo Bonometti</h2>

            <h1 class="it">
                Missioni impossibili. Montagne ostili. Sopravvivere non è garantito.
            </h1>

            <h1 class="en">
                Impossible missions. Hostile mountains. Survival is not guaranteed.
            </h1>

            <div class="reviews-hero it">
                “Storia ben costruita e ambientazione molto realistica.”<br>
                “Azione continua e coinvolgente fino alla fine.”
                <div class="highlight-review">
                “C'è un nuovo sceriffo nel thriller militare: Danilo Bonometti.”
                </div>
                <div class="author">— Payne Harrison</div>
            </div>

            <div class="reviews-hero en">
                “Well-structured story with strong realism.”<br>
                “Engaging action from start to finish.”
                <div class="highlight-review">
                “There’s a new sheriff in town in military thrillers.”
                </div>
                <div class="author">— Payne Harrison</div>
            </div>

        </div>

        <!-- VIDEO -->
        <div class="videos">
            <h2 class="it">Guarda l’azione</h2>
            <h2 class="en">Watch the action</h2>

            <iframe width="350" height="200" src="https://www.youtube.com/embed/WuZVreNsIP4"></iframe>
            <iframe width="350" height="200" src="https://www.youtube.com/embed/F44s3FMVpAs"></iframe>
        </div>

        <!-- BIO -->
        <div class="bio">

            <img src="https://i.imgur.com/fE0M4Is.jpeg">

            <h2 class="it">L'autore</h2>
            <h2 class="en">About the author</h2>

            <p class="it">
            Danilo Bonometti è autore di thriller militari appartenenti alla collana Action Tricolore,
            ambientati tra montagne estreme e operazioni speciali. I protagonisti sono operatori italiani
            altamente addestrati, impegnati in missioni ad alto rischio.
            Le sue storie puntano su realismo, tensione e immersione totale.
            </p>

            <p class="en">
            Danilo Bonometti writes military thrillers within the Action Tricolore series,
            featuring elite Italian operators in extreme mountain missions.
            His stories focus on realism, tension and immersive high-risk scenarios.
            </p>

        </div>

        <!-- LIBRI IT -->
        <div class="it">
            <h2>I miei thriller</h2>

            <div class="books">

                <div class="book">
                    <img src="https://i.imgur.com/LLk2xv1.jpeg">
                    <h3>Quota 3000 – Scontro tra le rocce</h3>
                    <a href="https://amzn.eu/d/0dI3x2wD" class="btn">Acquista</a>
                </div>

                <div class="book">
                    <img src="https://i.imgur.com/C8pXDwC.jpeg">
                    <h3>L’ombra del predatore</h3>
                    <a href="https://amzn.eu/d/01ST1DQa" class="btn">Acquista</a>
                </div>

            </div>
        </div>

        <!-- LIBRI EN -->
        <div class="en">
            <h2>My thrillers</h2>

            <div class="books">

                <div class="book">
                    <img src="https://i.imgur.com/diVeXge.jpeg">
                    <h3>Altitude 10,000FT</h3>
                    <a href="https://a.co/d/02W4gjlu" class="btn">Buy</a>
                </div>

                <div class="book">
                    <img src="https://i.imgur.com/7OCBSFm.jpeg">
                    <h3>The Shadow of the Predator</h3>
                    <a href="https://a.co/d/052qjtIE" class="btn">Buy</a>
                </div>

            </div>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
