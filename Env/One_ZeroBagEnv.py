from Env.env import Env
from dp_iteration.PolicyIteration import PolicyIteration

def idx(item):
    return sum([2 ** i for i in range(item)])


class OneZeroBagEnv(Env):
    def __init__(self, wgt, val, cap):
        assert len(wgt) == len(val)
        super(OneZeroBagEnv, self).__init__()
        self.wgt = wgt
        self.r = val
        self.n = sum([2 ** i for i in range(len(wgt))])

        self.left_cap = [cap] * self.n
        self.action = [0, 1]

        self.P = self.createP()

    def createP(self):
        P = [[[] for _ in self.action] for _ in range(self.n)]
        for item in range(len(self.wgt)):
            for s in range(2 ** item):
                for a in range(len(self.action)):
                    if item == len(self.wgt) - 1:
                        space = self.left_cap[idx(item) + s] >= self.wgt[item]
                        P[idx(item) + s][a] = [(1, idx(item) + s, self.r[item] * a * space, True)]
                        continue
                    next_item = min(len(self.wgt) - 1, item + 1)
                    next_s = 2*s + self.action[a]
                    next_state = idx(next_item) + next_s
                    space = self.left_cap[idx(item) + s] >= self.wgt[item]
                    self.left_cap[next_state] = (self.left_cap[idx(item) + s] - self.wgt[item] * a) if space \
                        else self.left_cap[idx(item) + s]
                    reward = self.r[item] * a * space + (space-1)*a*(100000)
                    done = False
                    if next_item == len(self.wgt) - 1:
                        done = True
                    P[idx(item) + s][a] = [(1, next_state, reward, done)]
        return P

    def print_agent(self, agent):
        print("State Value:")
        for item in range(len(self.wgt)):
            for s in range(2 ** item):
                print('%6.6s' % ('%.3f' % agent.V[idx(item)+s]), end=' ')
            print()

        print("Best Policy:")
        total_reward = 0
        s = 0
        cap = self.left_cap[0]
        item = []
        done = False
        while True:
            a = agent.Pi[s].index(max(agent.Pi[s]))
            if a : item.append(s)
            for k in agent.env.P[s][a]:
                p, next_s, r, process = k
                s = next_s
                done = process
                total_reward += r
                cap = self.left_cap[next_s]
            if done :
                print("I pick {} item with {} value in total, and left {} capability".format(item,total_reward,cap))
                print('End', end=' ')
                break
        print()


if __name__ == '__main__':
    wgt = [10, 20, 30, 40, 50]
    val = [50, 120, 150, 210, 240]
    cap = 50
    env = OneZeroBagEnv(wgt,val,cap)
    theta = 0.001
    gamma = 1
    agent = PolicyIteration(env, theta, gamma)
    agent.policy_iteration()
    env.print_agent(agent)

