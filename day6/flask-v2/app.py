from flask import Flask
import os
import redis
import urllib.parse

redis_url = urllib.parse.urlparse(os.environ.get("REDIS_URL"))

r = redis.Redis(
    host=redis_url.hostname,
    port=redis_url.port,
    password=redis_url.password,
    ssl=True  # required for Fly.io Redis
)


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