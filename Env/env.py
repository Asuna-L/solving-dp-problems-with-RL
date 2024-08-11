from abc import ABC, abstractmethod


class Env(ABC):
    @property
    # need to contain
    # n: the numbers of the state
    # action : the set for action in state s shape : [state, action]
    # *reward : fix reward set
    # *other property like clos and rows

    @abstractmethod
    def createP(self):
        return []

    @abstractmethod
    def print_agent(self,**kwargs):
        pass
