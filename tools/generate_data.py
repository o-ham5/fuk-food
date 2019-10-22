import pandas as pd
import numpy as np
import random
import string


def randomname(n):
    randlst = [random.choice(string.ascii_letters + string.digits)
               for i in range(n)]
    return ''.join(randlst)


# 管理者情報
super_users = [
    {
        'user_name': f'superuser{i:02d}',
        'email': f'superuser{i:02d}@e.com',
        'is_active': 1,
        'is_staff': 1,
        'is_admin': 1
    }
    for i in range(10)
]

super_users = pd.DataFrame(super_users)
super_users.to_csv('../api-db/init/super_users.csv')

# アカウント情報
accounts = [
    {
        'user_name': f'user{i:02d}',
        'email': f'user{i:02d}@e.com',
        'is_active': 1,
        'is_staff': 0,
        'is_admin': 0
    }
    for i in range(50)
]

accounts = pd.DataFrame(accounts)
accounts.to_csv('../api-db/init/accounts.csv')

# エリア情報
areas = [
    {
        'area_name': f'area_{i:02d}'
    }
    for i in range(30)
]

areas = pd.DataFrame(areas)
areas.to_csv('../api-db/init/areas.csv')

# ジャンル情報
genres = [
    {
        'genre_name': f'genre_{i:02d}'
    }
    for i in range(20)
]

genres = pd.DataFrame(genres)
genres.to_csv('../api-db/init/genres.csv')

# シチュエーション情報
situations = [
    {
        'situation_name': f'situation_{i:02d}'
    }
    for i in range(10)
]

situations = pd.DataFrame(situations)
situations.to_csv('../api-db/init/situations.csv')
