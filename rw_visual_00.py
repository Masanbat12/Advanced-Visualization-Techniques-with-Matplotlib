import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()

    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()
    # plt.savefig('exe4.png', bbox_inches='tight')

    keep_running = input("Do you want to make another walk? (y/n): ")
    if keep_running == 'n':
        break




