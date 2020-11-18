import json
import re
import os
import socket
import settings
import time
from cqhttp import CQHttp, Error

bot = CQHttp(api_root='http://127.0.0.1:5700/',
             access_token='',
             secret='')

owner = settings.owner
keyword = settings.keyword
localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :" + localtime)

@bot.on_message
def handle_msg(event):
    global keyword
    global owner
    if any(key in event['message'] for key in keyword) and event['message_type'] != 'private' and event['user_id'] != owner:
        print(event['message'])
        print('get')
        nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        sendmessage = nowtime + '“' + str(event['user_id']) + '”在“' + str(event['group_id']) + '”群说了“'+event['message'] + '"'
        bot.send({'user_id': owner}, sendmessage)






if __name__ == '__main__':
    bot.run(host='127.0.0.1', port=8887)