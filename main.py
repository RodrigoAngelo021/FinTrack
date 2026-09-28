print("================================")
print("           FINTRACK")
print("================================")

print("Olá! O FinTrack foi iniciado.")
nome = input("Digite seu nome: ")
renda = float(input("Digite sua renda mensal: "))
despesas = float(input("Digite suas despesas mensais: "))
saldo = renda - despesas


print(f"Certo, {nome}. Sua renda mensal é de R${renda:.2f} e suas despesas mensais são de R${despesas:.2f}.")
print(f"Seu saldo mensal é de R${saldo:.2f}.")
if saldo> 0:
    print ("Parabéns! Seu saldo está positivo")
    
meta = float(input("Digite sua meta de economia mensal: "))
saldo_disponivel = saldo - meta
if saldo_disponivel< 0:
     saldo_disponivel = saldo_disponivel * -1

if saldo < meta:
        print(f"Você não tem o suficiente para bater a meta, faltam R${saldo_disponivel:.2f}")
elif saldo > meta:
     print (f"Seu saldo é maior que a meta, você pode guardar dinheiro e ainda sobrará R${saldo_disponivel:.2f}")
elif saldo == meta:
    print ("Você tem exatamente o suficiente para a meta, após isso a conta ficará zerada")