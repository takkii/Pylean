[![GitHub release](https://img.shields.io/github/release/takkii/Pylean.svg?style=flat)](GitHub)[![GitHub Status](https://img.shields.io/github/last-commit/takkii/Pylean.svg?style=flat)](GitHub)

### Pylean はデータ分析用のプロジェクトです

今後はデータ分析を記録していきます。自前で、できることを集約します。

##### 「 環境構築 」

```markdown
pip3 install -r requirements.txt

env PYTHON_CONFIGURE_OPTS='--enable-shared' pyenv install 3.8.6
bundle install
```

#### 「 仕様 」

```markdown
・ 機械学習などを Ruby/Rails/TS などプロジェクトに組み込むための倉庫にします。
・ analyze フォルダは totolot から移動しました。
・ lean_rb フォルダは ruby で pycall を使い、データ分析をします。
```

### pylearn.py

> あかつきはかりうきものはなし あかつきばかり あきかせにたなひくくものたえまより あきのたのかりほのいほのとまをあらみ あくるまは あけぬるを あけぬれはくるるものとはしりなから あけぬれば あさちふのをののしのはらしのふれと あさほらけありあけのつきとみるまてに ... 風吹けば 香に匂ひける 高師の浜の 高砂の 鳥のそらねは 鳴きつる方を 鳴くや霜夜の 鳴く声に 鹿ぞ鳴くなる 黒髪の

```markdown
0 0.0 0.0 0.0 0.353553 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
1 0.0 0.0 0.0 0.000000 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
2 0.0 0.0 0.0 0.000000 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
3 0.0 0.0 0.0 0.000000 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
4 0.0 0.0 0.0 0.000000 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
.. ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ...
95 0.0 0.0 0.0 0.000000 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
96 0.0 0.0 0.0 0.000000 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
97 0.0 0.0 0.0 0.000000 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
98 0.0 0.0 0.0 0.000000 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
99 0.0 0.0 0.0 0.000000 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0

[100 rows x 780 columns]
```

### rblean_py.rb

```markdown
⚂ ⚂ ⚃ ⚁ ⚀ ⚀
```

_ランダムにサイコロを出力します_

### version.py

_pip3やsetuptoolsをアップグレードします_

```markdown
Requirement already up-to-date: pip in c:\python38\lib\site-packages (20.2.2)
CompletedProcess(args=['python', '-m', 'pip', 'install', '--upgrade', 'pip'], returncode=0, stderr='')
Requirement already up-to-date: pip in c:\python38\lib\site-packages (20.2.2)
Requirement already up-to-date: setuptools in c:\python38\lib\site-packages (49.6.0)
CompletedProcess(args=['python', '-m', 'pip', 'install', '-U', 'pip', 'setuptools'], returncode=0, stderr='')
3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)]
sys.version_info(major=3, minor=8, micro=5, releaselevel='final', serial=0)
```
