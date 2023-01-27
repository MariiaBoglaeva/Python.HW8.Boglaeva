def input_example():
    example = input("Введите пример: ")
    example = example.replace(' ', '').replace('+', ' + '). \
        replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
    if example.startswith(' - '):
        example = '-' + example[3:]
    example = example.split()
    return example


def print_result(orig_exp: list, example: list):
    print(f"{' '.join(orig_exp)} = {example[0]}")
