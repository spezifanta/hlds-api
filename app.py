import logging
import os


from flask import Flask, jsonify
from werkzeug.contrib.cache import SimpleCache
from SourceWatch import Query

# Disable Flask logging.
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
app.config.update(
  JSONIFY_PRETTYPRINT_REGULAR=True
)
cache = SimpleCache()

# Inject server by using environment variables.
server = os.getenv('HLDS_IP', 'steamcalculator.com')
port = int(os.getenv('HLDS_PORT', 27015))

@app.route('/')
def info():
    result = cache.get('status')
    if not result:
        query = Query(server, port)
        result = query.info()
        result = {**result, **query.rules()}
        result = {**result, **query.players()}
        cache.set('status', result, 10)
    return jsonify(result)

@app.route('/ping')
def ping():
    return 'pong'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=27014)
