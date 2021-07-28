import os
from typing import Union

import requests
from PyPtt import PTT


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
        check_mail = ptt.has_new_mail()

        user = ptt.get_user(os.getenv('acc'))
        text = f'✔ PTT 已成功簽到\n已登入 {user.login_time} 天\n'
        if check_mail:
            text += '👀 你有新信件！'
        tg.sendMessage(text)


if __name__ == '__main__':
    daily_login()
