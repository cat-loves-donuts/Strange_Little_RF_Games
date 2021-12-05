# You know how the snake games working.....

**The original creator of this game and agent is python-engineer: https://github.com/python-engineer/snake-ai-pytorch**

**If you are interested in how to make this game and RL agent, please go to python-engineer's Youtube channel...**

This is a basic snake game with an DQN agent.

Pyhon and Packages it using: 
```
python==3.8 
pygame==2.1.0
torch==1.7.1
IPyhon==7.30.0
matplotlib==3.5.0
```

**1. One day, when I was watching agent playing this game...**

You know what, the most charming part for me is to observe the moment that agent find the solution.

It is so stange.... I am not sure whether this is because of the RL strategy we used, the agnet know how to play the game in a sudden after 90 iterations...

Before 80~90 ierations, the agent can only get like 3 or 4 points in a round. But suddenly, it can get 14 points.... And after it, it know how to play...

What happend on earth in that iteration.....


**2. One day, when I was plaing with this little toy. I am wondering....**

You know when we using DQN, mostly, we set the reward as [-1, 1] or [0, 1] for neigative and positive movement results. Or some bigger values which can be normalized to this range.

I am thinking what if the difference of reward getting bigger?

Well, it turns out that with bigger difference, it is more difficult for agent to find the proper solution or movements.
For observation, it need more iterations to find a proper solution to get more points....


**3. One day, after I finished some Leetcode algorithm quize....**

Well, you know, when people had a very terrible experience (I mean after you get suffering on Leetcode), you will definately want to play some little games. You know.... for fun.

I choose to **watch** agent play games... But this time I added some barriers in the game.
One more terrible thing is that, The food can be geberated on the some point with the barrier...

Well, it indeed take more iterations for agent to learn how to play this game.

**But**, when the food generated on the same point as barriers... The snake choose to hit on the barriers sometimes...

Of course it will hit on the barriers, because it want to eat the food.....




