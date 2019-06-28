import itertools as it


def take(n, iterable):
    return list(it.islice(iterable, n))


def prepend(value, iterator):
    return it.chain([value], iterator)


def tabulate(function, start=0):
    # Same as (function(i) for i in range(start))
    return map(function, it.count(start))


def all_equal(iterable):
    g = it.groupby(iterable)
    return next(g, True) and not next(g, False)


def quantify(iterable, pred=bool):
    return sum(map(pred, iterable))


print(all_equal(iter([1, 1, 1, 1, 1])))
print(all_equal(iter([1, 1, 1, 1, 2])))
