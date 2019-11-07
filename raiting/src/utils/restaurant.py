class Restaurant:
    def __init__(self, name):
        self.name = name
        self.esti_eval = 3.0
        self.user_set = set()

    def add_user(self, users):
        self.user_set |= {user for user in users if self in user.evals}

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return f'rest {self.name:} estimated {self.esti_eval}'
