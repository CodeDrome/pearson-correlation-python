import math


def pearson_correlation(independent, dependent):

    """
    Implements Pearson's Correlation, using several utility functions to
    calculate intermediate values before calculating and returning rho.
    """

    # covariance
    independent_mean = _arithmetic_mean(independent)
    dependent_mean = _arithmetic_mean(dependent)
    products_mean = _mean_of_products(independent, dependent)
    covariance = products_mean - (independent_mean * dependent_mean)

    # standard deviations of independent values
    independent_standard_deviation = _standard_deviation(independent)

    # standard deviations of dependent values
    dependent_standard_deviation = _standard_deviation(dependent)

    # Pearson Correlation Coefficient
    rho = covariance / (independent_standard_deviation * dependent_standard_deviation)

    return rho


def  _arithmetic_mean(data):

    """
    Total / count: the everyday meaning of "average"
    """

    total = 0

    for i in data:
        total+= i

    return total / len(data)


def  _mean_of_products(data1, data2):

    """
    The mean of the products of the corresponding values of bivariate data
    """

    total = 0

    for i in range(0, len(data1)):
        total += (data1[i] * data2[i])

    return total / len(data1)


def  _standard_deviation(data):

    """
    A measure of how individual values typically differ from the mean_of_data.
    The square root of the variance.
    """

    squares = []

    for i in data:
        squares.append(i ** 2)

    mean_of_squares = _arithmetic_mean(squares)
    mean_of_data = _arithmetic_mean(data)
    square_of_mean = mean_of_data ** 2
    variance = mean_of_squares - square_of_mean
    std_dev = math.sqrt(variance)

    return std_dev
