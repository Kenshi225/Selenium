# Selenium

このプログラムを実行するには下記が必要です。
- Pythonのインストール -> https://www.python.org/downloads/
- seleniumのインストール -> pythonインストール後コマンドプロントで(pip install selenium)を実行
- webdriverのダウンロード -> https://chromedriver.chromium.org/downloads
- ログイン情報(17-19行目)
- 時刻の編集(40,41,45,46行目)

ダウンロードしたwebdriverのPathを指定、8,9行目を適宜書き直してください。
```
driver = webdriver.Chrome()
driver.get('https://www.google.com/')
```
↓
```
driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
```
