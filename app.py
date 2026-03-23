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
                text-align:center;
                padding:20px;
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

            .book {
                max-width:260px;
            }

            .book img {
                width:100%;
                border-radius:10px;
                margin-top:10px;
            }

            .btn {
                display:inline-block;
                margin-top:10px;
                padding:10px 20px;
                background:red;
                color:white;
                text-decoration:none;
                border-radius:5px;
                font-size:0.9em;
            }

            .lang {
                margin-top:10px;
                font-size:0.9em;
                color:#ccc;
            }

        </style>
    </head>

    <body>

        <div class="hero">
            <h2>Danilo Bonometti</h2>
            <h1>Thriller ad alta tensione tra montagne e missioni estreme</h1>
        </div>

        <div class="section">
            <h2>I miei thriller</h2>

            <div class="books">

                <!-- LIBRO 1 -->
                <div class="book">

                    <!-- ITALIANO -->
                    <div class="lang">🇮🇹 Italiano</div>
                    <img src="https://i.imgur.com/LLk2xv1.jpeg?v=17">
                    <h3>Quota 3000 – Scontro tra le rocce</h3>
                    <a href="https://amzn.eu/d/0dI3x2wD" target="_blank" class="btn">
                        Acquista su Amazon
                    </a>

                    <!-- INGLESE -->
                    <div class="lang">🇬🇧 English</div>
                    <img src="https://i.imgur.com/diVeXge.jpeg">
                    <h3>Altitude 10,000FT: Rock Siege</h3>
                    <a href="https://a.co/d/02W4gjlu" target="_blank" class="btn">
                        Buy on Amazon.com
                    </a>

                </div>

                <!-- LIBRO 2 -->
                <div class="book">

                    <!-- ITALIANO -->
                    <div class="lang">🇮🇹 Italiano</div>
                    <img src="https://i.imgur.com/C8pXDwC.jpeg?v=17">
                    <h3>L’ombra del predatore</h3>
                    <a href="https://amzn.eu/d/01ST1DQa" target="_blank" class="btn">
                        Acquista su Amazon
                    </a>

                    <!-- INGLESE -->
                    <div class="lang">🇬🇧 English</div>
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
