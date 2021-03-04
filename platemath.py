def plate_math(target):
    def find(current, history):
        if current == target:
            return history
        elif current > target:
            return None
        else:
            return find(current + 90, (f'{history} +  45') or find(current + 50, (f'{history} +  25')) or find(current + 20, (f'{history} +  10')) or find(current + 10, (f'{history} +  5')) or find(current + 2.5, (f'{history} +  5'))
    
    if find(45, "45") is not (None):
        return find(45, "45")
    elif find(25, '25') is not None:
        return find(25, '25')
    elif find(10, '10') is not None:
        return find(10, '10')
    elif find (5, '5') is not None:
        return find(5, '5')
    elif find (2.5, '2.5') is not None
        return find (2.5, '2.5')
    else:
        return ('no')