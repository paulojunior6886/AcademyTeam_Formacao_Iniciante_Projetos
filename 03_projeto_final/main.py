\
from pathlib import Path
import csv
from datetime import datetime

ARQUIVO_DADOS = Path(__file__).with_name("dados.txt")
CAMPOS = ["id", "titulo", "descricao", "concluida", "data_criacao"]


def carregar_atividades():
    if not ARQUIVO_DADOS.exists():
        return []

    atividades = []
    with ARQUIVO_DADOS.open("r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter="|")
        for linha in leitor:
            atividades.append({
                "id": int(linha["id"]),
                "titulo": linha["titulo"],
                "descricao": linha["descricao"],
                "concluida": linha["concluida"].lower() == "true",
                "data_criacao": linha["data_criacao"],
            })
    return atividades


def salvar_atividades(atividades):
    with ARQUIVO_DADOS.open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(
            arquivo,
            fieldnames=CAMPOS,
            delimiter="|",
            lineterminator="\n",
        )
        escritor.writeheader()
        for atividade in atividades:
            escritor.writerow({
                **atividade,
                "concluida": str(atividade["concluida"]).lower(),
            })


def proximo_id(atividades):
    return max((atividade["id"] for atividade in atividades), default=0) + 1


def buscar_por_id(atividades, atividade_id):
    for atividade in atividades:
        if atividade["id"] == atividade_id:
            return atividade
    return None


def mostrar_menu():
    print("\n" + "=" * 52)
    print("            GERENCIADOR DE ESTUDOS")
    print("=" * 52)
    print("1 - Cadastrar atividade")
    print("2 - Listar todas")
    print("3 - Listar pendentes")
    print("4 - Marcar atividade como concluída")
    print("5 - Remover atividade")
    print("0 - Sair")


def cadastrar(atividades):
    print("\nNOVA ATIVIDADE")
    titulo = input("Título: ").strip()
    if not titulo:
        print("O título é obrigatório.")
        return

    descricao = input("Descrição (opcional): ").strip()
    atividade = {
        "id": proximo_id(atividades),
        "titulo": titulo,
        "descricao": descricao,
        "concluida": False,
        "data_criacao": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    atividades.append(atividade)
    salvar_atividades(atividades)
    print(f'Atividade #{atividade["id"]} cadastrada com sucesso!')


def exibir_lista(atividades):
    if not atividades:
        print("Nenhuma atividade encontrada.")
        return

    for atividade in atividades:
        status = "✓" if atividade["concluida"] else "○"
        print(f'{atividade["id"]:>2}. [{status}] {atividade["titulo"]}')
        if atividade["descricao"]:
            print(f'    {atividade["descricao"]}')
        print(f'    Criada em: {atividade["data_criacao"]}')


def listar_todas(atividades):
    print("\nTODAS AS ATIVIDADES")
    print("-" * 52)
    exibir_lista(atividades)


def listar_pendentes(atividades):
    print("\nATIVIDADES PENDENTES")
    print("-" * 52)
    pendentes = [a for a in atividades if not a["concluida"]]
    exibir_lista(pendentes)


def concluir(atividades):
    listar_todas(atividades)
    if not atividades:
        return

    try:
        atividade_id = int(input("\nID da atividade concluída: "))
    except ValueError:
        print("Digite um ID numérico.")
        return

    atividade = buscar_por_id(atividades, atividade_id)
    if not atividade:
        print("Atividade não encontrada.")
        return

    atividade["concluida"] = True
    salvar_atividades(atividades)
    print("Atividade concluída!")


def remover(atividades):
    listar_todas(atividades)
    if not atividades:
        return

    try:
        atividade_id = int(input("\nID da atividade a remover: "))
    except ValueError:
        print("Digite um ID numérico.")
        return

    atividade = buscar_por_id(atividades, atividade_id)
    if not atividade:
        print("Atividade não encontrada.")
        return

    atividades.remove(atividade)
    salvar_atividades(atividades)
    print("Atividade removida.")


def main():
    atividades = carregar_atividades()
    print("Gerenciador de Estudos — AcademyTeam")
    print(f"{len(atividades)} atividade(s) carregada(s).")

    while True:
        mostrar_menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar(atividades)
        elif opcao == "2":
            listar_todas(atividades)
        elif opcao == "3":
            listar_pendentes(atividades)
        elif opcao == "4":
            concluir(atividades)
        elif opcao == "5":
            remover(atividades)
        elif opcao == "0":
            salvar_atividades(atividades)
            print("Dados salvos. Até a próxima!")
            break
        else:
            print("Opção inválida. Escolha uma opção do menu.")


if __name__ == "__main__":
    main()
