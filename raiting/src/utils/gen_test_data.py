from numpy.random import rand, randint, randn

# setting
user_data_path = '../../storage/test_user_data.txt'
rest_data_path = '../../storage/test_rest_data.txt'
eval_data_path = '../../storage/test_eval_data.txt'
n_user = 100
n_rest = 10000
n_eval = 0.2 * n_user * n_rest

# setting user data
users = {
    user_ix: {
        'bias': 4*rand()-2,  # (-2, 2)
        'variance': 2*rand()  # (0, 2)
    }
    for user_ix in range(n_user)
}

# setting rest data
rests = {
    rest_ix: {
        'true_eval': 5*rand()  # (0, 5)
    }
    for rest_ix in range(n_rest)
}

# generate evals
evals = set()
with open(eval_data_path, 'w') as f:
    while len(evals) < n_eval:
        user_ix = randint(n_user)
        rest_ix = randint(n_rest)
        if (user_ix, rest_ix) in evals:
            continue
        user = users[user_ix]
        rest = rests[rest_ix]
        normal_sampling = randn()
        eval_sampling = user['variance'] * normal_sampling + (rest['true_eval'] + user['bias'])
        print(user_ix, rest_ix, eval_sampling, file=f)
        evals.add((user_ix, rest_ix))

with open(user_data_path, 'w') as f:
    for user_ix in range(n_user):
        user = users[user_ix]
        print(user_ix, user['bias'], user['variance'], file=f)

with open(rest_data_path, 'w') as f:
    for rest_ix in range(n_rest):
        rest = rests[rest_ix]
        print(rest_ix, rest['true_eval'], file=f)

print('save as', eval_data_path)
print('save as', user_data_path)
print('save as', rest_data_path)
