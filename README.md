# 株式会社フィックスポイント　プログラミング試験問題

# 概要
プログラミング言語はPython3を用いました。
各フォルダ(task1, task2, task3, task4)ごとに各設問に対応するプログラムとログファイルを置いて実行しています。
実装した工夫として、今後のプログラムの拡張性を考慮し、データフレーム処理に特化したライブラリ（pandas）を導入しています。

詳細につきましては、各フォルダのREADMEにて記載していますので、そちらを参照してください。

# 動作環境の詳細
- Windows10
- Python 3.9.4
- pandas 1.2.4

# 使い方
### Githubからclone
Github上からソースコードをローカルPC上にcloneします。
```
$ git clone git@github.com:K-out-A/MonitoringSystem.git
```
cloneしたディレクトリ上に移動します。
```
$ cd MonitoringSystem
```

### 動作環境の構築
仮想環境を作成します。（そのまま実行すると既存のパッケージに干渉してエラーが起きる可能性があるためです。）
```
$ python3 -m venv myvenv
```
仮想環境を実行します。
```
$ source myvenv/bin/activate
```
必要なライブラリを仮想環境上にinstallします。（requirements.txtの中に必要なライブラリのリストが入っています。）
```
$ pip3 install -r requirements.txt
```

### ソースコードの実行
各設問ごとに以下のコード実行します。（例：設問1）

また、各設問ごとの変数はソースコード上で変更してください。
```
$ cd task1

$ python3 task1.py
```
