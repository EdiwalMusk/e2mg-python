import numpy as np


def compute_error_for_line_given_points(b, w, points):
    totalError = 0
    for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]
        totalError += (y - (w * x + b)) ** 2
    return totalError / float(len(points))


def step_gradient(b_current, w_current, points, learningRate):
    b_gradient = 0
    w_gradient = 0
    N = float(len(points))
    for i in range(len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2 / N) * (y - ((w_current * x) + b_current))
        w_gradient += -(2 / N) * x * (y - ((w_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = w_current - (learningRate * w_gradient)
    return [new_b, new_m]


def gradient_descent_runner(points, starting_b, starting_m, learningRate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, np.array(points), learningRate)
    return [b, m]


def run():
    points = np.genfromtxt("data.csv", delimiter=",")
    learningRate = 0.001
    initial_b = 0.0
    initial_m = 0.0
    num_iterations = 10000
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learningRate, num_iterations)
    print(b, m)


if __name__ == '__main__':
    run()
