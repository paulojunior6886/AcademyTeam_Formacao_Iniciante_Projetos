# AcademyTeam — Projetos de Apoio da Formação Iniciante

Este pacote reúne projetos e arquivos simples para uso nos vídeos de conexão,
atividades e demonstrações da Formação Iniciante em Programação.

## Estrutura

- `01_sem_persistencia/`
  - versão propositalmente simples do Gerenciador de Estudos;
  - os dados existem somente enquanto o programa está aberto;
  - ideal para demonstrar o problema apresentado no Vídeo de Conexão 04.

- `02_com_persistencia/`
  - versão com persistência em `dados.txt`;
  - usa apenas a biblioteca padrão do Python;
  - ideal para mostrar que os dados continuam disponíveis após fechar o programa.

- `03_projeto_final/`
  - versão organizada para o Projeto Integrador;
  - cadastro, listagem, conclusão, remoção, persistência, funções e README;
  - serve como projeto demonstrativo final.

- `04_repositorio_demo_git/`
  - repositório Git local com histórico de commits pronto para demonstração;
  - pode ser usado nos slides e no Vídeo de Conexão 03.

- `05_banco_de_dados/`
  - modelo SQL simples para a tabela `atividades`;
  - consultas introdutórias compatíveis com a Formação.

- `06_exemplos/`
  - exemplos de pseudocódigo e Python usados nos slides da conexão Lógica → Python.

- `ROTEIRO_DE_TESTES.md`
  - passo a passo para testar cada versão.

## Requisitos

- Python 3.10+ recomendado.
- Nenhuma dependência externa.

## Execução

Entre na pasta desejada e execute:

```bash
python main.py
```

No Windows, dependendo da instalação:

```bash
py main.py
```

> Os projetos foram feitos deliberadamente simples para fins didáticos.
