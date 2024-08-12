from abc import ABC, abstractmethod


class Env1(ABC):
    @property
    # need to contain
    # n: the numbers of the state
    # current state, like (x,y)
    # action : the set for action in state s shape : [state, action]
    # *reward : fix reward set
    # *other property like clos and rows

    @abstractmethod
    def step(self,*args,**kwargs):
        return []

    @abstractmethod
    def reset(self,*args,**kwargs):
        pass