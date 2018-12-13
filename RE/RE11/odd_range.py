#3.odd_range
def odd_range(start, stop, step):
    return (i for i in range(start if start%2==1 else start+1 , stop, step*2) if i%2==1)
