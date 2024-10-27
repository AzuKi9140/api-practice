# api-practice

ゼミで使用するリポジトリです。

[Python ではじめる数理最適化](https://www.amazon.co.jp/dp/B09G9VZ4PH) の 6 章のためのリポジトリです。
上記の本の公式リポジトリは [こちら](https://github.com/ohmsha/PyOptBook) です。

## 開発環境構築

```bash
git clone https://github.com/AzuKi9140/api-practice.git
```

- `main` からブランチを切って作業してください。
- デフォルトブランチの `main` へ PR を作成してください。

## ローカルでの実行方法

- パッケージのインストール（初回のみ）

  `pipenv` がインストールされていない場合はインストールする

  ```bash
  pipenv install
  ```

### 最適化問題の実行

- 最適化問題を解く
  ```bash
  pipenv run problem
  ```

### Flask での実行

1. Flask を起動

   ```bash
   pipenv run flask
   ```

2. リクエストを送信

   ```bash
    pipenv run curl_post
   ```

3. ブラウザで確認

   下記の URL にアクセスしてください。

   ```bash
   http://127.0.0.1:5000/
   ```

   入力するデータは、`resources` ディレクトリにある `students.csv` と `cars.csv` です。
