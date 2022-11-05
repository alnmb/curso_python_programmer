def binary_search(item, my_list):
    my_list = sorted(my_list)
    found = False
    first = 0
    last = len(my_list) - 1

    while found == False and first <= last:
        midpoint = (first + last)//2
        if my_list[midpoint] == item:
            found = True
        else:
            if my_list[midpoint]  < item:
                first = midpoint + 1
            else:
                last = midpoint - 1
    
    return found

test = [6,5,8,2,3,45,87,24,70]

print(binary_search(87,test))
print(binary_search(88,test))
