import itertools

def numbers(n: int):  # 1
    if n <= 0:
        return
    print(n)
    numbers(n - 1)


def fib(n: int) -> int:  # 2
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def power(number: int, n: int) -> int:  # 3
    if n == 0:
        return 1
    elif n == 1:
        return number
    else:
        return number * power(number, n - 1)


def reverse(txt: str) -> str:  # 4
    if len(txt) == 0:
        return txt
    else:
        return reverse(txt[1:]) + txt[0]


def factorial(n: int) -> int:  # 5
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n * factorial(n - 1)


def prime(n: int, i=2) -> bool:  # 6
    if n <= 2:
        return True if (n == 2) else False
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return prime(n, i + 1)


def n_sums(n: int, lst=None, i=0) -> list[int]:  # 7
    if lst is None:
        lst = []
        i = (10 ** n) - 1
    if i <= 10 ** (n - 1):
        return lst
    sum_even, sum_odd = 0, 0
    for j in range(n):
        if j % 2 == 0:
            sum_even += (i // 10 ** j) % 10
        else:
            sum_odd += (i // 10 ** j) % 10
    if sum_even == sum_odd:
        lst.append(i)
        return n_sums(n, lst, i - 11)
    return n_sums(n, lst, i - 1)


def combinations(n: int, lst=None) -> list[list[int]]:
    if lst is None:
        new_lst = [i + 1 for i in range(n)]
        new_lst += new_lst
        lst = list(itertools.permutations(new_lst))
    return lst


def remove_duplicates(txt: str) -> str:  # 9
    if len(txt) == 1:
        return txt
    if txt[0] == txt[1]:
        return remove_duplicates(txt[1:])
    return txt[0] + remove_duplicates(txt[1:])


if __name__ == '__main__':
    # numbers(10)
    # print(fib(3))
    # print(power(2, 3))
    # print(reverse("Oskar"))
    # print(factorial(4))
    # print(prime(2))
    # print(n_sums(3))
    print(combinations(3))
    # print(remove_duplicates("XYYYYWWWG"))
