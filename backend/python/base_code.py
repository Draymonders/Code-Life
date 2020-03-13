# 复制list
def copy_list():
    l = [1,2,3,4,5]
    l1 = l[:]
    l1[0] = 10
    print(l)
    print(l1)


def map_each():
    colors = {'red': 1, 'blue': 2}
    for key in colors:
        print(key, colors[key])
    print("====")
    for value in colors.values():
        print(value)
    print("====")
    for (key, value) in colors.items():
        print(key, value)

