# TODO: 取得したxmlから必要な情報だけをDBに格納する。
import xml.etree.ElementTree as ET
tree = ET.parse('../references/api_result_escaped_01.xml')
root = tree.getroot()

# 書名はなんと、root[4][0][2][0][0].text で取得できた。
print(root[4][0][2][0][0].text)
print(root[4][0][2][0][1].text)
print(root[4][0][2][0][3].text)

# TODO: 
# TODO: DBの選択 MongoDBにしよう。
