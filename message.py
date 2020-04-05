from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
import os

line_bot_api = LineBotApi('gYASpXYXSzDcD10Hq68gTpz9usBBzbLwUesj7x3N/1iKy1qWJ/6QvjRqGMXLZlqnBQ8PqFSvpXVf7OzMYKYH1GmJf2w++qfsggjHM+5luTAvphujEydI8DXsjf7KIRjIz/Bjb3vuUQyUUoIiAcYTqgdB04t89/1O/w1cDnyilFU=')

#LINE_CHANNEL_SECRET = os.environ["f7183c9e2c39ddf54e508a039d390117"]
#print(line_user_ID)
try:
    line_bot_api.push_message('U44e2443095bd21f68b4bc936f7243b43', TextSendMessage(text='水くれ'))
except LineBotApiError as e:
    # error handle
    print("Error occurred")
