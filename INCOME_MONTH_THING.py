month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "your Birthday")

profits = (20000,45000,78000,97000,120000,456000,540000,650000,1000000,3000000,7000000,9000000,11000000)

max_profit = max(profits)
max_profit_index = profits.index(max_profit)
print(max_profit_index)

max_profit_month = month[max_profit_index]
print("The maximum profit of " + str(max_profit)+ " was recorded in the month of " + str(max_profit_month))

min_profit = min(profits)
min_profit_index = profits.index(min_profit)
print(min_profit_index)

min_profit_month = month[min_profit_index]
print( "The minimum profit of "+str(min_profit)+" was recorded in the month of "+str(min_profit_month))