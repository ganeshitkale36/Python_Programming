def chkprime(list):
    if (list < 1):
        return False
    for i in range(2,int(list ** 0.5) + 1):
        if list % i == 0:
            return False
    return True

           
