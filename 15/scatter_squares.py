import matplotlib.pyplot as plot
import random
#x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
#y_values = [random.choice(list(range(0,x)))**2 for x in x_values]
#print y_values
plot.scatter(x_values, y_values, s=10, c=y_values,cmap=plot.cm.Blues)
#plot.plot(x_values,y_values)
plot.title('square numbers', fontsize=12)
plot.xlabel('valut',fontsize=4)
plot.ylabel('square of value', fontsize=4)

plot.tick_params(axis='both', which='major',labelsize=4)
plot.axis([0,1100,0,1100000])
plot.savefig('1.png',bbox_inches='tight')
plot.show()
