def fibonacci(number):
    """Função que verifica se um número está na sequência de Fibonacci."""
    if number < 0:
        return False
    elif number == 0:
        return True
    else:
        a, b = 0, 1
        while b < number:
            a, b = b, a + b
        return b == number

while True:
    # Pedir que o usuário insira um número ou "sair" para encerrar
    user_input = input("Insira um número inteiro ou digite 'sair' para encerrar: ")
    
    # Verificar se o usuário quer sair
    if user_input.lower() == "sair" or user_input.lower() == "exit":
        print("Encerrando o programa...")
        break
    
    # Converter a entrada do usuário em um número inteiro
    try:
        number = int(user_input)
    except ValueError:
        print("Entrada inválida. Insira um número inteiro ou digite 'sair' para encerrar.")
        continue
    
    # Verificar se o número está na sequência de Fibonacci
    if fibonacci(number):
        print(number, "está na sequência de Fibonacci.")
    else:
        print(number, "não está na sequência de Fibonacci.")
