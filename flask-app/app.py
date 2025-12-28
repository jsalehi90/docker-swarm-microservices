import os, socket, time, redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)

@app.route('/')
def hello():
    try:
        count = cache.incr('hits')
    except:
        count = "Redis not ready"
    return f"Hello! Hits: {count}. Host: {socket.gethostname()}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
