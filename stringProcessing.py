def get_cpf():
    cpf = input("Insira CPF: ")
    return cpf


def string_processor(cpf = get_cpf()):
    treated_cpf = ""
    digit_list = cpf[0:11].split('.')
    treated_cpf = "".join(digit_list)

    return treated_cpf