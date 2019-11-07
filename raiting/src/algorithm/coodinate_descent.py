from numpy import mean
from tqdm import tqdm

def coodinate_descent(users, rests):
    N_ROOP = 100
    for roop in tqdm(range(N_ROOP)):
        for user in users:
            # update bias
            user.bias = mean(
                [eval_score - rest.esti_eval for rest, eval_score in user.evals.items()]
            )
            # update variance
            user.variance = mean(
                [(eval_score - (rest.esti_eval+user.bias)**2)
                 for rest, eval_score in user.evals.items()]
            )
            user.variance = max(user.variance, 1e-5)
        for rest in rests:
            # update eval
            tmp_a = sum((user.evals[rest] - user.bias)/user.variance for user in rest.user_set)
            tmp_b = sum(1/user.variance for user in rest.user_set)
            rest.esti_eval = tmp_a / tmp_b

