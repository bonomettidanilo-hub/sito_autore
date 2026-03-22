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
        </style>
    </head>

    <body>

        <div class="hero">
            <h2>Danilo Bonometti</h2>
            <h1>Thriller ad alta tensione tra montagne e missioni estreme</h1>
        </div>

        <div class="books">

            <!-- QUOTA 3000 -->
            <div class="book">
                <img src="https://i.imgur.com/LLk2xv1.jpeg?v=9">
                <h2>Quota 3000 – Scontro tra le rocce</h2>
                <a href="https://amzn.eu/d/0dI3x2wD" target="_blank" class="btn">
                    Acquista su Amazon
                </a>
            </div>

            <!-- OMBRA DEL PREDATORE -->
            <div class="book">
                <img src="https://i.imgur.com/C8pXDwC.jpeg?v=9">
                <h2>L’ombra del predatore</h2>
                <a href="https://amzn.eu/d/01ST1DQa" target="_blank" class="btn">
                    Acquista su Amazon
                </a>
            </div>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
