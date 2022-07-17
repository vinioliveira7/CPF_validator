cpf = input("Digite um CPF [xxx.xxx.xxx-xx]: ")

def string_processor():
    treated_cpf = ""

    digit_list = cpf[0:11].split('.')
    treated_cpf = "".join(digit_list)

    return treated_cpf

def complete_string_processor():
    treated_cpf = ""

    digit_list = cpf.split('.')
    treated_cpf = "".join(digit_list)
    digit_list = treated_cpf.split('-')
    treated_cpf = "".join(digit_list)


    if treated_cpf[0] == treated_cpf[1] and treated_cpf[1] == treated_cpf[2] and treated_cpf[2] == treated_cpf[3] and treated_cpf[3] == treated_cpf[4]\
    and treated_cpf[4] == treated_cpf[5] and treated_cpf[5] == treated_cpf[6] and treated_cpf[6] == treated_cpf[7] and treated_cpf[7] == treated_cpf[8]\
    and treated_cpf[8] == treated_cpf[9] and treated_cpf[10]:
        return False

    return treated_cpf