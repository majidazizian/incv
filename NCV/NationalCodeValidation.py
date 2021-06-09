def CodeValidation(code):
    index = 10
    temp = 0
    NC = []

    for n in code:
        NC.append(int(n))

    if len(code) < 10:
        zero = 10 - len(code)
        for _ in range(zero):
            NC.insert(0, 0)
    elif len(code) > 10:
        return False

    for n in NC:
        if index < 2:
            break
        else:
            temp += n * index
        index -= 1

    if temp % 11 == 2:
        if temp % 11 == NC[-1]:
            return True
        else:
            return False
    else:
        if 11 - temp % 11 == NC[-1]:
            return True
        else:
            return False
