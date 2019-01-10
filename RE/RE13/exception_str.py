
def exception_str(l):
    try:
        l()
    except Exception as e:
        return str(e)
    else:
        return "No exception was raised"
        
        
        
    