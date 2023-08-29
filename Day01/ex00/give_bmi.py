def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        if (len(height) != len(weight)):
            raise AssertionError(" The Hight and Weight lists are not the same size ")
        amazing = weight + height
        for each in amazing:
            if (type(each) not in [float, int]):
                raise AssertionError("Invalid Elements in the list")
            if (each <= 0):
                raise AssertionError("Height and weight must be bigger then 0")
        bmi = []
        for indx, human in enumerate(height):
            bmi.append(round(weight[indx] / human ** 2, 2))
        return bmi
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))
    
def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        for each in bmi:
            if (type(each) not in [float, int]):
                raise AssertionError("Invalid Elements in the list")
        over = []
        for human in bmi:
            if (human > limit):
                over.append("False")
            else:
                over.append("True")
        return over
    except AssertionError as error:
        print(AssertionError.__name__ + ":" + str(error))
    return