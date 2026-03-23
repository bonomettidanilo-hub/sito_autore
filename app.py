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
        </style>

        <script>
            function setLanguage(lang) {
                document.getElementById('it').style.display = (lang === 'it') ? 'block' : 'none';
                document.getElementById('en').style.display = (lang === 'en') ? 'block' : 'none';
            }
        </script>

    </head>

    <body onload="setLanguage('it')">

        <!-- BOTTONI LINGUA -->
        <div class="lang-switch">
            <button onclick="setLanguage('it')">🇮🇹 IT</button>
            <button onclick="setLanguage('en')">🇬🇧 EN</button>
        </div>

        <div class="hero">
            <h2>Danilo Bonometti</h2>
            <h1>Thriller ad alta tensione tra montagne e missioni estreme</h1>
        </div>

        <!-- ITALIANO -->
        <div id="it">

            <div class="section">
                <h2>I miei thriller</h2>

                <div class="books">

                    <div class="book">
                        <img src="https://i.imgur.com/LLk2xv1.jpeg?v=18">
                        <h3>Quota 3000 – Scontro tra le rocce</h3>
                        <a href="https://amzn.eu/d/0dI3x2wD" target="_blank" class="btn">
                            Acquista su Amazon
                        </a>
                    </div>

                    <div class="book">
                        <img src="https://i.imgur.com/C8pXDwC.jpeg?v=18">
                        <h3>L’ombra del predatore</h3>
                        <a href="https://amzn.eu/d/01ST1DQa" target="_blank" class="btn">
                            Acquista su Amazon
                        </a>
                    </div>

                </div>
            </div>

        </div>

        <!-- INGLESE -->
        <div id="en">

            <div class="section">
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

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

