import CliffWalking, HouseRobeer, One_ZeroBagEnv
import CliffWalking2
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
    env.reset()
    print(env.step(3))
