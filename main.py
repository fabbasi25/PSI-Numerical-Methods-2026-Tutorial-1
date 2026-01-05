# HELLO WORLD for PSI Numerical Methods 2026

def myexp(x, N=10):
    """
    This function computes exp(x) via the Taylor Series using terms up to
    order N.
    """

    t = 1.0  # The value of the current term
    y = 1.0  # The value of exp(x) up to this point

    # We initialize with the 0th order term, so run the loop
    # for the remaining N terms.
    for i in range(1, N+1):
        t *= x/i  # Update the term: tn = x^n / n!
        y += t    # add tn to y

    # We're done!
    return y


if __name__ == "__main__":

    ## PROBLEM 3 

    print("Hello PSI 2026!")

    import numpy 
    print(numpy.e**1.2)

    import matplotlib.pyplot as plt 
    N = 1000 
    x_data_list = [i*2*numpy.pi/N for i in range(N+1)]
    x_data = numpy.array(x_data_list)
    y_data_cos = numpy.cos(x_data)
    y_data_sin = numpy.sin(x_data)
    graph = plt.figure(figsize=(9,9), layout='tight')
    plt.plot(x_data, y_data_cos, color="red", label="cos(x)")
    plt.plot(x_data, y_data_sin, color="blue", label="sin(x)")
    plt.legend()

    plt.savefig("./PSI-Numerical-Methods-2026-Tutorial-1/trig.png", transparent=False)


    print("e(1) with  5 terms is", myexp(1.0, 5))
    print("e(1) with 10 terms is", myexp(1.0, 10))
    print("e(1) with 20 terms is", myexp(1.0, 20))
    print("e(1) with 40 terms is", myexp(1.0, 40))
