import requests

chat_id = "6396782078"
urlp = "https://t.me/P_PP_Pi"
url = f"https://api.telegram.org/etChat6724982232:AAEIfqKAJmf1CSw1gV5xZSPNv5Yh0kg38pQ?chat_id={chat_id}"

req = requests.get(url).json()
print(req)
