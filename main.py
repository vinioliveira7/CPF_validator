from verifications import verification_case, validation_cpf
from string_processing import cpf


if len(cpf) != 11:
    print("Tamanho inválido")
else:
    if verification_case() and validation_cpf():
        print("CPF VÁLIDO")
    else:
        print("CPF INVÁLIDO")
    
input("Pressione ENTER para sair...")
    

