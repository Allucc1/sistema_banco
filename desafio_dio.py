menu = '''
------------ Bem vindo ao BA -------------
    Por favor selecione a opção desejada

    [d] Dep
    [s] Saque
    [e] Extrato
    [4] Sair

-------------------------------------------
'''

saldo = 0
limite = 500
extrato = []
num_saques = 0
limite_saques = 3

while True:
    opção = input(menu)

    

    if opção == 'd':
        valor_dep = int(input('Deposite o valor do dep: R$'))
        saldo += valor_dep
        print('O valor do dep foi de {} seu saldo agora é {}'.format(valor_dep, saldo))
        extrato.append(f'{valor_dep} de depósito') 

        if valor_dep > 0:
            extrato.append(f'+{valor_dep} de depósito')
            print(f'O valor do depósito foi de {valor_dep}. Seu saldo agora é {saldo}')
        else:
            print('Você não pode depositar um valor negativo. Por favor, insira um valor positivo.')

    elif opção == 's':
        valor_saq = float(input('Digite o valor a ser sacado: R$'))
        if valor_saq <= limite and valor_saq <= saldo and num_saques < limite_saques:
           saldo -= valor_saq
           num_saques += 1
           extrato.append(f'-{valor_saq} de saque')
        else:
            print('Saque não autorizado, verifique o saldo ou o limite de saque que é de R$500')

    elif opção == 'e':
        print(f'O seu salto atual é {saldo}')
        print('Extrato: ')
        for ação in extrato:
            print(ação)

    elif opção == '4':
        break

    else:
        print('Opção invalida, porfavor utilize apenas as opções validas.')
    

while True:
    print('Obrigado Volte sempre!')
    break


  




    




