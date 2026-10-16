import random, string

s_externa = ""

while True:

    print("----------------------------------")
    print("--------GERADOR DE SENHAS---------")
    print("----------------------------------")

    print("1 - Senha sem Maíusculo e Minúsculos")
    print("2 - Senha sem Caractere")
    print("3 - Senha sem Números")

    es = int(input("Digite a sua escolha: "))

    t_senha = int(input("Digite o tamanho da senha: "))
    
    match es:
        case 1:

            for i in range(t_senha):
            
                senha1 = string.digits + '!@#$%*&'

                senha2 = random.choice(senha1)

                s_externa += senha2 

            print(f"Senha: {s_externa}") 

            break

        case 2:

            for i in range(t_senha):
                        
                senha1 = string.ascii_letters + string.digits
            
                senha2 = random.choice(senha1)
        
                s_externa += senha2 
            
            print(f"Senha: {s_externa}") 

            break


        case 3:
            for i in range(t_senha):
                                    
                senha1 = string.ascii_letters + '!@#$%*&'
                        
                senha2 = random.choice(senha1)
                    
                s_externa += senha2 
                        
            print(f"Senha: {s_externa}")

            break
