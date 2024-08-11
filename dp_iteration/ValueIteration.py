class ValueIteration:
    def __init__(self, env, theta, gamma):
        self.env = env
        self.v = [0] * self.env.n
        self.theta = theta
        self.gamma = gamma
        self.pi = [None for i in range(self.env.n)]

    def value_iteration(self):
        cnt = 0
        while True:
            max_diff = 0
            new_V = [0] * self.env.n
            for s in range(self.env.n):
                qsa_list = []
                for a in range(len(self.env.Action)):
                    qsa = 0
                    for res in self.env.P[s][a]:
                        p, next_state, r, done = res
                        qsa += p * (r + self.gamma * self.v[next_state] * (1 - done))
                    qsa_list.append(qsa)
                new_V[s] = max(qsa_list)
                max_diff = max(max_diff, abs(new_V[s] - self.v[s]))
            self.v = new_V
            if max_diff < self.theta:
                break
            cnt += 1
        print("ValueIteration go through %d epoch" % cnt)
        self.get_policy()

    def get_policy(self):
        for s in range(self.env.nrow * self.env.ncol):
            qsa_list = []
            for a in range(4):
                qsa = 0
                for res in self.env.P[s][a]:
                    p, next_state, r, done = res
                    qsa += p * (r + self.gamma * self.v[next_state] * (1 - done))
                qsa_list.append(qsa)
            maxq = max(qsa_list)
            cntq = qsa_list.count(maxq)
            self.pi[s] = [1 / cntq if q == maxq else 0 for q in qsa_list]