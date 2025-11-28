import os
import sys

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Calcular comissões")
        print("2 - Registrar movimentação de estoque")
        print("3 - Calcular juros por atraso")
        print("4 - Abrir sistema web (Flask)")
        print("0 - Sair")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            os.system("python utils/comissoes.py")
        elif opc == "2":
            codigo = input("Código do produto: ")
            quantidade = input("Quantidade (+ entrada / - saída): ")
            descricao = input("Descrição: ")
            os.system(f"python utils/movimentacoes.py {codigo} {quantidade} \"{descricao}\"")
        elif opc == "3":
            valor = input("Valor da dívida: ")
            venc = input("Data de vencimento (YYYY-MM-DD): ")
            os.system(f"python utils/juros.py {valor} {venc}")
        elif opc == "4":
            os.system("python app.py")
        elif opc == "0":
            print("Encerrando...")
            sys.exit()
        else:
            print("Opção inválida!")
if __name__ == "__main__":
    menu()