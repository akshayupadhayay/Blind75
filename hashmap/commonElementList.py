def commonElementBetweenList(l1: list, l2: list) -> list:

    common = list(set(l1) & set(l2))

    return common


print(commonElementBetweenList([1, 2, 3], [4, 5, 6, 3]))
