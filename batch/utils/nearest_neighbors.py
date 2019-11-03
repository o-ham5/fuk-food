import MySQLdb
import numpy as np
from datetime import datetime
from annoy import AnnoyIndex
from sklearn.preprocessing import StandardScaler
import time


# データベースへの接続とカーソルの生成
def job_knn():
    start = time.time()
    print("####### job_knn start!! ########")
    connection = MySQLdb.connect(
        host='172.20.0.14',
        # host='127.0.0.1',
        user='fuk',
        passwd='fuk',
        db='api-db')
    cursor = connection.cursor()

    # 一度全てのレコードを削除
    sql = "TRUNCATE neighborhoods"
    cursor.execute(sql)

    # アカウント情報を取得し、各種特徴量を取得する。
    sql = "SELECT account_id, username, bias, variance, inyou, oshare, shokuji, setsuyaku FROM accounts"
    cursor.execute(sql)
    accounts = []
    for row in cursor:
        accounts.append(row)
    data = np.array(accounts)[:, 2:]
    data = data.astype(np.float32)
    # 標準化
    scaler = StandardScaler()
    scaler.fit(data)
    data = scaler.transform(data)

    query = data
    # KNNの実行
    t = AnnoyIndex(data.shape[1], "euclidean")
    for i, v in enumerate(data):
        t.add_item(i, v)

    t.build(10)  # 10 trees
    result = []
    dists = []
    for i, v in enumerate(query):
        r, d = t.get_nns_by_vector(v, 4, include_distances=True)
        result.append(r)
        dists.append(d)
    print(np.array(result))
    print(np.array(dists))

    # 結果をバルクで挿入する
    sql = "INSERT INTO neighborhoods (target, first, second, third, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)"
    params = []
    for idx in result:
        params.append([accounts[idx[0]][0], accounts[idx[1]][0],
                       accounts[idx[2]][0], accounts[idx[3]][0], datetime.now(), datetime.now()])

    cursor.executemany(sql, params)
    connection.commit()
    cursor.close()
    connection.close()

    elapsed_time = time.time() - start
    print("####### job_knn finished!! ########")
    print("time elapsed:{0}".format(elapsed_time) + "[sec]")


# job_knn()
