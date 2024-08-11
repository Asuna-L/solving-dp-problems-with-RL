from Env.env import Env
from dp_iteration.PolicyIteration import PolicyIteration
class HouseRobeerEnv(Env):
    def __init__(self, street):
        self.n = len(street) + 2
        self.r = street
        self.action = [2,3]
        self.P = self.createP() # P[state][action] = [(p, next_state, reward, done)]
    def createP(self):
        P = [[[] for j in range(2)] for i in range(self.n)]
        for s in range(self.n):
            for a in range(2):
                next_state =  s+ self.action[a]
                if next_state > self.n-1 :
                    reward = 0
                    done = True
                    next_state = self.n-1
                else :
                    reward = self.r[next_state-2]
                    done = False
                P[s][a] = [(1,next_state,reward,done)]
        return P

    def print_agent(self,agent, end=None):
        if end is None:
            end = [len(self.r),len(self.r)+1]
        print("State Value：")
        for s in range(agent.env.n):
            print('%6.6s' % ('%.3f' % agent.V[s]), end=' ')
        print()
        print("Policy")
        total_reward = 0
        s = 0
        print("-2 -> ", end='')
        while True:
            a = agent.Pi[s].index(max(agent.Pi[s]))
            for k in agent.env.P[s][a]:
                p, next_s, r, done = k
                s = next_s
                print("{} -> ".format(s - 2), end='')
                total_reward += r
            if s in end:
                print('End', end=' ')
                break
        print()
        print("The most cash can be stolen:{}".format(total_reward))

if __name__ == '__main__':
    street = [1,4,2,3,5]
    env = HouseRobeerEnv(street)
    theta = 0.001
    gamma = 1
    agent = PolicyIteration(env, theta, gamma)
    agent.policy_iteration()
    env.print_agent(agent)