def getDegree(num):
    return {
        num == 0: ' = 0',
        num == 1: '*x + ',
        num > 1: f'*x^{num} + ',       
    }[True]