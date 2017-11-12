import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)
plt.xlabel('value',fontsize=14)
plt.ylabel('squares of value', fontsize=14)
plt.title('Square Numbers',fontsize=14)

plt.tick_params(axis='both',labelsize=14,labelcolor='red')

plt.show()

