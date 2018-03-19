import requests

# 書籍「Pythonで体験するベイズ推論」の情報を国立国会図書館から取得
# ISBN:978-4-627-07791-1    検索時はハイフンを除去
api = "http://iss.ndl.go.jp/api/sru?operation=searchRetrieve&query=isbn=9784627077911"

info = requests.get(api)
print(info.status_code)
print(info.text)

# TODO: ISBNコードをパラメータ渡しにする。
# TODO: 結果がxml形式なので、必要情報のみ取り出すようにする。


