import math
import matplotlib.pyplot as plt
# Infinite While  loop that will continue until entering no value stops program
while True:
    # Get the values from the user
    a = input("Enter a: ")
    # Pressing enter stops the program
    if a == "":
        break

    a = float(a)
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    # define the discrminant
    d = b**2 - 4*a*c

    if d < 0:
        print("no real solutions")
        xopt = -b / (2*a)
        x = []
        # Make 150 x values around the middle
        for n in range(150):
            x.append(xopt - 5 + n * 10 / 149)

    elif d == 0:
        x1 = -b / (2*a)
        print("one solution:", format(x1, ".4f"))
        x = []
        for n in range(150):
            x.append(x1 - 5 + n * 10 / 149)
    else:
        x1 = (-b - math.sqrt(d)) / (2*a)
        x2 = (-b + math.sqrt(d)) / (2*a)
        print("two solutions: x1=", format(x1, ".4f"), "x2=", format(x2, ".4f"))
        # Put the smaller root first
        if x1 < x2:
            xmin = x1
            xmax = x2
        else:
            xmin = x2
            xmax = x1
        x = []
        # Make 150 x values between the roots
        for n in range(150):
            x.append(xmin - 1 + n * (xmax - xmin + 2) / 149)
    # Calculate the y values
    y = []
    for value in x:
        y.append(a * value**2 + b * value + c)
    # Plot the graph
    plt.plot(x, y)
    plt.axhline(0)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Quadratic Equations")
    plt.show()

