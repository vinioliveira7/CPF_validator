from verifications import verification_case, validation_cpf

if verification_case() and validation_cpf():
    print("CPF VÁLIDO")
else:
    print("CPF INVÁLIDO")

input("Pressione ENTER para sair...")
    

