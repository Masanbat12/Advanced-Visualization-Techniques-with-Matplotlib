import matplotlib.pyplot as plt

from random_walk import RandomWalk
"""for exec_03"""
# from exec_03 import Exec_03
"""for exec_04"""
# from exec_04 import Exec_04

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    # rw = Exec_03(50_000)
    # rw = Exec_04(50_000)
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    # fig, ax = plt.subplots()
    """ use of the space available on your screen """
    # fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    fig, ax = plt.subplots(figsize=(12, 6))

    point_numbers = range(rw.num_points)
    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolor='none', s=1)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
               s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    # plt.savefig('exe_04.png', bbox_inches='tight')

    keep_running = input("Do you want to make another walk? (y/n): ")
    if keep_running == 'n':
        break
