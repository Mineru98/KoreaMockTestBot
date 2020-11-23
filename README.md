# KoreaMockTestBot
한국 고등학교에서는 매년 3월 6월 9월 12월에 수능 모의고사를 봅니다.
그때마다 많은 학생들은 친구들과 서로 시험 점수를 비교하는 것을 좋아하기도 합니다.
이 파이썬 코드는 그들이 원하는 것을 빠르게 찾아주고 Excel로 바로 보여줍니다.

# Usage
```sh
python KMT.py
python KMT.py {년도 = 현재 년도} {월 = 현재 월} {학년 = 3}
```

# init setting
`pip install -r requirements.txt`

DownloadLink : https://chromedriver.chromium.org/downloads

```sh
wget https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
rm -rf chromedriver_linux64.zip
```

```sh
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -

echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list

sudo apt-get update
sudo apt-get install google-chrome-stable
```

```sh
apt-get install -y unzip
```
