import os
import json


from flask import Flask, Response, jsonify, request
from cachelib import SimpleCache
from SourceWatch import Query


app = Flask(__name__)
cache = SimpleCache()

# Default values
HLDS_DEFAULT_QUERY_SERVER = os.getenv(
    "HLDS_DEFAULT_QUERY_SERVER", "steamcalculator.com"
)
HLDS_DEFAULT_QUERY_PORT = int(os.getenv("HLDS_DEFAULT_QUERY_PORT", 27015))
HLDS_ADDRESS = os.getenv("HLDS_ADDRESS", "127.0.0.1")
HLDS_PORT = int(os.getenv("HLDS_PORT", 27000))


@app.route("/")
def info():
    server = request.args.get("server", HLDS_DEFAULT_QUERY_SERVER)
    port = int(request.args.get("port", HLDS_DEFAULT_QUERY_PORT))
    cache_key = f"status_{server}_{port}"

    result = cache.get(cache_key)

    if not result:
        query = Query(server, port)
        result = query.info() | query.rules() | query.players()
        cache.set(cache_key, result, 10)
    return Response(
        response=json.dumps(result, indent=2),
        status=200,
        mimetype="application/json",
    )


@app.route("/ping")
def ping():
    return "pong"


@app.errorhandler(Exception)
def handle_error(e):
    return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host=HLDS_ADDRESS, port=HLDS_PORT)
