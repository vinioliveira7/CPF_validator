from digit_verification import new_cpf
from string_processing import complete_string_processor


if complete_string_processor == False:
    print("CPF INVÁLIDO")
else:
    print("CPF VÁLIDO" if complete_string_processor() == new_cpf() else "CPF INVÁLIDO")

    

