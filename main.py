num = int(input("Digite um número inteiro: "))

if num <= 0:
    print("Número inválido")
elif num == 1:
    print("Não primo")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print("Primo")
    else:
        print("Não primo")