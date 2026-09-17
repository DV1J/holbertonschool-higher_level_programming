#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    div = 0
    try:
        for num in range(list_length):
            div = my_list_1[num] / my_list_2[num]
            new_list.append(div)
    except ZeroDivisionError:
        print('division by 0')
        new_list.append(0)
        num += 1
        div = my_list_1[num] / my_list_2[num + 1]
        new_list.append(div)
        if TypeError:
            print('wrong type')
            new_list.append(0)
        if FloatingPointError:
            new_list.append(0)
        if IndexError:
            print('out of range')
    finally:
        return (new_list)
