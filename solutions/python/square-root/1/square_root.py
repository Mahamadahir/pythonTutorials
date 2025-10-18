
def square_root(number):
    def helper(estimate):

        better = 0.5 * (estimate + number/estimate)

        if abs(estimate - better < 0.00000000001):
            return int(better)

        return helper(better)

    return helper(number/2)
        