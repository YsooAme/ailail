from pyrogram import Client, filters

bot_token = "6724982232:AAEIfqKAJmf1CSw1gV5xZSPNv5Yh0kg38pQ"

api_id = 25281175
api_hash = "6d99cb2b60a2c519fc1f99bd19565730"
app = Client("nb", api_id, api_hash, bot_token=bot_token)


app.start()


@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(f"Hello")


app.run()

