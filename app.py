from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AWS Scalable Web Application</title>
    </head>
    <body>
        <h1>Hello from AWS ECS Fargate!</h1>
        <p>My containerized web application is working.</p>
        <p>Environment: Development</p>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)