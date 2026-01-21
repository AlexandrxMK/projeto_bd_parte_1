from crud import *


def iniciar_menu():
    while True:
        print("\n" + "="*30)
        print("      SISTEMA BAR 1.0")
        print("="*30)
        print("1. Cadastrar Bebida")
        print("2. Listar Tudo")
        print("3. Pesquisar por Nome")
        print("4. Alterar Preço")
        print("5. Remover Bebida")
        print("6. Exibir um (por ID)")
        print("7. Relatório Geral")
        print("8. Registrar Venda (Baixa Estoque)")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            listar_todos()
        elif opcao == '3':
            pesquisar_por_nome()
        elif opcao == '4':
            alterar_preco()
        elif opcao == '5':
            remover_produto()
        elif opcao == '6':
            exibir_um()
        elif opcao == '7':
            gerar_relatorio()
        elif opcao == '8':
            registrar_venda()
        elif opcao == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")
