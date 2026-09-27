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
meta = float(input("Digite sua meta de economia mensal: "))
saldo_disponivel = saldo - meta
print(f"Após guardar o valor da meta de economia de R${meta:.2f}, você terá um saldo disponível de R${saldo_disponivel:.2f} no mês.")