import requests
from fetchData import main

TOKEN = "7330917684:AAG0XhfkGbDrn7gfwQ9XFpqIcLRmq96xzAU"
CHAT_ID = "6912329538"
URL = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
message = str(main())
SENDMESSAGE = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"

def send_message():
    return requests.get(SENDMESSAGE).json()
