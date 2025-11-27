# comissoes.py
import json
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP

def calc_comissao(valor: Decimal) -> Decimal:
    if valor < Decimal('100'):
        return Decimal('0')
    if valor < Decimal('500'):
        return (valor * Decimal('0.01')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return (valor * Decimal('0.05')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def main():
    with open('data/vendas.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    comissoes_por_vendedor = defaultdict(Decimal)
    detalhes = defaultdict(list)

    for venda in data.get('vendas', []):
        vendedor = venda['vendedor']
        valor = Decimal(str(venda['valor']))
        comissao = calc_comissao(valor)
        comissoes_por_vendedor[vendedor] += comissao
        detalhes[vendedor].append({'valor': float(valor), 'comissao': float(comissao)})

    print("Comissões por vendedor:")
    for v, c in comissoes_por_vendedor.items():
        print(f"- {v}: R$ {c.quantize(Decimal('0.01'))}")

    # opcional: salvar detalhes
    with open('data/comissoes_result.json', 'w', encoding='utf-8') as out:
        json.dump({'comissoes': {v: float(c) for v, c in comissoes_por_vendedor.items()}, 'detalhes': detalhes}, out, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()
