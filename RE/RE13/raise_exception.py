
def raise_exception(alist, value):
    final_list =  []
    for i in alist:
        if (i<=value):
            final_list.append(ValueError("{} is not greater than {}".format(i, value)))
    return final_list
            