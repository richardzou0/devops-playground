from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route("/")
def hello():
    r.incr("hits")
    count = r.get("hits").decode("utf-8")
    return f"""
    <html>
        <head>
            <title>Flask + Redis Counter</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin-top: 100px;
                    background-color: #f4f4f4;
                }}
                .counter {{
                    font-size: 2em;
                    color: #333;
                }}
            </style>
        </head>
        <body>
            <h1>Welcome to My Flask + Redis App</h1>
            <p class="counter">You've hit this page {count} times.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)