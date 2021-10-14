# zad1

def foo(f_letter, surname):
    return f"{f_letter}.{surname}"


print(foo("oskar", "dondalski"))


# zad2


def foo2(name, surname):
    return f"{name[0].title()}.{surname.title()}"


print(foo2("oskar", "dondalski"))


# zad3

def foo3(n, m, age):
    year = str(n) + str(m)
    return int(year) - age


print(foo3(20, 20, 20))


# zad4


def foo4(name, surname, funct):
    return funct(name, surname)


print(foo4("jan", "kowalski", foo2))


# zad5


def foo5(n, m):
    if n > 0 and m >= 0:
        return n / m
    return 0


print(foo5(25, 1))


# zad6

def foo6():
    x = int(input("Podaj liczbe"))
    sum_x = x
    while sum_x < 100:
        x = int(input("Podaj liczbe"))
        sum_x += x
    return sum_x


print(foo6())


# zad7

def foo7(lst):
    return tuple(lst)


print(foo7([1, 2, 3]))


# zad8
def foo8():
    tab = []
    for i in range(5):
        x = input("Podaj wartosc")
        tab.append(x)
    return tuple(tab)


print(foo8())


# zad9

def foo9(n):
    days = ["Poniedzialek", "Wtorek", "Sroda", "Czwartek", "Piatek", "Sobota", "Niedziela"]
    return days[n - 1]


print(foo9(6))


# zad10

def foo10(str_arg):
    for i in range(len(str_arg)):
        if str_arg[i] == str_arg[len(str_arg) - 1 - i]:
            continue
        else:
            return False
    return True


print(foo10("kajak"))
