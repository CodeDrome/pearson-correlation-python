import data
import pearsoncorrelation


def main():

    """
    Iterates the three available sets of data
    and calls function to calculate rho.
    Then prints the data and Pearson Correlation Coefficient.
    """

    print("-------------------------")
    print("| codedrome.com         |")
    print("| Pearson's Correlation |")
    print("-------------------------\n")

    independent = []
    dependent = []

    for d in range(1, 4):

        if data.populatedata(independent, dependent, d) == True:

            rho = pearsoncorrelation.pearson_correlation(independent, dependent)

            print("Dataset %d\n---------" % d)
            print("Independent data: " + (str(independent)))
            print("Dependent data:   " + (str(dependent)))
            print("Pearson Correlation Coefficient rho = %1.2f\n" % rho)
        else:
            print("Cannot populate Dataset %d" % d)


main()
