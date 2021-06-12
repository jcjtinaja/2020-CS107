import numpy as np
import cProfile
from pstats import SortKey, Stats

def f(x):
    return x - np.exp(-2.0 * np.sin(4.0*x) * np.sin(4.0*x))

def dfdx(x):
    return 1.0 + 16.0 * np.exp(-2.0 * np.sin(4.0*x) * np.sin(4.0*x)) * np.sin(4.0*x) * np.cos(4.0*x)

def dfdx_h(x, epsilon):
    return (f(x + epsilon) - f(x)) / epsilon

def main():
    # Start Newton algorithm
    xk = -100.0 # Initial guess
    tol = 1.0e-08 # Some tolerance
    max_it = 100 # Just stop if a root isn't found after 100 iterations
    h = 1.0e-09
    
    root = None # Initialize root
    for k in range(max_it):
        delta_xk = -f(xk) / dfdx(xk) # Update Delta x_{k}
        # delta_xk = -f(xk) / dfdx_h(xk, h) # Update Delta x_{k}
        if (abs(delta_xk) <= tol): # Stop iteration if solution found
            root = xk + delta_xk
            print("Found root at x = {0:17.16f} after {1} iterations.".format(root, k+1))
            break
        print("At iteration {0}, Delta x = {1:17.16f}".format(k+1, delta_xk))
        xk += delta_xk # Update xk

if __name__ == "__main__":
    cProfile.run('main()', 'stats')
    p = Stats('stats')
    p.sort_stats(SortKey.CUMULATIVE)
    p.print_stats()
    #main()