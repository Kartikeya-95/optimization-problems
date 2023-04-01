<b>Optimization Problem to maximize the production of goods in a factory</b>
-----------------------------------------------------------------------------------------------------------------------------------------------------------
There are 4 machines that are operational in a factory and we have to maximize the overall production during the next 10 hours after the production starts.\
The objective function of our problem is-\
$$Z = max\sum_{m}\sum_{t}x_{m,t} \text{ s.t. } 0\le x_{m,t} \le 10 $$
$$\text{ where } x_{m,t} \text{ represents the production quantity of machine m at hour t.} $$
Some machines have dependencies on others and the constraints are (for each t)
$$2x_{2,t}-8x_{3,t} \le 0$$
$$x_{2,t}-2x_{3,t-2}+x_{4,t} \ge 1 $$
And the capacity production is given by (for all t)
$$\sum_{m}x_{m,t} \le 50 $$
$$x_{1,t}+x_{2,t-1}+x_{3,t}+x_{4,t} \le 10 $$
<b>Solve the problem and find the optimal production for each machine for each hour during 10 consecutive hours.</b>

Note: x<sub>2,t-1</sub> in the last constraint , represents the second machine at hour t-1\
Second and Fourth constraints does not exists for t<3 and t<2 respectively
