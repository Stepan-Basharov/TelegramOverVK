from flask import Flask, request, jsonify

from vkontakte.handler import handle_vk_update
from telegram.handler import handle_telegram_update

app = Flask(__name__)


@app.route("/vkontakte", methods=["POST"])
def vk_webhook():
    data = request.get_json()

    if not data:
        return "no data", 400

    # optional: VK confirmation handshake
    if data.get("type") == "confirmation":
        return "your_confirmation_code_here"

    # dispatch VK event to handler
    handle_vk_update(data)

    return "ok"


@app.route("/telegram", methods=["POST"])
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