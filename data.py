
def populatedata(independent, dependent, dataset):

    """
    Populates two lists with one of three sets of bivariate data
    suitable for testing and demonstrating Pearson's Correlation
    """

    del independent[:]
    del dependent[:]

    if dataset == 1:
        independent.extend([10,20,40,45,60,65,75,80])
        dependent.extend([32,44,68,74,92,98,110,116])
        return True

    elif dataset == 2:
        independent.extend([10,20,40,45,60,65,75,80])
        dependent.extend([40,40,60,80,90,110,100,130])
        return True

    elif dataset == 3:
        independent.extend([10,20,40,45,60,65,75,80])
        dependent.extend([100,10,130,90,40,80,180,50])
        return True

    else:
        return False
