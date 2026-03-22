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
                padding:100px 20px;
            }
        </style>
    </head>

    <body>

        <div class="hero">
            <h2>Danilo Bonometti</h2>
            <h1>Thriller ad alta tensione tra montagne e missioni estreme</h1>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
