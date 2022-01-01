# 概要

## 使用するライブラリのインストール

※ ubuntu 20.04 の使用を想定しています

1. curl をインストールする

`sudo apt install curl`

2. poetry をインストールする

`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3`

3. PATH を通す

`source $HOME/.poetry/env`

4. パッケージをインストールする

`poetry install`

## 起動コマンド

アプリの設定  
`export FLASK_APP=app.py`  

環境の設定  
`export FLASK_ENV=development`  

実行  
`poetry run flask run`
