from functools import reduce

from ft_filter import ft_filter
from ft_map import ft_map
from ft_reduce import ft_reduce


test = [0, 1, 2, 120, 121]

result = ft_filter(lambda x: x % 2, test)
print('ft_filter:', result)

result = list(filter(lambda x: x % 2, test))
print('filter:   ', result)

result = ft_map(lambda x: x + 2, test)
print('ft_map:   ', result)


result = list(map(lambda x: x + 2, test))
print('map:      ', result)

result = ft_reduce(lambda x, y: x + y, test)
print('ft_reduce:', result)

result = reduce(lambda x, y: x + y, test)
print('reduce:   ', result)
