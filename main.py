import os
def nome_prog():
     print("================================")
     print("           FINTRACK")
     print("================================")
     print("\nOlá! O FinTrack foi iniciado.")
def main():
     nome_prog()
if __name__ == '__main__':
     main()
nome = input("Digite seu nome: ")
renda = float(input("Digite sua renda mensal: "))
despesas = float(input("Digite suas despesas mensais: "))
def calcular_saldo (renda, despesas):
     saldo = renda - despesas
     return saldo

saldo = calcular_saldo(renda, despesas)
print(f"Certo, {nome}. Sua renda mensal é de R${renda:.2f} e suas despesas mensais são de R${despesas:.2f}.")
print(f"Seu saldo mensal é de R${saldo:.2f}.")
if saldo> 0:
    print ("Parabéns! Seu saldo está positivo")

meta = float(input("Digite sua meta de economia mensal: "))
def calcular_saldo_disponivel (saldo, meta):
     saldo_disponivel = saldo - meta
     return saldo_disponivel
saldo_disponivel = calcular_saldo_disponivel(saldo, meta)
def verificar_meta (saldo, meta):
     meta_atingida = saldo >= meta
     return meta_atingida
meta_atingida = verificar_meta (saldo, meta)
def calcular_valor_faltar (saldo, meta):
    if saldo < meta:
     return meta - saldo
    return 0
faltante = calcular_valor_faltar(saldo, meta)
if saldo < meta:
        print(f"Você não tem o suficiente para bater a meta, faltam R${faltante:.2f}")
elif saldo > meta:
     print (f"Seu saldo é maior que a meta, você pode guardar dinheiro e ainda sobrará R${saldo_disponivel:.2f}")
elif saldo == meta:
    print ("Você tem exatamente o suficiente para a meta, após isso a conta ficará zerada")

    if saldo >0 and saldo >= meta:
         print ("Situação financeira está saudavel e sua meta será atingida")
    elif saldo >0 and saldo < meta:
         print ("Situação financeira saudavel mas não será atingido a meta")
    elif saldo <= 0:
         print("Atenção seu saldo está negativo e/ou igual a 0, não será possivel bater a meta, recomenda-se economizar ")
    if not meta_atingida:
         print(" A meta não será atingida por falta de saldo")