import matplotlib.pyplot as plot

from random_walk import RandomWalk

while 1:
	rw = RandomWalk(50000)
	rw.fill_walks()
	point_numbers = list(range(rw.num_points))
	
	plot.scatter(rw.x_values,rw.y_values,c=point_numbers, cmap=plot.cm.Blues,edgecolors='none',s=10)
	plot.scatter(0, 0, c='green', edgecolors='none',s=100)
	plot.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
	
	plot.axes().get_xaxis().set_visible(False)
	plot.axes().get_yaxis().set_visible(False)
	plot.show()
	
	stop = raw_input('input q for quit: ')
	
	if stop == 'q':
		break