from env1 import Env1


class CliffWalkingEnv(Env1):
    def __init__(self, ncol, nrow):
        # parameters
        self.nrow = nrow
        self.ncol = ncol

        #current state
        self.x = 0
        self.y = self.nrow - 1

        self.action = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        self.reward = -1

    def step(self, a):

        self.x = min(self.ncol - 1, max(0, self.x + self.action[a][0]))
        self.y = min(self.nrow - 1, max(0, self.y + self.action[a][1]))

        next_state = self.y * self.ncol + self.x
        reward = self.reward
        done = False
        if self.y == self.nrow - 1 and self.x > 0:
            done = True
            if self.x != self.ncol - 1:
                reward = -100
        return next_state, reward, done

    def reset(self):
        self.x = 0
        self.y = self.nrow - 1
        return self.y * self.ncol + self.x
