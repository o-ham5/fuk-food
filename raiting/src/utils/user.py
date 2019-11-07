from numpy import mean

class User:
    def __init__(self, name):
        self.name = name
        self.bias = 0
        self.variance = 1
        self.evals = dict()

    def add_eval(self, added_eval):
        self.evals.update(added_eval)

    def set_param(self, bias, variance):
        self.bias = bias
        self.variance = variance

    def __str__(self):
        return f'user {self.name} bias {self.bias} var {self.variance} num evals {len(self.evals)}'
