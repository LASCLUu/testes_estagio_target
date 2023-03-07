import json


with open('faturamentos.json') as f:
    faturamentos = json.load(f)
    faturamentos_int = int(0)


menor = min(faturamentos_int)
maior = max(faturamentos_int)


dias_com_faturamento = [f for f in faturamentos_int if f > 0]
media = sum(dias_com_faturamento) / len(dias_com_faturamento)


dias_acima_da_media = sum(1 for f in faturamentos_int if f > media)


print("Menor faturamento diário:", menor)
print("Maior faturamento diário:", maior)
print("Número de dias com faturamento acima da média:", dias_acima_da_media)