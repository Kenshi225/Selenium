# Selenium

8,9行目の部分は下記サイトより使用しているchromeのバージョンに合ったwebdriverをダウンロードして、配置したPathに適宜書き直してください。

https://chromedriver.chromium.org/downloads

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

↓

例
driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')

また、40,41,45,46行目はそれぞれ開始時間と終了時間、休憩時間となっています。
