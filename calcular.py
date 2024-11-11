import json

quant_dias=0
quant_dias_alto = 0
total=0

with open('faturamento.json', 'r') as file:
    dados = json.load(file)

faturamentos = [dia["faturamento"] for dia in dados["faturamentos"] if dia["faturamento"] > 0]

valor_min = faturamentos[0]
valor_max = faturamentos[0]

for faturamento in faturamentos:
    total += faturamento
    quant_dias += +1
    if faturamento > valor_max:
        valor_max = faturamento
    if faturamento < valor_min:
        valor_min = faturamento

media=total/quant_dias

for faturamento in faturamentos:
     if faturamento > media:
        quant_dias_alto = quant_dias_alto+1



print("Valor máximo:", valor_max)
print("Valor mínimo:", valor_min)
print("Quantidades de dias acima da media:",quant_dias_alto)