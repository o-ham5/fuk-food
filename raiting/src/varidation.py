from sys import argv
import setting
from numpy import mean


def usage():
    print(f'python {__file__} user_data.txt(esti) rest_data.txt(esti)')

def main(esti_user_data_path, esti_rest_data_path):
    real_user_data = read_user_data(setting.user_data_path)
    real_rest_data = read_rest_data(setting.rest_data_path)

    esti_user_data = read_user_data(esti_user_data_path)
    esti_rest_data = read_rest_data(esti_rest_data_path)

    bias_errors, variance_errors = stat_user(real_user_data, esti_user_data)
    eval_errors = stat_rest(real_rest_data, esti_rest_data)

    print('[ user ]')
    print('mean bias error', mean(bias_errors))
    print('mean vari error', mean(variance_errors))
    print('[ rest ]')
    print('mean eval error', mean(eval_errors))

def read_user_data(file_path):
    user_data = dict()
    with open(file_path, 'r') as f:
        for line in f.readlines():
            user_ix, bias, variance = line.strip().split()
            user_data[int(user_ix)] = {
                'bias': float(bias),
                'variance': float(variance)
            }
    return user_data

def read_rest_data(file_path):
    rest_data = dict()
    with open(file_path, 'r') as f:
        for line in f.readlines():
            rest_ix, true_eval = line.strip().split()
            rest_data[int(rest_ix)] = {
                'true_eval': float(true_eval)
            }
    return rest_data

def stat_user(real_user_data, esti_user_data):
    bias_errors = []
    variance_errors = []
    for user_ix in esti_user_data:
        if user_ix not in real_user_data:
            continue
        esti_user = esti_user_data[user_ix]
        real_user = real_user_data[user_ix]
        bias_error = esti_user['bias'] - real_user['bias']
        vari_error = esti_user['variance'] - real_user['variance']
        bias_errors.append(bias_error)
        variance_errors.append(vari_error)

    return bias_errors, variance_errors


def stat_rest(real_rest_data, esti_rest_data):
    eval_errors = []
    for rest_ix in esti_rest_data:
        if rest_ix not in real_rest_data:
            continue
        esti_rest = esti_rest_data[rest_ix]
        real_rest = real_rest_data[rest_ix]
        eval_error = esti_rest['true_eval'] - real_rest['true_eval']
        eval_errors.append(eval_error)

    return eval_errors

if __name__ == '__main__':
    if len(argv) != 3:
        usage()
    else:
        main(*argv[1:])

