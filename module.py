operation = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             "*": lambda x, y: x * y,
             "/": lambda x, y: x / y}


def calculate(oper_1, oper_2, example):
    global operation
    i = 0
    while oper_1 in example or oper_2 in example:
        if example[i] in [oper_1, oper_2]:
            example[i - 1] = operation.get(example[i])(int(example[i - 1]), int(example[i + 1]))
            example.pop(i)
            example.pop(i)
        else:
            i += 1


def res_calculation(example: list):
    while len(example) > 1:
        calculate('*', '/', example)
        calculate('+', '-', example)
    return example
