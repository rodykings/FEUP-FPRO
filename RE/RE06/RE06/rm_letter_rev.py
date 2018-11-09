def rm_letter_rev(l, astr):
    
    result = ""
    replace = astr.replace(l, "")
    if l != " ": 
        for i in replace:
                result = i + result
        return result
    else:
        for i in replace:
                result += i
        return result


