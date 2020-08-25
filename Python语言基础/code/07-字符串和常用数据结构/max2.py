"""
返回传入的列表中最大和第二大的元素的值
"""


def max2(list):
    m1, m2 = (list[0], list[1]) if list[0] > list[1] else (list[1], list[0])
    for index in range(2, len(list)):
        if list[index] > m1:
            m2 = m1
            m1 = list[index]
        elif list[index] > m2:
            m2 = list[index]
    return m1, m2


if __name__ == "__main__":
    list = [89, 20, 13, 47, 95, 34, 8, 72]
    print(max2(list))
