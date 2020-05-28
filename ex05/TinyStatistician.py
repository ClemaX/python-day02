from math import sqrt


class TinyStatistician():
    @staticmethod
    def mean(x):
        """
        Add all numbers in x and divide them by their count

        returns the mean as a float or None if iter(x) is empty.
        This method should not raise any exceptions.
        """
        length = len(x)

        return sum(x) / length if length else None

    @staticmethod
    def median(x):
        """
        Get the center of sorted(x) or the average of the two central elements

        returns the median or None if iter(x) is empty
        """
        length = len(x)

        if length == 0:
            return None

        center = length // 2

        x.sort()
        if length % 2 == 0:
            return (x[center - 1] + x[center]) / 2
        else:
            return x[center]

    @staticmethod
    def quartiles(x, percentile):
        """
        Get the 1st and 3rd quartiles in sorted(x)
        """
        length = len(x)

        if percentile == 25:
            center = length // 4
        elif percentile == 75:
            center = length // 2 + length // 4

        x.sort()

        if length % 2 == 0:
            return (x[center - 1] + x[center]) / 2
        else:
            return x[center]

    @staticmethod
    def var(x):
        """
        Get the mean square difference between each value in x and mean(x)

        returns the variance or None if iter(x) is empty
        """
        length = len(x)

        if length == 0:
            return None
        result = 0.0
        m = TinyStatistician.mean(x)
        for i in x:
            result += (i - m) ** 2

        return result / (length - 1)

    @staticmethod
    def std(x):
        """
        Get the standard deviation in x

        returns the standard deviation of x or None if iter(x) is empty
        """
        return sqrt(TinyStatistician.var(x))


if __name__ == "__main__":
    dataset = [1, 2, 3, 4]

    t = TinyStatistician()
    print('dataset:      ', dataset)
    print('mean:         ', t.mean(dataset))
    print('median:       ', t.median(dataset))
    print('1st quartile: ', t.quartiles(dataset, 25))
    print('3rd quartile: ', t.quartiles(dataset, 75))
    print('var:          ', t.var(dataset))
    print('std:          ', t.std(dataset))
