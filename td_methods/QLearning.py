from collections import defaultdict

import numpy as np
import random

from matplotlib import pyplot as plt
from tqdm import tqdm


class QLearning:
    def __init__(self, env, epsilon, alpha, gamma, n=1,ax = None):
        self.env = env
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.n = n
        self.Q = defaultdict(lambda: np.zeros(len(self.env.action)))
        self.Model = dict()

        self.ax = ax

    def take_action(self, state):
        if np.random.rand() <= self.epsilon:
            next_action = np.random.choice(len(self.env.action))
        else:
            next_action = np.argmax(self.Q[state])
        return next_action

    def q_learning(self, state, action, reward, next_state):
        self.Q[state][action] = self.Q[state][action] + self.alpha * (
                reward + self.gamma * self.Q[next_state].max() - self.Q[state][action]
        )

    def update(self, state, action, reward, next_state):
        self.q_learning(state, action, reward, next_state)
        self.Model[(state, action)] = (reward, next_state)
        for _ in range(self.n):
            (rnd_state, rnd_action), (rnd_reward, rnd_next_state) = random.choice(list(self.Model.items()))
            self.q_learning(rnd_state, rnd_action, rnd_reward, rnd_next_state)

    def train(self, episodes):
        return_list = []
        for epoch in range(10):
            with tqdm(total=int(episodes / 10), desc=f'Epoch: [{epoch}/{10}]') as pbar:
                for i in range(int(episodes / 10)):
                    episodes_return = 0
                    state = self.env.reset()
                    action = self.take_action(state)
                    done = False
                    while not done:
                        next_state, reward, done = self.env.step(action)
                        next_action = self.take_action(next_state)

                        self.update(state, action, reward, next_state)

                        state = next_state
                        action = next_action

                        episodes_return += reward
                    return_list.append(episodes_return)

                    if (i + 1) % 10 == 0:
                        pbar.set_postfix({
                            'episode': '{:d}'.format(int(episodes / 10 * epoch + i + 1)),
                            'return': '{:.3f}'.format(np.mean(return_list[-10:]))
                        })
                    pbar.update(1)
        Episodes = list(range(len(return_list)))
        if self.ax == None:
            plt.plot(Episodes, return_list, label = f'Q_learning n = {self.n}')
            plt.legend()
            plt.xlabel('Episodes')
            plt.ylabel('Return')
            plt.title('Q_learning on ' + self.env.name)
            plt.show()
        else:
            self.ax.plot(Episodes, return_list, label = f'Q_learning n = {self.n}')





