# レイティングアルゴリズム検証用

**目的**

ユーザーがレストランに与えた評価集合を元に, レストランの真の価値を推定する



**ディレクトリ構造**

```
├── src
│   ├── algorithm
│   │   ├── __init__.py
│   │   └── coodinate_descent.py
│   ├── run.py
│   ├── setting.py
|   ├── varidation.py
│   └── utils
│       ├── gen_test_data.py
│       ├── restaurant.py
│       └── user.py
├── result
│   ├── cd_rest_data.txt
│   └── cd_user_data.txt
└── storage
    └── eval_data.txt
```



+ `run.py` レイティング関数実行用
+ `varidation.py` 推定結果検証用 (実行方法はusageを参照)
+ `setting.py`  どのeval_dataを使用するかを指定する

<br>

## コンペに参加する人へ

storageディレクトリに3種類のデータを入れています

+ eval_data_mini.txt (デバッグ用) (user 5, rest 10)
+ eval_data_mini2.txt (デバッグ用) (user 20, rest 100)
+ eval_data.txt (本番用) (user 100, rest 10000)

`setting.py`でどのデータを読み込んで`run.py`を動かすかを設定できます.

下記のレイティング関数追加方法を参考に, 自作関数をalgorithmディレクトリに追加していってください. `utils/gen_test_data.py`を実行すると, 新しくeval_data.txtを生成できます. (どのようにeval_dataが作成されているかも見ることができます)



<br>

## レイティング関数追加方法

+ users, restsを引数とする関数を作成し, algorithmにスクリプトとして追加

  > algorithm/coodinate_descent.pyを参考にしてください

+ `algorithm/__init__.py`に関数情報を追加

  > 書き方は中身を見てください

+ `run.py`に情報を追加
  + from algorithm import に関数名を追加
  + プログラム上部, algorithm 辞書に情報を追加

+ `run.py`を実行するときに`-a 関数名`で実行すれば動き, 実行結果は`result`フォルダに格納されます

<br>