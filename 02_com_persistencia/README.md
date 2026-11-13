# Gerenciador de Estudos — Versão 02: Com Persistência

**Formação Iniciante em Programação | AcademyTeam**

## 1. Apresentação

A primeira versão do Gerenciador de Estudos guardava as atividades apenas na memória: elas desapareciam quando o programa era encerrado. Nesta versão, o programa passa a **salvar as informações no arquivo `dados.txt`** e a recuperá-las quando é aberto novamente.

Além de título e situação de conclusão, cada atividade possui **descrição e data de criação**.

**Onde aparece na Formação:** Conexão 04 (persistência), demonstração de evolução do Gerenciador e preparação para o Projeto Integrador.

## 2. Requisitos e estrutura

- Python 3 instalado (3.10 ou superior recomendado).
- Terminal ou VS Code.
- Nenhuma biblioteca externa, conexão com a internet ou servidor de banco de dados.

```text
02_com_persistencia/
├── main.py     # Código principal
├── dados.txt   # Arquivo com registros das atividades
└── README.md   # Este guia
```

**Atenção:** o pacote já traz atividades de exemplo em `dados.txt`. Faça uma cópia da pasta antes de realizar alterações. Se você usar a mesma pasta para gravar vídeos, seus testes modificarão os dados demonstrativos.

## 3. Como executar

Entre na pasta `02_com_persistencia` pelo terminal e rode:

```bash
python main.py
```

No Windows, também pode funcionar:

```powershell
py main.py
```

O programa informa quantas atividades foram carregadas e apresenta as opções:

```text
1 - Cadastrar atividade
2 - Listar atividades
3 - Marcar atividade como concluída
0 - Sair
```

## 4. Teste guiado: comprovar que os dados ficam salvos

1. Execute o programa e digite `2` para observar os registros carregados.
2. Digite `1` e informe o título `Preparar atividade prática`.
3. Quando solicitado, informe a descrição `Testar gravação em arquivo`.
4. Digite `2` para conferir o novo registro. Observe também a data de criação.
5. Digite `0` para sair.
6. Execute `python main.py` novamente.
7. Digite `2` e confirme que `Preparar atividade prática` continua na lista.
8. Abra `dados.txt` em um editor de texto e procure a nova linha.

**Resultado esperado:** a atividade continua disponível após reiniciar porque foi gravada no arquivo.

## 5. Entenda as informações de uma atividade

O programa representa cada tarefa com um dicionário semelhante a:

```python
{
    "id": 4,
    "titulo": "Preparar atividade prática",
    "descricao": "Testar gravação em arquivo",
    "concluida": False,
    "data_criacao": "2026-11-13 14:30"
}
```

O número do ID e a data acima são apenas exemplos; o programa calcula os valores conforme o conteúdo existente e o momento do cadastro.

| Campo | Significado |
|---|---|
| `id` | Identificador numérico da atividade |
| `titulo` | Nome curto da tarefa |
| `descricao` | Detalhes opcionais |
| `concluida` | `True` para concluída; `False` para pendente |
| `data_criacao` | Data e horário registrados no cadastro |

## 6. Como o arquivo `dados.txt` funciona?

O programa usa um **arquivo de texto estruturado**, no qual a primeira linha contém os nomes dos campos e cada linha seguinte representa uma atividade. O caractere `|` é usado como separador:

```text
id|titulo|descricao|concluida|data_criacao
1|Estudar Python|Revisar estruturas de repetição|true|2026-08-14 14:00
```

É importante diferenciar esse arquivo de um banco SQL: embora os dados estejam organizados em colunas, **o programa ainda não se conecta a um banco de dados**.

Evite alterar manualmente os nomes dos campos ou remover separadores, pois o código espera essa organização ao carregar o arquivo.

## 7. Entenda as partes principais do código

### 7.1. `Path`: localizar o arquivo

```python
ARQUIVO_DADOS = Path(__file__).with_name("dados.txt")
```

O módulo `pathlib` ajuda a trabalhar com caminhos de arquivos. Esse trecho indica que `dados.txt` fica **na mesma pasta do `main.py`**, mesmo quando o programa é executado a partir de outro diretório.

### 7.2. `carregar_atividades()`: recuperar registros

Essa função começa verificando se o arquivo existe. Se não existir, devolve uma lista vazia.

Quando o arquivo existe, o código usa `csv.DictReader(..., delimiter="|")`. Apesar do nome `csv`, podemos escolher o delimitador; neste projeto é `|`, não vírgula.

Cada linha do arquivo é transformada em um dicionário Python. O texto do ID é convertido em `int`, e o campo `concluida` é convertido de texto (`"true"` ou `"false"`) para valor booleano.

### 7.3. `salvar_atividades(atividades)`: escrever registros

A função usa `csv.DictWriter` para gravar a lista no arquivo. Ela escreve o cabeçalho e, em seguida, todas as atividades. O arquivo é aberto no modo `"w"`, que **reescreve seu conteúdo** com a versão atual da lista.

O trecho:

```python
"concluida": str(atividade["concluida"]).lower()
```

converte o valor booleano para `true` ou `false` em minúsculas, no formato utilizado pelo arquivo.

A gravação acontece ao **cadastrar**, ao **concluir** uma atividade e também ao **sair** do programa.

### 7.4. `proximo_id(atividades)`: escolher um identificador

```python
return max((a["id"] for a in atividades), default=0) + 1
```

A expressão observa os IDs existentes, encontra o maior e soma 1. Caso não existam atividades, utiliza 0 como referência, então o primeiro ID será 1.

Essa expressão é uma forma compacta de percorrer os IDs. Não é necessário decorá-la agora; o importante é entender sua finalidade.

### 7.5. `cadastrar(atividades)`: registrar uma tarefa nova

Essa função pede título e descrição, valida o título, define o estado inicial como `False`, registra a data atual com `datetime.now()` e chama `salvar_atividades()` depois de adicionar o registro à lista.

### 7.6. `listar(atividades)`: mostrar tarefas

Um `for` percorre os dicionários, mostrando ID, estado, título, data de criação e descrição quando preenchida.

### 7.7. `concluir(atividades)`: atualizar uma tarefa

A função lê um ID, trata entradas não numéricas usando `try/except ValueError`, procura o registro correspondente, altera `concluida` para `True` e **salva imediatamente** a lista atualizada.

### 7.8. `main()`: iniciar carregando o arquivo

A principal diferença em relação à versão anterior é esta:

```python
atividades = carregar_atividades()
```

O programa não começa mais obrigatoriamente com uma lista vazia. Ele começa com os dados recuperados do arquivo, quando disponíveis.

## 8. Exercícios para praticar

1. Cadastre uma tarefa, feche o programa e confirme que ela reaparece ao abrir novamente.
2. Conclua uma tarefa, saia e reabra. Verifique se o estado de conclusão foi preservado.
3. Compare a lista de dicionários usada pelo Python com as linhas de `dados.txt`.
4. **Desafio:** identifique em quais três situações o programa chama `salvar_atividades()`.
5. **Reflexão:** por que apenas colocar o código dentro de `try/except` não resolveria o problema de perder os dados?

## 9. Dificuldades comuns

- **Arquivo não encontrado:** se `dados.txt` não existir, o programa começa com lista vazia e o recria quando salvar.
- **Dados de exemplo aparecendo:** a pasta original já vem com registros; use uma cópia se quiser começar do zero.
- **Arquivo editado incorretamente:** alterações indevidas no cabeçalho ou nas colunas podem impedir a leitura. Recupere uma cópia do original.
- **Tarefa não mudou de estado:** confira se você digitou o ID realmente exibido.
- **Erro ao executar:** verifique a instalação do Python e a pasta aberta no terminal.

## 10. Para continuar

A próxima etapa reúne persistência, filtros e remoção de atividades no **`03_projeto_final`**. Lá você verá a organização de um programa um pouco mais completo, mas construído com os mesmos fundamentos.

> **Aprenda por etapas:** primeiro compreenda o problema que cada versão resolve; depois estude as partes do código e tente modificar pequenas funcionalidades.
