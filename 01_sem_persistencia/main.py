\
def mostrar_menu():
    print("\n" + "=" * 42)
    print("       GERENCIADOR DE ESTUDOS")
    print("=" * 42)
    print("1 - Cadastrar atividade")
    print("2 - Listar atividades")
    print("3 - Marcar atividade como concluída")
    print("0 - Sair")


def cadastrar(atividades):
    titulo = input("Título da atividade: ").strip()
    if not titulo:
        print("O título não pode ficar vazio.")
        return

    atividades.append({
        "id": len(atividades) + 1,
        "titulo": titulo,
        "concluida": False,
    })
    print("Atividade cadastrada com sucesso!")


def listar(atividades):
    print("\nATIVIDADES")
    print("-" * 42)

    if not atividades:
        print("Nenhuma atividade cadastrada.")
        return

    for atividade in atividades:
        status = "✓" if atividade["concluida"] else "○"
        print(f'{atividade["id"]}. [{status}] {atividade["titulo"]}')


def concluir(atividades):
    listar(atividades)
    if not atividades:
        return

    try:
        atividade_id = int(input("\nID da atividade concluída: "))
    except ValueError:
        print("Digite um número válido.")
        return

    for atividade in atividades:
        if atividade["id"] == atividade_id:
            atividade["concluida"] = True
            print("Atividade marcada como concluída!")
            return

    print("Atividade não encontrada.")


def main():
    # Esta lista existe apenas em memória.
    # Ao fechar o programa, todos os dados são perdidos.
    atividades = []

    while True:
        mostrar_menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar(atividades)
        elif opcao == "2":
            listar(atividades)
        elif opcao == "3":
            concluir(atividades)
        elif opcao == "0":
            print("Programa encerrado. Os dados desta versão NÃO foram salvos.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
