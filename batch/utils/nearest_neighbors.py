import MySQLdb
import numpy as np
from datetime import datetime
import faiss
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

    query = data
    # KNNの実行
    index = faiss.IndexFlatL2(data.shape[1])   # build the index
    index.add(data)                  # add vectors to the index
    dists, result = index.search(query, k=4)     # actual search
    print(result)

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
