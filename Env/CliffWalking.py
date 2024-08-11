from dp_iteration import PolicyIteration as robot
from env import Env
class CliffWalkingEnv(Env):
    def __init__(self, ncol = 12, nrow= 4):
        super(CliffWalkingEnv, self).__init__()
        self.ncol = ncol
        self.nrow = nrow
        self.n = self.ncol * self.nrow
        self.action = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        self.P = self.createP()

    def createP(self):
        P = [[[] for j in range(4)] for i in range(self.n)]

        for i in range(self.nrow):
            for j in range(self.ncol):
                for a in range(len(self.action)):
                    if i == self.nrow - 1 and j > 0:
                        P[i * self.ncol + j][a] = [(1, i * self.ncol + j, 0, True)]
                        continue
                    next_x = min(self.ncol - 1, max(0, j + self.action[a][0]))
                    next_y = min(self.nrow - 1, max(0, i + self.action[a][1]))
                    next_state = next_y * self.ncol + next_x
                    reward = -1
                    done = False

                    if next_y == self.nrow - 1 and next_x > 0:
                        done = True
                        if next_x != self.ncol - 1:
                            reward = -100
                    P[i * self.ncol + j][a] = [(1, next_state, reward, done)]
        return P

    def print_agent(slef, agent, action_meaning=None, disaster=None, end=None):
        if end is None:
            end = []
        if disaster is None:
            disaster = []
        if action_meaning is None:
            action_meaning = ['^', 'v', '<', '>']
        print("State Value:")
        for i in range(slef.nrow):
            for j in range(slef.ncol):
                print('%6.6s' % ('%.3f' % agent.V[i * agent.env.ncol + j]), end=' ')
            print()

        print("Policy：")
        for i in range(slef.nrow):
            for j in range(slef.ncol):
                if (i * slef.ncol + j) in disaster:
                    print('****', end=' ')
                elif (i * slef.ncol + j) in end:
                    print('EEEE', end=' ')
                else:
                    a = agent.Pi[i * slef.ncol + j]
                    pi_str = ''
                    for k in range(len(action_meaning)):
                        pi_str += action_meaning[k] if a[k] > 0 else 'o'
                    print(pi_str, end=' ')
            print()

if __name__ == '__main__':
    env = CliffWalkingEnv()
    action_meaning = ['^', 'v', '<', '>']
    theta = 0.001
    gamma = 0.9
    agent = robot.PolicyIteration(env, theta, gamma)
    agent.policy_iteration()
    env.print_agent(agent, action_meaning, list(range(37, 47)), [47])


