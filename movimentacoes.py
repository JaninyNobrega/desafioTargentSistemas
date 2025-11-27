# movimentacoes.py
import json
import uuid
import sys
from datetime import datetime
from pathlib import Path

DATA_DIR = Path('data')
ESTOQUE_FILE = DATA_DIR / 'estoque.json'
MOVS_FILE = DATA_DIR / 'movimentacoes.json'

def load_estoque():
    with ESTOQUE_FILE.open(encoding='utf-8') as f:
        return json.load(f)['estoque']

def save_estoque(estoque_list):
    with ESTOQUE_FILE.open('w', encoding='utf-8') as f:
        json.dump({'estoque': estoque_list}, f, ensure_ascii=False, indent=2)

def load_movs():
    if MOVS_FILE.exists():
        with MOVS_FILE.open(encoding='utf-8') as f:
            return json.load(f)
    return []

def save_movs(movs):
    with MOVS_FILE.open('w', encoding='utf-8') as f:
        json.dump(movs, f, ensure_ascii=False, indent=2)

def find_prod(estoque, codigo):
    for p in estoque:
        if p['codigoProduto'] == codigo:
            return p
    return None

def main():
    # simples parsing: python movimentacoes.py <codigoProduto> <quantidade> "<descricao>"
    if len(sys.argv) < 4:
        print("Uso: python movimentacoes.py <codigoProduto> <quantidade> \"<descricao>\"")
        print("quantidade positiva = entrada, negativa = saída")
        sys.exit(1)

    codigo = int(sys.argv[1])
    quantidade = int(sys.argv[2])
    descricao = sys.argv[3]

    estoque = load_estoque()
    prod = find_prod(estoque, codigo)
    if prod is None:
        print(f"Produto com código {codigo} não encontrado.")
        sys.exit(1)

    mov = {
        'id': str(uuid.uuid4()),
        'codigoProduto': codigo,
        'descricaoMovimentacao': descricao,
        'quantidade': quantidade,
        'dataHora': datetime.now().isoformat()
    }

    prod['estoque'] += quantidade
    if prod['estoque'] < 0:
        print("Erro: estoque ficou negativo. Operação abortada.")
        sys.exit(1)

    movs = load_movs()
    movs.append(mov)
    save_movs(movs)
    save_estoque(estoque)

    print(f"Movimentação registrada: id={mov['id']}")
    print(f"Produto: {prod['descricaoProduto']} (codigo {codigo})")
    print(f"Quantidade alterada: {quantidade}")
    print(f"Estoque final: {prod['estoque']}")

if __name__ == '__main__':
    main()
