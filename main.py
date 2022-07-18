from verifications import verification_case, validation_cpf
from string_processing import cpf

while(True):
    if len(cpf) != 11:
        print("Tamanho inválido")
        break

    if verification_case() and validation_cpf():
        print("CPF VÁLIDO")
    else:
        print("CPF INVÁLIDO")

    input("Pressione ENTER para sair...")
    

