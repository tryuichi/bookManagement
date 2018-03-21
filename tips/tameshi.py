from pyndlsearch.client import SRUClient
from pyndlsearch.cql import CQL


if __name__ == '__main__':
    # CQL検索クエリの組み立て
    cql = CQL()
    cql.isbn = '9784627077911'
    #print(cql.payload())

    # NDL Searchクライアントの設定
    client = SRUClient(cql)
    client.set_maximum_records(1)
    #print(client)
    
    # get_response()ではxml形式で取得可能
    #res = client.get_response()
    #print(res.text)

    # SRU
    srres = client.get_srresponse()

    for record in srres.records:
        print(record.recordData.title)
        print(record.recordData.creator)
        print(record.recordData.publisher)
