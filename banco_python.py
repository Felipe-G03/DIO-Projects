saldo = 0
extrato = []
def deposito(quantia):
    global saldo
    if quantia > 0 :
        saldo = saldo + quantia
    else:
        print("Valor invalido, a quantia deve ser maior que 0!")
    op = f'deposito de {quantia} reais'
    extrato.append(op)
def saque(quantia):
    global saldo
    if saldo <= quantia:
        saldo = saldo - quantia
    else:
        print("O valor excede o seu saldo atual!")
    op = f'saque de {quantia} reais'
    extrato.append(op)
def view():
    global saldo
    if saldo is None:
        print("Sua conta está vazia")
    else:
        print(f"Seu saldo atual é de {saldo} reais.")       

def ext():
    global extrato
    prt = 'extrato'.center(30,'$')
    print(prt)
    for i in extrato:
        print(i)
    

while True:

   
    print('''
            BANCO DO XESQUE
          Escolha sua operação
          (s) para sacar
          (d) para depositar
          (e) para visualizar seu extrato
          (q) para sair''')
    print()
    
    escolha = input().lower()
    
    if escolha == 's':
        quantia = int(input('Qual quantia deseja sacar? :'\n))
        saque(quantia)
        view()
        
    elif escolha == 'd':
        quantia = int(input("Qual quantia você deseja depositar?"))
        deposito(quantia)
        view()
        
    elif escolha == 'q':
        break
    elif escolha == 'e':
        ext()
    
    else:
        print("Operação desejada não encontrada, tente novamente: ")
