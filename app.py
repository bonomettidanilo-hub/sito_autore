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

            .section {
                margin-top:60px;
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
                margin-top:10px;
                padding:10px 20px;
                background:red;
                color:white;
                text-decoration:none;
                border-radius:5px;
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
            <h1>Thriller ad alta tensione tra montagne e missioni estreme</h1>

            <!-- RECENSIONI -->
            <div class="reviews-hero it">
                “Storia ben costruita e ambientazione molto realistica.”<br>
                “Azione continua e coinvolgente fino alla fine.”

                <div class="highlight-review">
                “C'è un nuovo sceriffo nel thriller militare: Danilo Bonometti.”
                </div>

                <div class="author">
                — Payne Harrison, autore bestseller del New York Times
                </div>
            </div>

            <div class="reviews-hero en">
                “Well-structured story with strong realism.”<br>
                “Engaging action from start to finish.”

                <div class="highlight-review">
                “There’s a new sheriff in town in military thrillers: Danilo Bonometti.”
                </div>

                <div class="author">
                — Payne Harrison, New York Times bestselling author
                </div>
            </div>

        </div>

        <!-- ITALIANO -->
        <div class="section it">
            <h2>I miei thriller</h2>

            <div class="books">

                <div class="book">
                    <img src="https://i.imgur.com/LLk2xv1.jpeg?v=20">
                    <h3>Quota 3000 – Scontro tra le rocce</h3>
                    <a href="https://amzn.eu/d/0dI3x2wD" target="_blank" class="btn">
                        Acquista su Amazon
                    </a>
                </div>

                <div class="book">
                    <img src="https://i.imgur.com/C8pXDwC.jpeg?v=20">
                    <h3>L’ombra del predatore</h3>
                    <a href="https://amzn.eu/d/01ST1DQa" target="_blank" class="btn">
                        Acquista su Amazon
                    </a>
                </div>

            </div>
        </div>

        <!-- INGLESE -->
        <div class="section en">
            <h2>My thrillers</h2>

            <div class="books">

                <div class="book">
                    <img src="https://i.imgur.com/diVeXge.jpeg">
                    <h3>Altitude 10,000FT: Rock Siege</h3>
                    <a href="https://a.co/d/02W4gjlu" target="_blank" class="btn">
                        Buy on Amazon.com
                    </a>
                </div>

                <div class="book">
                    <img src="https://i.imgur.com/7OCBSFm.jpeg">
                    <h3>The Shadow of the Predator</h3>
                    <a href="https://a.co/d/052qjtIE" target="_blank" class="btn">
                        Buy on Amazon.com
                    </a>
                </div>

            </div>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
