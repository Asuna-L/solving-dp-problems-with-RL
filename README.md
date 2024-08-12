# Record for my _Reinforcement Learning Process_
  This project is my studying **dairy record**. I will share what I learn and write it here if time permitted. And definetely I will keep updating this journal.
  **Welcome any suggestions! Thank you all!**  
## 1.Tring to Use RL to Sovle basic Dp Problem

  - 1.1 Basic info for Reinforcement Learning

    - Reinforcement learning is a computational method in which a machine achieves its goals by interacting with the environment.
    - Designed to sovle Sequential Decision Making task. Agent need to resposible for the furture and make further decisions at a future point in time.
      ![image](https://github.com/user-attachments/assets/86edc2d5-6c83-43bd-b6b1-28324b591e26)
    - The agent has three key elements, namely `perception`( The agent perceives the state of the environment to some extent, and thus knows the current situation it is in) , `decision-making`(The process by which an agent calculates the actions it needs to take to achieve its goal based on its current state is called decision making) and `reward`(The environment generates a scalar signal as reward feedback based on the state and the actions taken by the agent).

    - A reinforcement learning need an agent that takes actions based on specific policy to achieve the goal and interact with the environment , and gets the feedback to estimate the value of specific action and state, thus optimizing its policy in next turn util it finds the best policy to achieve the goal.
    - basic elements:
        - _**agent**_:
          - `state space`
          - `action space`
          - `reward`
          - `state transition function`
          - `state-value function`
        - _**enviroment**_ :
          - The environment sampling the next state based on the current state and the action of the agent.
          - The probability distribution of the environment's state at the next moment will be jointly determined by the current state and the agent's action.

            $Next Stae$ ~  $P(.|Current State, Agent' Action)$
        - _**occupancy measure**_
  - 1.2 Stochastic Process & Marcov Decision Progress

  - 1.3 Two Basic Dynamic Programming Methods for MDP optimazation
      - Policy Iteration
      - Value Iteration 

  - 1.4 Temporal Difference methods for model-free Reinforcement learning
      - Monte-Carlo methods
      - Saras & n-step-Saras
      - Q-learning

  - 1.5 promote for this topic

> How to use it
1. Short Introduction
   I only upate my first 3 attempts to construct Envs for 3 classic dynamic programming problems like 0-1 Bag, House Robbery.
    - Qustion :
      1. _**House Robbery:**_
         A professional thief planned to steal from houses along the street. There was a certain amount of cash hidden in each house. The only factor that affected the thief's theft was that the adjacent houses were   equipped with interconnected anti-theft systems. _**If two adjacent houses were broken into by thieves on the same night, the system would automatically alarm .**_
         
         Given an array of non-negative integers ($[1,4,2,3,5]$ as example) representing the amount of money stored in each house nums , calculate the maximum amount that can be stolen in one night _**without setting off the alarm**_ .
      2. _**0-1 Bag:**_
        Given $n$ Items, The weight of the $ith$ item is $wgt[i]$, value is $val[i]$, and a capacity of Each item can only be selected once. The maximum value of the item that can be put into the backpack is limited.

        Take $wgt = [10,20,30,40,50]$, $val = [50,120,150,210,240]$, $cap = 50$ as example.
        ![image](https://github.com/user-attachments/assets/e915fa6a-5537-459c-92e0-b49b3b9d2ff9)
      3._**Cliff Walking**_
        Given a grid reprecenting the position, in which $****$ reprecenting the cliff and $EEEE$ reprecenting the destination. You are in the orign(upper left corner).Find the shortest methods to get to the destination.

        Take clos = $12$, rows = $4$ , cliff = $[3,1:10]$, destination = $[3,11]$
   
        ![image](https://github.com/user-attachments/assets/4eb8a4df-4dd6-4250-bc81-0dccd953aa70)

2. Parkage

   `Env` now has 3 enviroment that I constructed for the problem. Each need to contain property `action space`、`P` 、 `n` 、and `other elements` and function `createP` ,to creat Probability Transform Function with shape $P[state][action] = (p,next_state,reward,done)$, and `print_agent`, to print specific policy for problem.


        
      
      
         
    
