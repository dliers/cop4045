import math
import matplotlib.pyplot as plt
# Function that will create x and y values and plots
def plot_function(fun_str, domain, ns):

    xmin = domain[0]
    xmax = domain[1]
    xs = []
    # Make the x values
    for i in range(ns):
        x = xmin + i * (xmax - xmin) / (ns - 1)
        xs.append(x)
        
    ys = []
    # Find the y values
    for x in xs:
        y = eval(fun_str)
        ys.append(y)
    # Print the values
    for i in range(ns):
        print(format(xs[i], "+.4f"), format(ys[i], "+.4f"))
    # Make the graph

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(fun_str)
    plt.plot(xs, ys)
    plt.show()

# Input Values
fun_str = input("Enter function with variable x: ")
ns = int(input("Enter number of samples: "))
xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))
domain = (xmin, xmax)
plot_function(fun_str, domain, ns)

