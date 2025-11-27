# juros.py
from datetime import datetime, date
from decimal import Decimal, ROUND_HALF_UP
import sys

def dias_atraso(vencimento: date, hoje: date) -> int:
    delta = (hoje - vencimento).days
    return max(0, delta)

def juros_simples(valor: Decimal, dias: int, taxa_diaria_percent: Decimal = Decimal('2.5')) -> Decimal:
    taxa = taxa_diaria_percent / Decimal('100')
    juros = (valor * taxa * Decimal(dias)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return juros

def juros_compostos(valor: Decimal, dias: int, taxa_diaria_percent: Decimal = Decimal('2.5')) -> Decimal:
    taxa = taxa_diaria_percent / Decimal('100')
    total = (valor * ((Decimal('1') + taxa) ** dias)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return (total - valor).quantize(Decimal('0.01'))

def parse_date(s: str) -> date:
    return datetime.strptime(s, '%Y-%m-%d').date()

def main():
    # Uso: python juros.py <valor> <vencimento(YYYY-MM-DD)>
    if len(sys.argv) < 3:
        print("Uso: python juros.py <valor> <vencimento YYYY-MM-DD>")
        sys.exit(1)
    valor = Decimal(sys.argv[1])
    venc = parse_date(sys.argv[2])
    hoje = date.today()
    dias = dias_atraso(venc, hoje)
    juros_s = juros_simples(valor, dias)
    juros_c = juros_compostos(valor, dias)
    total_s = (valor + juros_s).quantize(Decimal('0.01'))
    total_c = (valor + juros_c).quantize(Decimal('0.01'))

    print(f"Hoje: {hoje} | Vencimento: {venc} | Dias de atraso: {dias}")
    print(f"Juros simples (@2.5%/dia): R$ {juros_s} | Total: R$ {total_s}")
    print(f"Juros compostos (@2.5%/dia): R$ {juros_c} | Total: R$ {total_c}")

if __name__ == '__main__':
    main()
