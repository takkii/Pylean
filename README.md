[![GitHub release](https://img.shields.io/github/release/takkii/Pylean.svg?style=flat)](GitHub)[![GitHub Status](https://img.shields.io/github/last-commit/takkii/Pylean.svg?style=flat)](GitHub)

### Pylean はデータ分析用のプロジェクトです

今後はデータ分析を記録していきます。自前で、できることを集約します。

##### 「 環境構築 」

```markdown
環境構築、基本。
pyenv, anaconda3-2020.11
pip3 install -r requirements.txt

lean_rbフォルダ内環境構築。
env PYTHON_CONFIGURE_OPTS='--enable-shared' pyenv install 3.8.8
bundle install
```

#### 「 仕様 」

```markdown
・ 機械学習の分析結果を、プロジェクトに組み込むための保管庫にします。
・ analyzeフォルダは、totolotから移動しました。
・ lean_rbフォルダは、rubyでpycallを使いデータ分析をします。
```
