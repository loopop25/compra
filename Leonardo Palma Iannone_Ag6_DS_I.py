
valor_total = float(input("Digite o valor total da compra (R$): "))

if valor_total < 200.00:
    percentual_desconto = 5
elif 200.00 <= valor_total < 300.00:
    percentual_desconto = 10
else:
    percentual_desconto = 15

valor_desconto = valor_total * (percentual_desconto / 100)
valor_final = valor_total - valor_desconto

print("\n--- RESUMO DA COMPRA ---")
print(f"Valor original: R$ {valor_total:.2f}")
print(f"Desconto aplicado ({percentual_desconto}%): R$ {valor_desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")