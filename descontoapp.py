# Entrada do valor da compra do cliente
valor_Total_Compras = float(input("Insira o valor total de sua compra por favor: \n"))

# Estrutura de decisão dos descontos progressivos
if valor_Total_Compras < 200:
    # 5 porcento de desconto
    desconto = valor_Total_Compras - (valor_Total_Compras * 0.05)
    print(f"Parabéns! Você ganhou 5% de desconto nas suas compras, o valor final agora é: {desconto:.2f}$")
elif valor_Total_Compras >= 200 and valor_Total_Compras < 300:
    # 10 porcento de desconto
    desconto = valor_Total_Compras - (valor_Total_Compras * 0.1)
    print(f"Parabéns! Você ganhou 10% de desconto nas suas compras, o valor final agora é: {desconto:.2f}$")
else:
    # 15 porcento de desconto
    desconto = valor_Total_Compras - (valor_Total_Compras * 0.15)
    print(f"Parabéns! Você ganhou o desconto maior de 15% nas suas compras, o valor final agora é: {desconto:.2f}$")




    
