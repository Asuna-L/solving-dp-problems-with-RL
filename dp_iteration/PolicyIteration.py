import copy
class PolicyIteration:
    def __init__(self,env,theta,gamma):
        self.env = env
        self.V = [0]*self.env.n
        self.Pi = [[1/len(self.env.action) for _ in self.env.action] for _ in range(self.env.n)]
        self.theta = theta
        self.gamma = gamma

    def policy_evaluation(self):
        cnt = 1  #Counter
        while True :
            derta = 0
            new_V = [0]* self.env.n
            for s in range(self.env.n):
                qsa_list = []
                for a in range(len(self.env.action)):
                    qsa = 0
                    for step in self.env.P[s][a]:
                        p, next_state,r,done = step
                        qsa += p * (r + self.gamma*self.V[next_state]*(1-done))
                    qsa_list.append(self.Pi[s][a] * qsa)
                new_V[s] = sum(qsa_list)
                derta = max( derta, abs(new_V[s] - self.V[s]))
            self.V = new_V
            if derta < self.theta:
                break
            cnt += 1
        print("Policy evaluation finish after %d iteration " % cnt)

    def policy_improvement(self):
        for s in range(self.env.n):
            qsa_list = []
            for a in range(len(self.env.action)):
                qsa = 0
                for k in self.env.P[s][a]:
                    p, next_state, r, done = k
                    qsa += p * (r + self.gamma * self.V[next_state] * (1 - done))
                qsa_list.append(qsa)
            max_q = max(qsa_list)
            cnt_q = qsa_list.count(max_q)

            self.Pi[s] = [1 / cnt_q  if q == max_q else 0 for q in qsa_list]
        print("Policy improvement finsh")
        return self.Pi

    def policy_iteration(self):
        while True :
            self.policy_evaluation()
            pre_pi = copy.deepcopy(self.Pi)
            pi = self.policy_improvement()
            if pre_pi == pi:
                break