# TODO: 取得したxmlから必要な情報だけをDBに格納する。
import xml.etree.ElementTree as ET
tree = ET.parse('../references/api_result.xml')
root = tree.getroot()
print (root('version').text)
# TODO: DBの選択 MongoDBにしよう。
