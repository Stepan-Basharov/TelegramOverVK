from telegram.client import send_to_telegram

vk_to_tg_map = {
    123: 456789
}

def route_message(msg):
    if msg["platform"] == "vkontakte":
        tg_chat = vk_to_tg_map.get(msg["chat_id"])

        if not tg_chat:
            print("No mapping for VK chat")
            return

        send_to_telegram(tg_chat, f"[VK] {msg['text']}")