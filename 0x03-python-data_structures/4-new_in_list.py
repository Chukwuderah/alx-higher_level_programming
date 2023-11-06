<<<<<<< HEAD
#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    new_list = list(my_list)
    new_list[idx] = element
    return new_list

=======
#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    if (idx < 0) or (idx > (len(my_list)-1)):
        return my_list

    cp = [x for x in my_list]
    cp[idx] = element
    return cp
>>>>>>> 727c1ef99e915b90480c09b9388bcaa414cc3eff
