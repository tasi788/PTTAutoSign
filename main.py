import os
from PyPtt import PTT

import requests
from typing import Union

class Bot:
    def __init__(self, token: str, chat_id: Union[str, int]):
        self.token = token
        self.chat_id = chat_id
        self.api_url = f'https://api.telegram.org/bot{self.token}'

    def sendMessage(self, text: str):
        r = requests.post(self.api_url + '/sendMessage',
                          json={
                              'chat_id': self.chat_id,
                              'text': text,
                              'parse_mode': 'html'
                          })

ptt = PTT.API(
    log_level=PTT.log.level.SILENT
)
tg = Bot(os.getenv('bot_token'),
         os.getenv('chat_id'))

def daily_login():
    try:
        ptt.login(
            os.getenv('acc'),
            os.getenv('passwd'),
            kick_other_login=True)
    except PTT.exceptions.NoSuchUser:
        tg.sendMessage('PTT 登入失敗！\n找不到使用者')
    except (PTT.exceptions.WrongIDorPassword, PTT.exceptions.WrongPassword):
        tg.sendMessage('PTT 登入失敗！\n帳號密碼錯誤')
    except PTT.exceptions.LoginTooOften:
        tg.sendMessage('PTT 登入失敗！\n登入太頻繁')
    except PTT.exceptions.UseTooManyResources:
        tg.sendMessage('PTT 登入失敗！\n使用過多 PTT 資源，請稍等一段時間並增加操作之間的時間間隔')
    else:
        boards = os.getenv('board')
        if not boards:
            boards = ['TigerBlue']
        else:
            boards = boards.split(',')

            for board in boards:
                _ = ptt.get_newest_index(
                    PTT.data_type.index_type.BBS,
                    board=board)
            text = 'PTT 已成功簽到\n<code>'
            text += ', '.join(e for e in boards)
            text += '</code>'
            tg.sendMessage(text)

if __name__ == '__main__':
    daily_login()