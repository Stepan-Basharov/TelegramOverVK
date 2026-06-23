from flask import Flask, request, jsonify

from vk_adapter.handler import handle_vkontakte_update
from tg_adapter.handler import handle_telegram_update

app = Flask(__name__)


@app.route("/vk_adapter", methods=["POST"])
def vk_webhook():
    data = request.get_json()

    if not data:
        return "no data", 400

    # optional: VK confirmation handshake
    if data.get("type") == "confirmation":
        return "47204d18"

    # dispatch VK event to handler
    handle_vkontakte_update(data)

    return "ok"


@app.route("/tg_adapter", methods=["POST"])
def telegram_webhook():
    data = request.get_json()

    if not data:
        return "no data", 400

    # dispatch Telegram update to handler
    handle_telegram_update(data)

    return "ok"


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1984, debug=True)