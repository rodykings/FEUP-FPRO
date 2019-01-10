
def rec_exceptions(l):
    final_list = []
    for i in (l):
        try:
            e2 = i()
        except Exception as ex:
            final_list.append(ex)
        else:
            final_list += rec_exceptions(e2)
    return final_list