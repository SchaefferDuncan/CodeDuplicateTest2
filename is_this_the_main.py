def a_bubbly_kind_of_sort(argh):
    n = len(argh)
    for i in range(n):
        for j in range(0, n - i - 1):
            if argh[j] > argh[j + 1]:
                argh[j], argh[j + 1] = argh[j + 1], argh[j]


def the_sort_that_inserts(ugh):
    for i in range(1, len(ugh)):
        key = ugh[i]
        j = i - 1
        while j >= 0 and key < ugh[j]:
            ugh[j + 1] = ugh[j]
            j -= 1
        ugh[j + 1] = key


def break_up_the_band(ugg, low, high):
    i = (low - 1)
    pivot = ugg[high]
    for j in range(low, high):
        if ugg[j] <= pivot:
            i = i + 1
            ugg[i], ugg[j] = ugg[j], ugg[i]
    ugg[i + 1], ugg[high] = ugg[high], ugg[i + 1]
    return i + 1


# Function to do Quick sort
def a_super_fast_sort(arr, low, high):
    if low < high:
        pi = break_up_the_band(arr, low, high)
        a_super_fast_sort(arr, low, pi - 1)
        a_super_fast_sort(arr, pi + 1, high)
