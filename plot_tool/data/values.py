# python native modules

# third-party modules

# plot-tool modules


class ValuesLengthDoesNotMatch(Exception):
    def __init__(self):
        super(ValuesLengthDoesNotMatch, self).__init__(
            "There are not the same amount of x values and y values."
        )


class InvalidConstructorValues(Exception):
    def __init__(self):
        super(InvalidConstructorValues, self).__init__(
            "The constructor received invalid or unexpected values."
        )


class ValueOutOfDomain(Exception):
    def __init__(self):
        super(ValueOutOfDomain, self).__init__(
            "The value is out of the function's domain. No given definition for that value."
        )


class GraphValues(object):
    """ Represents the pair of values that describe a function,
    it consists in a series of (x,y) values corresponding to:
    y = f(x), when f it the function being described.
    """

    def __init__(self, x_values: list, y_values: list):
        x_values = list(x_values)
        y_values = list(y_values)

        # Constructor validation
        if type(x_values) is not list or type(y_values) is not list:
            raise InvalidConstructorValues
        if len(x_values) < len(y_values):
            y_values = y_values[0:len(x_values)]
        elif len(x_values) > len(y_values):
            x_values = x_values[0:len(y_values)]

        if len(x_values) != len(y_values):
            raise ValuesLengthDoesNotMatch

        self.x = x_values
        self.y = y_values

    def __call__(self, x):
        """
        Evaluates the function in the given value and returns
        the resulting y = f(x).

        :param x: Where the function is evaluated.
        :return: The f(x) value.
        """

        # Verifying if x belongs to the function's domain
        if x not in self.x:
            raise ValueOutOfDomain

        return self.y[self.x.index(x)]

    def get_range(self, min_value, max_value) -> list:
        """
        Returns a list of x values that belong to the
        function's domain between the minimum and maximum.

        :param min_value: Minimum value to be added to the list.
        :param max_value: Maximum value to be added to the list.
        :return: List of x values from the function's domain.
        """

        return [
            x
            for x in self.x
            if min_value <= x <= max_value
        ]

    def get_max(self):
        """
        Returns the maximum y = f(x) value of the described function.

        :return: Maximum f(x) = y value or None if empty.
        """

        # Verify if y values list is empty
        if not len(self.y):
            return None
        else:
            return max(self.y)

    def get_min(self):
        """
        Returns the minimum y = f(x) value of the described function.

        :return: Minimum f(x) = y value or None if empty.
        """

        # Verify if y values list is empty
        if not len(self.y):
            return None
        else:
            return min(self.y)
