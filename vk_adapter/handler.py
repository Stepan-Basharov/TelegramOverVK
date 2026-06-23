from core.router import route_message
def handle_vkontakte_update(raw):

    print(raw["object"]["message"])
    data = {"platform": "vk_adapter", "text": raw["object"]["message"]["text"], "chat_id": 123}

    route_message(data)