# PTTAutoSign
PTT 自動簽到，最近老人在用的 PTT 終於又重新開方註冊了，我也嘗試當個老人。

1. 首先右上角 Star 給他按下去，接著 `fork` 一份。
2. 接著打開 [appveyor](https://ci.appveyor.com/login) 用一個舒服的方式登入或註冊。
3. 點一下 `New Project`，並找到剛剛 `fork` 走的 `repo`。 \
![image](https://user-images.githubusercontent.com/11913223/127419686-82ac7564-4925-490e-8b08-98e7b90a6974.png)
4. 接著點 `Settings`，左邊的 `General` \
![image](https://user-images.githubusercontent.com/11913223/127419874-47e790c2-7a8b-4bc1-b32e-b3b6f207858d.png)
5. 在同一頁面往下滾動~ 找到這幾個選像打勾
```
Do not build feature branches with open Pull Requests
Do not build on "Push" events
Do not build on "Pull request" events
```
![image](https://user-images.githubusercontent.com/11913223/127419928-1547079a-c735-411c-ba8c-75b7614f01a7.png)

6. 點左邊的 `Environment` 設定環境參數 
```
bot_token  -> telegram bot token
chat_id    -> telegram chat id
ptt_id_1   -> ptt 帳號 (username,passwd)
ptt_id_2   -> ptt 帳號 (username,passwd)
```
不知道 `chat_id` 嗎？請參考下方 FAQ \
![image](https://user-images.githubusercontent.com/11913223/127420317-7c2fa5f3-5ac5-494c-ad93-a02047e4c890.png)

7. 點[這裡](https://ci.appveyor.com/api-keys)來獲取 appveyor 的 `api-key`，記得選自己的帳號，接著將下方顯示的東西複製起來。 \
![image](https://user-images.githubusercontent.com/11913223/127420746-749ebdbb-af85-4a05-b53f-5c4be656abda.png)

8. 接著回到 GitHub 點 `Settings` `Secrets` `New repository secret`，將剛剛複製的 `api-key` 貼上。 \
![image](https://user-images.githubusercontent.com/11913223/127420954-2ec5d45e-4f77-4c51-93be-33b69d46062d.png)

9. 點自己 `Repo` 的 `Action`，找到左側 `Daily Trigger` 打開 workflow。 \
![image](https://user-images.githubusercontent.com/11913223/127421102-ada99cea-f20b-43ca-8899-8ba65b4b733b.png)

10. 自動同步更新原始碼，請點[這裡](https://github.com/apps/pull)，並點一下綠色的 Install，如果安裝過請點 `Configure`。 \
![image](https://user-images.githubusercontent.com/11913223/127421412-7b146eab-4b12-4aea-b95a-656a49c73df2.png)

11. Enjoy 🎉


## FAQ
Q: 我怎麼找到我的 `bot_token` \
A: 先去找 @Botfather 申請一個，之後會拿到一個 `token` 像是 `1234567:abcdefghijklmnopqrstuwxyz` 

Q: 我要怎麼知道 `chat_id`？頻道或群組支援嗎？ \
A: 拆開講。 \
如果你要拿自己的 `chat_id` 直接私訊 @my_id_bot \
如果你要拿頻道的 `chat_id` 開好一個頻道，在頻道裡面隨便打一段字，接著將那串文字轉傳給 @my_id_bot \
如果你要拿群組的 `chat_id` 直接把 @my_id_bot 加進群組
