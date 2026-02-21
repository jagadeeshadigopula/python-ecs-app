from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Prometheus counter for requests
REQUESTS = Counter('python_app_requests_total', 'Total HTTP Requests')

@app.route('/')
def home():
    REQUESTS.inc()
    return "Hello from ECS Python App! 🚀"

@app.route('/metrics')
def metrics():
    return generate_latest(REQUESTS), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)