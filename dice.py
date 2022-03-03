import random
import plotly.express as px
import plotly.figure_factory as ff

diceResult = []
countList = []

for i in range(0,100):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    diceResult.append(die1+die2)
    countList.append(i)
fig = ff.create_distplot([diceResult], ['countList'])
fig.show()



