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
    return max((a["id"] for a in atividades), default=0) + 1


def mostrar_menu():
    print("\n" + "=" * 46)
    print("         GERENCIADOR DE ESTUDOS")
    print("=" * 46)
    print("1 - Cadastrar atividade")
    print("2 - Listar atividades")
    print("3 - Marcar atividade como concluída")
    print("0 - Sair")


def cadastrar(atividades):
    titulo = input("Título: ").strip()
    if not titulo:
        print("O título não pode ficar vazio.")
        return

    descricao = input("Descrição (opcional): ").strip()

    atividades.append({
        "id": proximo_id(atividades),
        "titulo": titulo,
        "descricao": descricao,
        "concluida": False,
        "data_criacao": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })
    salvar_atividades(atividades)
    print("Atividade cadastrada e salva!")


def listar(atividades):
    print("\nATIVIDADES")
    print("-" * 46)

    if not atividades:
        print("Nenhuma atividade cadastrada.")
        return

    for atividade in atividades:
        status = "✓" if atividade["concluida"] else "○"
        print(
            f'{atividade["id"]:>2}. [{status}] {atividade["titulo"]}'
            f' | criada em {atividade["data_criacao"]}'
        )
        if atividade["descricao"]:
            print(f'    {atividade["descricao"]}')


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
            salvar_atividades(atividades)
            print("Atividade marcada como concluída e salva!")
            return

    print("Atividade não encontrada.")


def main():
    atividades = carregar_atividades()
    print(f"{len(atividades)} atividade(s) carregada(s) do arquivo.")

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
            salvar_atividades(atividades)
            print("Dados salvos. Até a próxima!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
