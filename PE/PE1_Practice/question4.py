def fpro_grade(le, re, pe, te):
    if (le>100 or re>100 or pe>100 or te>100) or (le<0 or re<0 or pe<0 or te<0):
        return "Input error"
    elif pe < 40 or te < 40:
        return "RFC"
    else:
        return round(((le + re + 4 * pe + 4 * te)/50), 0)

le_input = float(input("LE: "))
re_input = float(input("RE: "))
pe_input = float(input("PE: "))
te_input = float(input("TE: "))

print(fpro_grade(le_input, re_input, pe_input, te_input))
