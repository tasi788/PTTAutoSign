import os
import requests
from PyPtt import PTT
from datetime import datetime, timezone, timedelta
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


# 設定為 +8 時區
tz = timezone(timedelta(hours=+8))

# get env
BOT_TOKEN = os.getenv('bot_token')
CHAT_ID = os.getenv('chat_id')

if not os.getenv('ptt_id_1'):
    print('未輸入帳號資料')
    os.exit(1)

ptt_account = list([os.getenv('ptt_id_1')])
for i in range(2, 6):
    pttid_ = os.getenv(f'ptt_id_{i}')
    if pttid_:
        ptt_account.append(pttid_)

ptt = PTT.API(
    log_level=PTT.log.level.SILENT
)
tg = Bot(BOT_TOKEN,
         CHAT_ID)


def daily_login(ptt_id: str, ptt_passwd: str):
    try:
        ptt.login(
            ptt_id,
            ptt_passwd,
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

        user = ptt.get_user(ptt_id)
        text = f'✅ PTT {pttid} 已成功簽到\n'
        text += f'📆 已登入 {user.login_time} 天\n'
        if check_mail:
            text += '👀 你有新信件！\n'
        now: datetime = datetime.now(tz)
        text += f'#ptt #{now.strftime("%Y%m%d")}'
        tg.sendMessage(text)
        ptt.logout()


if __name__ == '__main__':
    for pttid in ptt_account:
        ptt_id, ptt_passwd = pttid.split(',')
        daily_login(ptt_id, ptt_passwd)
