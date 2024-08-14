from collections import defaultdict

import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

class Sarsa:
    def __init__(self,env, epsilon, alpha, gamma,n=1):
        self.env = env
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.Q = defaultdict(lambda : np.zeros(len(self.env.action)))
        self.n = n

        if self.n>1 :
            self.history_state = []
            self.history_action = []
            self.history_reward = []

    def take_action(self, state):
        if np.random.rand() <= self.epsilon:
            next_action = np.random.choice(len(self.env.action))
        else:
            next_action = np.argmax(self.Q[state])
        return next_action

    def update(self,state,action,reward,next_state,next_action,done):
        if self.n > 1:
            self.history_state.append(state)
            self.history_action.append(action)
            self.history_reward.append(reward)

            if len(self.history_state) == self.n:
                G = self.Q[next_state][next_action]
                for i in reversed(range(self.n)):
                    G = self.gamma * G + self.history_reward[i]
                    if done and i>0: # i > 0 make sure 0th state will not been update there
                        last_n_state = self.history_state[i]
                        last_n_action = self.history_action[i]

                        self.Q[last_n_state][last_n_action] = self.Q[last_n_state][last_n_action] + self.alpha*(
                                G - self.Q[last_n_state][last_n_action]
                        )
                update_state = self.history_state.pop(0)
                update_action = self.history_action.pop(0)
                self.history_reward.pop(0)
                # here update 0th state in history record
                self.Q[update_state][update_action] = self.Q[update_state][update_action] + self.alpha * (
                    G - self.Q[update_state][update_action]
                )
                if done:
                    self.history_state = []
                    self.history_action = []
                    self.history_reward = []

        else:
            self.Q[state][action] = self.Q[state][action] + self.alpha*(
                reward + self.gamma * self.Q[next_state][next_action] - self.Q[state][action]
            )

    def get_best_policy(self,state):
        maxQ = np.max(self.Q[state])
        best_action = np.zeros(len(self.env.action))
        for i in range(len(self.env.action)):
            if self.Q[state,i] == maxQ  : best_action[i] = 1
        return best_action

    def train(self,episodes = 500):
        return_list = []
        for epoch in range(10):
            with tqdm(total = int(episodes / 10),desc =f'Epoch: [{epoch}/{10}]') as pbar:
                for i in range(int(episodes/10)):
                    episodes_return = 0
                    state = self.env.reset()
                    action = self.take_action(state)
                    done = False
                    while not done:
                        next_state, reward, done = self.env.step(action)
                        next_action = self.take_action(next_state)

                        self.update(state,action,reward,next_state,next_action,done)

                        state = next_state
                        action = next_action

                        episodes_return += reward
                    return_list.append(episodes_return)

                    if (i + 1) % 10 == 0:
                        pbar.set_postfix({
                            'episode': '{:d}'.format(int(episodes / 10* epoch + i+ 1)),
                            'return': '{:.3f}'.format(np.mean(return_list[-10:]))
                        })
                    pbar.update(1)

        Episodes = list(range(len(return_list)))
        plt.plot(Episodes,return_list)
        plt.xlabel('Episodes')
        plt.ylabel('Return')
        plt.title('Saras on ' + self.env.name)
        plt.show()





