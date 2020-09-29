import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import random

data = pd.DataFrame(
	[['Control', 12.896613843672583],
    ['Control', 6.716642778724209],
    ['Control', 19.835786429431085],
    ['Control', 15.99262575562149],
    ['Control', 17.35535164079229],
    ['Control', 16.899936882913718],
    ['Control', 20.964225021714938],
    ['Control', 14.241776063991209],
    ['Control', 19.610959854462507],
    ['Control', 28.805999011427318],
    ['Control', 13.53181793061354],
    ['Control', 18.62595227984058],
    ['Control', 12.630163688642257],
    ['Control', 23.15530582621697],
    ['Control', 19.726519473848732],
	['Experimental', 5.130734063781696],
	['Experimental', 6.716642778724209],
    ['Experimental', 8.039528026099145],
	['Experimental', 4.7209770466430925],
    ['Experimental', 5.487865602666737],
	['Experimental', 7.080875337888015],
    ['Experimental', 3.457651652626209],
	['Experimental', 4.76655165489297],
    ['Experimental', 5.130734063781696],
	['Experimental', 6.4026453555496134],
    ['Experimental', 5.332639593248529],
	['Experimental', 9.36927644533533],
    ['Experimental', 5.591391986916058],
	['Experimental', 6.4376044910028964],
    ['Experimental', 7.120966915158945]],
	columns=['name', 'Time (s)'])

# print(data["Time (s)"].mean()) 
fig, ax = plt.subplots()

a = sns.boxplot(y="name", x="Time (s)", data=data)
a.set_xlabel("Time (s)",fontsize=18)
a.set_yticklabels(['Control', 'Experimental'], size = 15)
ax.set_ylabel('')
plt.show()

# for i in range(20):
#     print(random.uniform(2, 29))


<Icon-Camera />
