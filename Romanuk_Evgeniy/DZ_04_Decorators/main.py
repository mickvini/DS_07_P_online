def cache_results_for_calls(func):
    counter = 1
    result = 0

    def wrapper(*args):
        nonlocal counter
        nonlocal result

        if counter == 1:
            result = func(*args)
            counter += 1
            return result
        elif counter < 3:
            counter += 1
            return result
        else:
            counter = 1
            return result

    return wrapper


@cache_results_for_calls
def sum_of_args(*args):
    return f"Result of sum, {sum(args)}"


@cache_results_for_calls
def multiplication_of_args(*args):
    result = 1
    for arg in args:
        result *= arg
    return f"Result of mult, {result}"


print(sum_of_args(1, 2))
print(sum_of_args(2, 5))
print(sum_of_args(4, 2))
print(sum_of_args(6, 2))
print(sum_of_args(6, 3))
print(sum_of_args(6, 3))

print(multiplication_of_args(2, 3))
print(multiplication_of_args(2, 3))
print(multiplication_of_args(5, 3))
print(multiplication_of_args(5, 3))
print(multiplication_of_args(4, 3))
print(multiplication_of_args(4, 3))
print(multiplication_of_args(4, 3))