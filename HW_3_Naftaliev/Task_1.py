# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.


def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

lst = [8,8,8,8,8,8,9,9,9,9,9,9,9,10,10,10,10,11]
print(find_duplicates(lst))