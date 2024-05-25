# ouchi-gpt-transapi-backend

「AI チャットアプリを作って学ぶアプリ開発」のバックエンド（Translate）部分です。

## 環境準備

### 仮想環境

仮想環境で実行する場合は以下です。

```bash
python -m venv .venv
. bin/activate
```

### ライブラリ

```bash
pip install -r requirements.txt
```

### ネットワーク

外部ネットワークに接続している必要があります。

## 実行

以下コマンドにてポート 8080 番で起動します。

```bash
python uvicorn main:app --host 0.0.0.0 --port 8080
```
