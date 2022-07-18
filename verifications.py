from string_processing import *

treated_cpf = string_processor()

def digit1_verificator():

    digits = treated_cpf
    cont = 10
    total = 0
    for digit in digits:
        digit = int(digit)
        value = digit * cont
        total += value
        cont -= 1
    result = 11 - (total % 11)
    return '0' if result > 9 else str(result)


def digit2_verificator():
    
    digits = treated_cpf + digit1_verificator()
    cont = 11
    total = 0
    for digit in digits:
        digit = int(digit)
        value = digit * cont
        total += value
        cont -= 1
    result = 11 - (total % 11)
    return '0' if result > 9 else str(result)

def new_cpf():
    complete_cpf = treated_cpf + digit1_verificator() + digit2_verificator()
    return complete_cpf


def verification_case():

    if new_cpf() == cpf[0] * 11:
        return False

    return True
    

def validation_cpf():
    
    if new_cpf() != cpf:
        return False
    
    return True

    






