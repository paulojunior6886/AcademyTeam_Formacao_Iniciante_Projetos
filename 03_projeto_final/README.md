# Gerenciador de Estudos — Projeto Integrador

**Formação Iniciante em Programação | AcademyTeam**

## 1. Sobre o projeto

O **Gerenciador de Estudos** é uma aplicação de terminal feita em Python para organizar atividades de aprendizagem. Ele reúne conteúdos vistos ao longo da Formação: lógica, variáveis, condições, laços, listas, dicionários, funções, arquivos e organização de projetos.

Este é um **modelo de referência**, destinado a mostrar o funcionamento de um software pequeno. O objetivo do aluno é compreender suas decisões e desenvolver, adaptar ou documentar a própria solução — não decorar ou copiar cada linha.

**Importante:** esta aplicação guarda os dados em `dados.txt`. O exemplo de SQL do pacote é uma atividade complementar; o Python desta pasta **não utiliza um banco de dados**.

## 2. O que o programa faz?

| Opção | Funcionalidade | Resultado |
|---|---|---|
| `1` | Cadastrar atividade | Adiciona título, descrição, ID, estado e data |
| `2` | Listar todas | Exibe tarefas pendentes e concluídas |
| `3` | Listar pendentes | Exibe apenas as que ainda não foram concluídas |
| `4` | Concluir atividade | Altera o estado de uma atividade existente |
| `5` | Remover atividade | Exclui uma atividade pelo ID |
| `0` | Sair | Salva os dados e encerra o programa |

Os registros permanecem disponíveis quando o programa é executado novamente.

## 3. Requisitos e arquivos

- Python 3 instalado (Python 3.10+ recomendado).
- VS Code ou terminal do sistema.
- Nenhuma dependência de terceiros.

```text
03_projeto_final/
├── main.py     # Código principal
├── dados.txt   # Registro persistente das atividades
└── README.md   # Guia do projeto
```

**Dica:** o `dados.txt` original desta versão contém apenas o cabeçalho. Faça uma cópia da pasta antes de gravar demonstrações ou testar mudanças.

## 4. Como executar

Abra o terminal na pasta `03_projeto_final` e rode:

```bash
python main.py
```

No Windows, se preferir:

```powershell
py main.py
```

Digite o número da opção desejada e pressione **Enter**. Ao cadastrar uma atividade, você deverá informar um título e poderá adicionar uma descrição.

## 5. Demonstração completa: passo a passo

Para reproduzir o exemplo abaixo, comece com uma cópia de `dados.txt` contendo apenas o cabeçalho. Os IDs podem ser diferentes se já existirem registros.

1. Escolha `1`. Título: `Estudar Python`. Descrição: `Resolver exercícios`.
2. Escolha `1` novamente. Título: `Revisar Git`. Descrição: `Praticar commits`.
3. Escolha `2` para visualizar todas as atividades. Ambas devem aparecer pendentes (`○`).
4. Escolha `3` para listar só as pendentes. As duas devem ser exibidas.
5. Escolha `4` e informe o ID de `Estudar Python` (normalmente `1`). A atividade será marcada como concluída (`✓`).
6. Escolha `3`: agora só `Revisar Git` deve aparecer como pendente.
7. Escolha `5` e informe o ID de `Revisar Git` (normalmente `2`). A atividade será removida.
8. Escolha `2`: apenas `Estudar Python`, já concluída, deverá permanecer.
9. Escolha `0` para encerrar e execute `python main.py` outra vez.
10. Escolha `2`: a atividade restante será recuperada do arquivo.

**Resultado principal:** você demonstrou cadastro, consulta, filtro, atualização, remoção e persistência.

## 6. Como o projeto foi construído?

### 6.1. Organização dos dados

Cada atividade é representada por um **dicionário** Python:

```python
{
    "id": 1,
    "titulo": "Estudar Python",
    "descricao": "Resolver exercícios",
    "concluida": False,
    "data_criacao": "2026-11-13 14:30"
}
```

Os dicionários ficam dentro de uma lista chamada `atividades`. O exemplo de data é ilustrativo; o programa utiliza a data real do momento do cadastro.

### 6.2. O papel de cada função

| Função | Responsabilidade |
|---|---|
| `mostrar_menu()` | Exibir as opções disponíveis |
| `carregar_atividades()` | Ler os registros salvos em `dados.txt` |
| `salvar_atividades(atividades)` | Reescrever o arquivo com o estado atual da lista |
| `proximo_id(atividades)` | Calcular um identificador a partir do maior ID existente |
| `buscar_por_id(atividades, atividade_id)` | Encontrar uma tarefa específica ou retornar `None` |
| `cadastrar(atividades)` | Solicitar dados e adicionar uma atividade |
| `exibir_lista(atividades)` | Mostrar os registros recebidos |
| `listar_todas(atividades)` | Exibir a lista completa |
| `listar_pendentes(atividades)` | Filtrar e mostrar atividades não concluídas |
| `concluir(atividades)` | Alterar o estado para concluído |
| `remover(atividades)` | Excluir uma atividade da lista e salvar |
| `main()` | Carregar dados, mostrar menu e direcionar ações |

### 6.3. Entrada e validação de informações

`input()` recebe textos digitados pelo usuário. O `.strip()` retira espaços nas extremidades. Se o título estiver vazio, o cadastro é cancelado.

Nos campos de ID, o código usa `int()` dentro de `try/except ValueError`. Assim, uma entrada como `abc` gera uma mensagem de orientação em vez de encerrar a execução por erro de conversão.

### 6.4. Cadastrar: uma tarefa nasce pendente

A função `cadastrar()` monta um novo dicionário, atribuindo `False` ao campo `concluida`. Ela usa `proximo_id()` para definir o ID e `datetime.now().strftime(...)` para registrar a data e o horário.

Depois de adicionar o dicionário à lista com `.append()`, chama `salvar_atividades()`, persistindo a mudança.

### 6.5. Listar e filtrar: mostrar o que interessa

A função `exibir_lista()` recebe uma lista e percorre seus itens, exibindo os dados na tela.

A função `listar_todas()` simplesmente apresenta a lista completa. Já `listar_pendentes()` prepara uma lista filtrada:

```python
pendentes = [a for a in atividades if not a["concluida"]]
```

Esse trecho é chamado de **compreensão de lista**: ele percorre as atividades e mantém apenas aquelas cujo estado ainda é `False`. É uma forma compacta de escrever um filtro que também poderia ser feito com `for` e `if`.

### 6.6. Concluir e remover: mudar registros existentes

O programa chama `buscar_por_id()` para encontrar o dicionário correto.

- **Concluir:** altera `atividade["concluida"] = True` e salva a lista.
- **Remover:** utiliza `atividades.remove(atividade)` para retirar o dicionário da lista e salva em seguida.

Se o ID não existir, a mensagem `Atividade não encontrada.` é apresentada. IDs não são posições da lista: o programa procura pelo valor armazenado no campo `id`.

### 6.7. Persistência: manter os dados depois de sair

O programa usa `pathlib.Path` para localizar `dados.txt` ao lado de `main.py`, e `csv.DictReader` / `csv.DictWriter` para carregar e gravar registros separados por `|`.

Exemplo simplificado do arquivo:

```text
id|titulo|descricao|concluida|data_criacao
1|Estudar Python|Resolver exercícios|true|2026-11-13 14:30
```

O arquivo é atualizado depois de cada operação que modifica os dados e também ao encerrar. `true` e `false` são gravados em texto e convertidos em valores booleanos na leitura.

**Atenção:** essa é uma persistência didática. O programa não oferece autenticação, acesso simultâneo por várias pessoas nem banco de dados. Não foi projetado como um sistema multiusuário de produção.

### 6.8. O fluxo geral

```text
Iniciar
  ↓
Carregar dados.txt (ou começar com lista vazia)
  ↓
Exibir menu
  ↓
Receber opção
  ├─ 1: Cadastrar → Salvar → Voltar ao menu
  ├─ 2: Listar todas → Voltar ao menu
  ├─ 3: Listar pendentes → Voltar ao menu
  ├─ 4: Concluir → Salvar → Voltar ao menu
  ├─ 5: Remover → Salvar → Voltar ao menu
  └─ 0: Salvar e encerrar
```

## 7. O que este projeto reúne da Formação?

| Conteúdo estudado | Uso no Gerenciador |
|---|---|
| Algoritmos e lógica | Planejamento das opções e operações |
| Variáveis e tipos | IDs, títulos, descrições e estados |
| Condicionais | Escolha no menu e validação das entradas |
| Repetições | Menu com `while` e listagem com `for` |
| Listas e dicionários | Armazenamento das tarefas em memória |
| Funções | Divisão do programa em pequenas responsabilidades |
| Arquivos | Gravação e leitura de `dados.txt` |
| Git e GitHub | Versionamento e documentação, realizados separadamente |
| SQL | Modelo complementar de como esses dados poderiam virar tabela |

O código-fonte desta pasta **não implementa comandos Git nem SQL**: são conhecimentos utilizados nas atividades de organização e modelagem do projeto.

## 8. Desafios de aprendizagem

**Nível 1 — Compreensão**
1. Cadastre três tarefas e conclua uma delas.
2. Explique a diferença entre as opções `2` e `3`.
3. Identifique no código onde cada ação do menu chama uma função.

**Nível 2 — Modificação**
4. Altere uma mensagem do menu sem modificar as funcionalidades.
5. Adicione uma confirmação antes da remoção de atividades.
6. Crie uma nova opção para exibir a quantidade de tarefas pendentes.

**Nível 3 — Extensão opcional**
7. Acrescente um campo de prioridade (baixa, média, alta), adaptando a leitura e a gravação do arquivo.
8. Crie uma pesquisa pelo título das atividades.
9. Modele esses dados como uma tabela SQL, usando a pasta `05_banco_de_dados` como referência.

As atividades de nível 3 exigem alterações adicionais e **não fazem parte das funcionalidades já implementadas**.

## 9. Problemas comuns e cuidados

- **Não encontrou `main.py`:** execute o comando dentro da pasta correta.
- **`dados.txt` tem informações antigas:** use uma cópia limpa para repetir a demonstração.
- **ID não encontrado:** confira o ID exibido; não confunda ID com posição.
- **Uma atividade permanece após reiniciar:** é o comportamento esperado da persistência.
- **Arquivo foi alterado manualmente e parou de funcionar:** recupere a cópia do `dados.txt` ou o formato correto de cabeçalho e colunas.
- **Removeu o último ID e cadastrou outro:** o programa calcula o próximo ID a partir do maior **ID ainda existente**; em um exemplo didático, números removidos podem voltar a ser usados. Em sistemas reais, geralmente se emprega uma estratégia mais robusta.
- **Quer publicar no GitHub:** inclua o código e o README, mas evite publicar registros pessoais ou arquivos com informações sensíveis.

## 10. Próximos passos

Depois de executar o Gerenciador, siga para `04_repositorio_demo_git` para entender seu histórico de versões, e `05_banco_de_dados` para conhecer uma representação alternativa dos registros em SQL.

> **Objetivo final:** ser capaz de explicar o que o programa faz, executar suas funções, identificar onde cada conceito aparece e realizar pelo menos uma pequena modificação por conta própria.
