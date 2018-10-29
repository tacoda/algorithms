def insertion_sort(array):
    for j in range (1, len(array)):
        key = array[j]
        i = j - 1
        while i > -1 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key

first = [5, 2, 4, 6, 1, 3]
insertion_sort(first)
print(first)

second = [31, 41, 59, 26, 41, 58]
insertion_sort(second)
print(second)

def reverse_insertion_sort(array):
    for j in range (1, len(array)):
        key = array[j]
        i = j - 1
        while i > -1 and array[i] < key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key

third = [5, 2, 4, 6, 1, 3]
reverse_insertion_sort(third)
print(third)

fourth = [31, 41, 59, 26, 41, 58]
reverse_insertion_sort(fourth)
print(fourth)
