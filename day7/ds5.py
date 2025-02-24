# In a np array of spendings of the week, find the highest spending and the day.

import numpy as np
week_spendings = np.array([50, 120, 30, 40, 200, 90, 300])
index = 1
big_spending = week_spendings[0]
index = np.argmax(week_spendings)
days = {1:'mon', 2:'tue', 3:'wed', 4:'thus', 5:'fri', 6:'sat', 7:'sun'}
print(big_spending, days[index])

'''
for i in range(len(week_spendings)):
	if week_spendings[i] > big_spending:
		big_spending = week_spendings[i]
		index = i
        '''