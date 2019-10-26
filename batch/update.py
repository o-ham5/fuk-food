import MySQLdb
import numpy as np
from numpy import mean, isnan
import pandas as pd
from random import randint
from tqdm import tqdm

import schedule
import time


class Spot:
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.evaluated_score = None
        self.account_list = []

    def update_evaluated_score(self):
        if not self.account_list:
            return
        tmp_a = sum((float(account.evals[self]) - float(account.bias)) /
                    account.variance for account in self.account_list)
        tmp_b = sum(1/account.variance for account in self.account_list)
        self.evaluated_score = tmp_a / tmp_b

    def set_judge_list(self, accounts):
        self.account_list = [
            account for account in accounts if self in account.evals]

    def get_spot_id(self):
        return self.spot_id

    def get_evaluated_score(self):
        return self.evaluated_score

    def __repr__(self):
        return f'spot_id {self.spot_id:} estimated {self.evaluated_score} {self.account_list}'


class Account:
    def __init__(self, account_id, bias, variance, evals):
        self.account_id = account_id
        self.bias = None
        self.variance = None
        self.evals = evals

    def update_bias(self):
        self.bias = mean([float(eval_score) - float(spot.evaluated_score)
                          for spot, eval_score in self.evals.items()])

    def update_variance(self):
        self.variance = mean([(float(eval_score) - float(spot.evaluated_score))**2 for spot,
                              eval_score in self.evals.items()]) - self.bias ** 2
        self.variance = max(self.variance, 1e-5)

    def add_eval(self, added_eval):
        self.evals.update(added_eval)

    def set_param(self, bias=0, variance=1):
        self.bias = bias
        self.variance = variance

    def get_account_id(self):
        return self.account_id

    def get_bias(self):
        return self.bias

    def get_variance(self):
        return self.variance

    def __repr__(self):
        return f'account {self.account_id} bias {self.bias} var {self.variance} num evals {len(self.evals)}'


def job():
    # データベースへの接続とカーソルの生成
    connection = MySQLdb.connect(
        host='172.20.0.14',
        user='fuk',
        passwd='fuk',
        db='api-db')
    cursor = connection.cursor()

    # 口コミデータを全て取得する
    sql = "SELECT spot, account, score FROM rest_kuchikomi"
    cursor.execute(sql)
    kuchikomis = []
    for row in cursor:
        kuchikomis.append(row)
    kuchikomis = np.array(kuchikomis)

    # 口コミ対象のスポットを全て取得する
    sql = "SELECT spot_id, evaluated_score FROM spots"
    cursor.execute(sql)
    spots = []
    spots_dict = dict()
    for row in cursor:
        spot = Spot(row[0])
        spots.append(spot)
        spots_dict[str(row[0])] = spot

    # 口コミを投稿したアカウントのリストを取得する。
    accounts = []
    account_ids = np.unique(kuchikomis[:, 1])
    for account_id in account_ids:
        sql = f"SELECT bias, variance FROM accounts WHERE account_id = '{account_id}'"
        cursor.execute(sql)
        account_kuchikomi = kuchikomis[kuchikomis[:, 1] == account_id]
        for row in cursor:
            account = Account(account_id, row[0], row[1], {
                spots_dict[ak[0]]: ak[2] for ak in account_kuchikomi})

        accounts.append(account)

    for spot in spots:
        spot.evaluated_score = 3
        spot.set_judge_list(accounts)
    for account in accounts:
        account.set_param()

    num_roop = 10000
    for _ in tqdm(range(num_roop)):
        for account in accounts:
            account.update_bias()
            account.update_variance()
        for spot in spots:
            spot.update_evaluated_score()

    for spot in spots:
        sql = f"UPDATE spots SET evaluated_score = {spot.get_evaluated_score()} WHERE spot_id = {spot.get_spot_id()}"
        cursor.execute(sql)

    for account in accounts:
        sql = f"UPDATE accounts SET bias = {account.get_bias()}, variance = {account.get_variance()} WHERE account_id = '{account.get_account_id()}'"
        cursor.execute(sql)

    connection.commit()
    cursor.close()
    connection.close()


# 毎時間ごとにjobを実行
schedule.every(5).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
