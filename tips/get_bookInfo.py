import requests

# 書籍「Pythonで体験するベイズ推論」の情報を国立国会図書館から取得
# ISBN:978-4-627-07791-1    検索時はハイフンを除去
api = "http://iss.ndl.go.jp/api/opensearch?isbn=9784627077911"

info = requests.get(api)

# TODO: 取得したxmlが一部サニタイズされたままで情報抽出できない。変換できるツール探す。
from xml.sax.saxutils import unescape
print(unescape(info.text, entities={"&quot;":'"'}))

info_file = open('../references/api_result_escaped.xml', 'w')
info_file.write(unescape(info.text, entities={"&quot;":'"'}))
info_file.close()

# TODO: ISBNコードをパラメータ渡しにする。
# TODO: 結果がxml形式なので、必要情報のみ取り出すようにする。


