### ./analyze

```markdown
( データ分析を行うフォルダです )
```

#### ~~ 初期設定 ~~

```markdown
wget https://raw.githubusercontent.com/takkii/totolot/master/analyze/install.py

python ./install.py
```

#### 作成日 2020/04/09

```markdown
Requirement already satisfied: scikit-learn in d:\python37\lib\site-packages (0.22.2.post1)
Requirement already satisfied: scipy>=0.17.0 in d:\python37\lib\site-packages (from scikit-learn) (1.4.1)
Requirement already satisfied: joblib>=0.11 in d:\python37\lib\site-packages (from scikit-learn) (0.14.1)
Requirement already satisfied: numpy>=1.11.0 in d:\python37\lib\site-packages (from scikit-learn) (1.18.2)
CompletedProcess(args=['python', '-m', 'pip', 'install', 'scikit-learn'], returncode=0, stderr='')
Requirement already satisfied: numpy in d:\python37\lib\site-packages (1.18.2)
CompletedProcess(args=['python', '-m', 'pip', 'install', 'numpy'], returncode=0, stderr='')
Requirement already satisfied: pandas in d:\python37\lib\site-packages (1.0.3)
Requirement already satisfied: numpy>=1.13.3 in d:\python37\lib\site-packages (from pandas) (1.18.2)
Requirement already satisfied: pytz>=2017.2 in d:\python37\lib\site-packages (from pandas) (2019.3)
Requirement already satisfied: python-dateutil>=2.6.1 in d:\python37\lib\site-packages (from pandas) (2.8.1)
Requirement already satisfied: six>=1.5 in d:\python37\lib\site-packages (from python-dateutil>=2.6.1->pandas) (1.14.0)
CompletedProcess(args=['python', '-m', 'pip', 'install', 'pandas'], returncode=0, stderr='')
Requirement already satisfied: requests-html in d:\python37\lib\site-packages (0.10.0)
Requirement already satisfied: pyquery in d:\python37\lib\site-packages (from requests-html) (1.4.1)
Requirement already satisfied: parse in d:\python37\lib\site-packages (from requests-html) (1.15.0)
Requirement already satisfied: bs4 in d:\python37\lib\site-packages (from requests-html) (0.0.1)
Requirement already satisfied: pyppeteer>=0.0.14 in d:\python37\lib\site-packages (from requests-html) (0.0.25)
Requirement already satisfied: fake-useragent in d:\python37\lib\site-packages (from requests-html) (0.1.11)
Requirement already satisfied: w3lib in d:\python37\lib\site-packages (from requests-html) (1.21.0)
Requirement already satisfied: requests in d:\python37\lib\site-packages (from requests-html) (2.23.0)
Requirement already satisfied: lxml>=2.1 in d:\python37\lib\site-packages (from pyquery->requests-html) (4.5.0)
Requirement already satisfied: cssselect>0.7.9 in d:\python37\lib\site-packages (from pyquery->requests-html) (1.1.0)
Requirement already satisfied: beautifulsoup4 in d:\python37\lib\site-packages (from bs4->requests-html) (4.9.0)
Requirement already satisfied: pyee in d:\python37\lib\site-packages (from pyppeteer>=0.0.14->requests-html) (7.0.1)
Requirement already satisfied: websockets in d:\python37\lib\site-packages (from pyppeteer>=0.0.14->requests-html) (8.1)
Requirement already satisfied: appdirs in d:\python37\lib\site-packages (from pyppeteer>=0.0.14->requests-html) (1.4.3)
Requirement already satisfied: urllib3 in d:\python37\lib\site-packages (from pyppeteer>=0.0.14->requests-html) (1.25.8)
Requirement already satisfied: tqdm in d:\python37\lib\site-packages (from pyppeteer>=0.0.14->requests-html) (4.45.0)
Requirement already satisfied: six>=1.4.1 in d:\python37\lib\site-packages (from w3lib->requests-html) (1.14.0)
Requirement already satisfied: chardet<4,>=3.0.2 in d:\python37\lib\site-packages (from requests->requests-html) (3.0.4)
Requirement already satisfied: idna<3,>=2.5 in d:\python37\lib\site-packages (from requests->requests-html) (2.9)
Requirement already satisfied: certifi>=2017.4.17 in d:\python37\lib\site-packages (from requests->requests-html) (2019.11.28)
Requirement already satisfied: soupsieve>1.2 in d:\python37\lib\site-packages (from beautifulsoup4->bs4->requests-html) (2.0)
CompletedProcess(args=['python', '-m', 'pip', 'install', 'requests-html'], returncode=0, stderr='')
Requirement already satisfied: beautifulsoup4 in d:\python37\lib\site-packages (4.9.0)
Requirement already satisfied: soupsieve>1.2 in d:\python37\lib\site-packages (from beautifulsoup4) (2.0)
CompletedProcess(args=['python', '-m', 'pip', 'install', 'beautifulsoup4'], returncode=0, stderr='')
```

### ~~ 実行 ~~

```markdown
Coronavirus Tracker




╔══════╤════════════╤══════════════╤═════════════╤══════════════╤══════════════╤════════════╤═══════════╤══════════╤════════════════╗
║ Rank │ Country    │ Total Cases  │ New Cases ▲ │ Total Deaths │ New Deaths ▲ │ Recovered  │ Active    │ Critical │ Cases / 1M pop ║
╟──────┼────────────┼──────────────┼─────────────┼──────────────┼──────────────┼────────────┼───────────┼──────────┼────────────────╢
║ 1    │ Japan (JP) │       63,822 │             │        1,209 │              │     51,688 │    10,925 │      246 │            505 ║
╟──────┼────────────┼──────────────┼─────────────┼──────────────┼──────────────┼────────────┼───────────┼──────────┼────────────────╢
║      │ World      │   24,344,815 │    20,243 ▲ │      829,778 │        864 ▲ │ 16,672,838 │ 6,842,199 │   61,425 │       3,123.53 ║
╚══════╧════════════╧══════════════╧═════════════╧══════════════╧══════════════╧════════════╧═══════════╧══════════╧════════════════╝

Code: https://github.com/sagarkarira/coronavirus-tracker-cli
Twitter: https://twitter.com/ekrysis

Last Updated on: 27-Aug-2020 07:08 UTC

US STATES API: https://corona-stats.online/states/us
HELP: https://corona-stats.online/help
SPONSORED BY: ZEIT NOW
Checkout fun new side project I am working on: https://messagink.com/story/5eefb79b77193090dd29d3ce/global-response-to-coronavirus
```

```markdown
python ./ruby-dic3_ana.py
```

#### [ 出力結果 ]

```markdown
                   0

0 nesting\n
1 used_modules\n
2 constants\n
3 new\n
4 allocate\n
... ...
2622 reiwa_print\n
2623 version\n
2624 himekuri\n
2625 count\n
2626 reiwa

[2627 rows x 1 columns]
```

#### ※ 読み込む辞書の行数とカウントする文字列を表示しています。

```markdown
python ./sklearn_dic.py
```

### [ 出力結果 ]

```markdown
      __callee__  __dir__  __end__  __id__  __method__  __name__  ...  yielder  zero  zerodivisionerror  zip  zone  zoom

0 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0 0.0
1 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0 0.0
2 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0 0.0
3 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0 0.0
4 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0 0.0
... ... ... ... ... ... ... ... ... ... ... ... ... ...
2622 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0 0.0
2623 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0 0.0
2624 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0 0.0
2625 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0 0.0
2626 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0 0.0

[2627 rows x 2019 columns]
```

#### ※ 重複していないことが数字でわかります。

```markdown
cd analyze

python3 corona_ja_result.py
```

#### ※ コロナウイルス対策の日本で影響範囲がわかります。

![corona_ja_result_image](https://github.com/takkii/totolot/blob/master/images/corona_ja_result.png)

### Python で Tcl/Tk を使用しコンソール画像を表示しました。

![corona_ja_result_movie](https://github.com/takkii/totolot/blob/master/images/corona_movie.gif)

### Python を実行する様子を動画にしました。

```markdown
Dice shuffle 5 times [心] ... ⚁ ⚅ ⚃ ⚃ ⚂

or

Dice shuffle 5 times [義] ... ⚂ ⚅ ⚂ ⚂ ⚅
```

### サイコロを 5 回シャッフルしてみました。

```markdown
現在の設定では、JavaScript を利用できません。有効にしてお使いくださいませ。

RSS アンテナ

～ GitHub の作業記録を RSS フィードで表示します ～

[これより、30 タイトル程ずつ履歴表示します]

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 13 日 05 時 55 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 11 日 12 時 01 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 11 日 09 時 57 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 11 日 05 時 08 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 10 日 13 時 50 分

takkii created a tag 1.6.7 in takkii/totolot
投稿時刻 ： 2020 年 04 月 10 日 13 時 47 分

takkii released もの想うトトロット at takkii/totolot
投稿時刻 ： 2020 年 04 月 10 日 13 時 47 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 10 日 09 時 44 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 10 日 09 時 17 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 10 日 07 時 12 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 10 日 07 時 10 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 09 日 22 時 50 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 09 日 13 時 46 分

takkii created a tag 1.6.6.1 in takkii/totolot
投稿時刻 ： 2020 年 04 月 09 日 10 時 15 分

takkii released 大魔神トトロット改 🚌 at takkii/totolot
投稿時刻 ： 2020 年 04 月 09 日 10 時 15 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 09 日 10 時 12 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 09 日 10 時 10 分

takkii created a tag 1.6.6 in takkii/totolot
投稿時刻 ： 2020 年 04 月 09 日 09 時 48 分

takkii released 大魔神トトロット ✴ at takkii/totolot
投稿時刻 ： 2020 年 04 月 09 日 09 時 48 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 09 日 08 時 45 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 09 日 08 時 29 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 09 日 08 時 27 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 09 日 08 時 11 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 09 日 08 時 10 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 09 日 08 時 03 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 09 日 08 時 02 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 09 日 07 時 59 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 09 日 07 時 25 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 09 日 07 時 23 分

takkii pushed to master in takkii/totolot
投稿時刻 ： 2020 年 04 月 09 日 06 時 38 分

RSS アンテナ立ち上げ記念日 / 2016 年 2 月 5 日

西暦:2020 年 04 月 13 日
和暦:令和 2 年 4 月 13 日

Ruby_VERSION : 2.7.1 Sinatra_VERSION : 2.0.8.1
Copyright 2016 ～ 2020 Takayuki Kamiyama All Rights Reserved.

Designed by NyaSoCom
```

### RSS アンテナを python で文字列表示しました。
