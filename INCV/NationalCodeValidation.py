import re


def CodeValidation(code):
    index = 10
    temp = 0
    NC = []
    BlackCode = ["1111111111", "2222222222", "3333333333", "4444444444", "5555555555", "6666666666", "7777777777",
                 "8888888888", "9999999999"]
    pattern = re.compile("^([0-9]){10}$")
    if pattern.search(code):
        if code in BlackCode:
            return False
        else:
            for n in code:
                NC.append(int(n))

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
    else:
        return False
