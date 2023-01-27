import module
import view


def calculate():
    exp = view.input_example()
    origin_exp = exp.copy()
    result = module.res_calculation(exp)
    view.print_result(origin_exp, result)
