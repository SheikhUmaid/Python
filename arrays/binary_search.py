


def binary_search(list: list, target : int):
    for i in range(len(list)):
        if list[i] == target:
            print(f"{target} Found at index {i}")

a = {2,4,5,6,8,7,1,9,3,0}
print(a[0])
# binary_search(a, 5)