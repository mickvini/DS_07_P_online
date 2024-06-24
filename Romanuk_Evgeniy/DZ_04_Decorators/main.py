def cache_results_for_calls(func):
    cache = {}
    call_count = {}

    def wrapper(*args):
        if args in cache and call_count.get(args, 0) < 3:
            call_count[args] = call_count.get(args, 0) + 1
            return f"Return cached {cache[args]}"
        else:
            result = func(*args)
            cache[args] = result
            call_count[args] = 1
            return f"Return computed {result}"

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
print(sum_of_args(6, 2))
print(sum_of_args(2, 5))

print(multiplication_of_args(2, 3))
print(multiplication_of_args(2, 3))
print(multiplication_of_args(5, 3))
print(multiplication_of_args(5, 3))
print(multiplication_of_args(4, 3))
print(multiplication_of_args(4, 3))
print(multiplication_of_args(4, 3))
print(multiplication_of_args(4, 3))
print(sum_of_args(6, 2))

