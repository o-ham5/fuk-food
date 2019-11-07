from argparse import ArgumentParser
import setting
from utils.user import User
from utils.restaurant import Restaurant
from algorithm import (
    coodinate_descent
)

algorithm = {
    'coodinate_descent': {
        'func': coodinate_descent,
        'prefix': 'cd'
    }
}

def main():
    users, rests = read_eval_datas()

    # 評価値推測アルゴ
    algo = algorithm[args.algorithm]['func']
    algo(users, rests)

    # 結果の書き出し
    prefix = algorithm[args.algorithm]['prefix']
    write_esti(users, rests, prefix=prefix)


def read_eval_datas():
    users = dict()
    rests = dict()

    eval_data_path = setting.eval_data_path
    with open(eval_data_path, 'r') as f:
        for line in f.readlines():
            user_ix, rest_ix, eval_score = line.strip().split()
            user_ix = int(user_ix)
            rest_ix = int(rest_ix)
            eval_score = float(eval_score)

            if user_ix in users:
                user = users[user_ix]
            else:
                user = User(user_ix)
                users[user_ix] = user

            if rest_ix in rests:
                rest = rests[rest_ix]
            else:
                rest = Restaurant(rest_ix)
                rests[rest_ix] = rest

            user.add_eval({rest: float(eval_score)})
            rest.add_user({user})

    return set(users.values()), set(rests.values())


def write_esti(users, rests, prefix=''):
    # user
    esti_user_data_path = f'{setting.RESULT_DIR}/{prefix}_user_data.txt'
    esti_rest_data_path = f'{setting.RESULT_DIR}/{prefix}_rest_data.txt'
    with open(esti_user_data_path, 'w') as f:
        for user in sorted(list(users), key=lambda u: u.name):
            print(user.name, user.bias, user.variance, file=f)
    # rest
    with open(esti_rest_data_path, 'w') as f:
        for rest in sorted(list(rests), key=lambda r: r.name):
            print(rest.name, rest.esti_eval, file=f)
    print('save as', esti_user_data_path)
    print('save as', esti_rest_data_path)


def argparser():
    parser = ArgumentParser()
    parser.add_argument(
        '-a', '--algorithm',
        choices=list(algorithm),
        default='coodinate_descent',
    )
    return parser


if __name__ == '__main__':
    parser = argparser()
    args = parser.parse_args()

    print('[ algorithm ]')
    print(args.algorithm)

    main()

