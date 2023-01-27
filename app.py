#compose_flask/app.py
import sys

from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis',port=6379)

@app.route('/')
def hello():
    sys.exit(0)
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed for %s time(s).' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
