import numpy as np
import matplotlib.pyplot as plt
import CliffWalking, HouseRobeer, One_ZeroBagEnv
import CliffWalking2
from td_methods.Sarsa import Sarsa
from td_methods.QLearning import QLearning

def make(env:str, *args,**kwargs):
    if env == 'CliffWarking_v0':
        return CliffWalking.CliffWalkingEnv(*args,**kwargs)
    elif env == 'CliffWarking_v1':
        return CliffWalking2.CliffWalkingEnv(*args,**kwargs)
    elif env == 'HouseRobeer_v0':
        return HouseRobeer.HouseRobeerEnv(*args,**kwargs)
    elif env == 'One_ZeroBag_v0':
        return One_ZeroBagEnv.OneZeroBagEnv(*args,**kwargs)


if __name__ == '__main__':
    ncol = 12
    nrow = 4
    env = make('CliffWarking_v1',ncol,nrow)
    np.random.seed(0)
    epsilon = 0.01
    alpha = 0.1
    gamma = 0.9
    fig,ax = plt.subplots()
    for n in [0,2,20]:
        agent = QLearning(env,epsilon,alpha,gamma,n=n,ax=ax)
        agent.train(episodes=300)

    plt.xlabel('Episodes')
    plt.ylabel('Return')
    plt.title('Qlearning on Cliff Walking')
    plt.legend()
    plt.show()