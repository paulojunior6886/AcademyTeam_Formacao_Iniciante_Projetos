# Gerenciador de Estudos — Introdução à Modelagem de Dados e SQL

**Formação Iniciante em Programação | AcademyTeam**

## 1. Por que existe esta atividade?

Até aqui, o Gerenciador de Estudos armazenou informações em uma lista Python e, depois, no arquivo `dados.txt`. Nesta etapa, vamos imaginar como esses mesmos dados poderiam ser organizados em uma **tabela de banco de dados**.

A atividade apresenta conceitos de **tabela, campo, registro, chave primária e comandos SQL**. Não é necessário conectar o Python ao banco de dados.

**Onde aparece na Formação:** Módulo de Dados e SQL, Atividade 04 e revisão do Projeto Integrador.

## 2. Arquivos disponíveis

```text
05_banco_de_dados/
├── schema.sql        # Modelo da tabela e exemplos SQL
├── modelo_tabela.md  # Explicação dos campos
└── README.md         # Este guia didático
```

É possível estudar o material apenas abrindo esses arquivos no VS Code ou em outro editor de texto. Executar as instruções SQL é opcional.

## 3. Conheça os dados da atividade

Cada atividade possui cinco informações:

| Campo | Tipo no exemplo SQL | Para que serve? |
|---|---|---|
| `id` | `INTEGER` | Identificar cada atividade |
| `titulo` | `VARCHAR(150)` | Guardar o nome da atividade |
| `descricao` | `VARCHAR(500)` | Registrar detalhes opcionais |
| `concluida` | `BOOLEAN` | Indicar se a tarefa está concluída |
| `data_criacao` | `TIMESTAMP` | Registrar quando a atividade foi criada |

Uma **tabela** organiza registros em linhas e campos em colunas. Cada linha representa uma atividade; cada coluna descreve uma característica dessa atividade.

O campo `id` é usado como **chave primária**, isto é, um identificador que distingue uma atividade das demais dentro da tabela.

## 4. `CREATE TABLE`: criar a estrutura

O arquivo `schema.sql` começa com:

```sql
CREATE TABLE atividades (
    id INTEGER PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descricao VARCHAR(500),
    concluida BOOLEAN NOT NULL DEFAULT FALSE,
    data_criacao TIMESTAMP NOT NULL
);
```

Entenda as partes:

- `CREATE TABLE atividades`: cria uma tabela chamada `atividades`.
- `INTEGER PRIMARY KEY`: define `id` como chave primária inteira.
- `VARCHAR(150)` e `VARCHAR(500)`: expressam a intenção de armazenar textos de determinados tamanhos.
- `NOT NULL`: indica que um campo não pode ficar sem valor SQL (`NULL`).
- `DEFAULT FALSE`: define o estado inicial como pendente, caso ele não seja informado na inserção.
- `TIMESTAMP`: representa a informação de data e horário de criação.

**Nota:** o exemplo usa SQL introdutório compatível com SQLite para os testes sugeridos. O SQLite possui particularidades na interpretação de tipos, como `BOOLEAN`, `VARCHAR` e `TIMESTAMP`; esse arquivo não é um projeto completo de modelagem ou validação de dados.

## 5. `SELECT`: consultar atividades

Para ver todas as linhas da tabela:

```sql
SELECT * FROM atividades;
```

O símbolo `*` significa selecionar todas as colunas.

Para consultar apenas tarefas pendentes:

```sql
SELECT * FROM atividades
WHERE concluida = FALSE;
```

`WHERE` acrescenta uma condição. Nesse caso, a consulta retorna apenas atividades cujo campo `concluida` representa falso.

## 6. `INSERT`: cadastrar uma atividade

O arquivo demonstra a inserção de um registro:

```sql
INSERT INTO atividades (id, titulo, descricao, concluida, data_criacao)
VALUES (
    1,
    'Estudar Python',
    'Revisar estruturas de repetição',
    FALSE,
    CURRENT_TIMESTAMP
);
```

`INSERT INTO` indica a tabela e os campos que receberão valores. `VALUES` informa os dados correspondentes. `CURRENT_TIMESTAMP` representa o horário atual fornecido pelo banco.

Neste exemplo, o ID `1` é informado explicitamente. Para cadastrar mais atividades, não reutilize um ID já existente.

## 7. `UPDATE`: marcar uma tarefa como concluída

```sql
UPDATE atividades
SET concluida = TRUE
WHERE id = 1;
```

`UPDATE` indica que vamos modificar um registro; `SET` define o novo valor; `WHERE id = 1` limita a mudança à atividade identificada pelo ID 1.

**Atenção:** sem a condição `WHERE`, um `UPDATE` pode alterar várias linhas da tabela. Esse é um motivo importante para compreender o identificador e os filtros.

## 8. Uma execução guiada em ordem didática

A ordem de leitura dos exemplos no `schema.sql` não equivale à melhor ordem para observar resultados no banco: algumas consultas estão **antes** do `INSERT`. Se você executar a tabela recém-criada e consultar imediatamente, ela estará vazia.

Para praticar e visualizar uma atividade, utilize esta sequência:

1. Execute o `CREATE TABLE`.
2. Execute o `INSERT`.
3. Execute `SELECT * FROM atividades;` para conferir o registro.
4. Execute `SELECT * FROM atividades WHERE concluida = FALSE;` para ver a pendente.
5. Execute o `UPDATE` para marcar o ID 1 como concluído.
6. Repita os `SELECT` para comparar os resultados.

**Resultado esperado:** antes do `UPDATE`, a atividade aparece como pendente; depois, continua na listagem geral, mas deixa de aparecer no filtro de pendentes.

## 9. Como testar sem instalar um servidor de banco?

Para uma demonstração opcional, você pode usar o módulo `sqlite3` incluído na biblioteca padrão do Python. Abra o terminal dentro de `05_banco_de_dados` e execute:

```bash
python -c "import sqlite3, pathlib; c=sqlite3.connect(':memory:'); c.executescript(pathlib.Path('schema.sql').read_text(encoding='utf-8')); print(c.execute('SELECT id, titulo, concluida FROM atividades').fetchall()); c.close()"
```

No Windows, você pode substituir `python` por `py`.

Esse comando cria um banco **temporário na memória**, executa o conteúdo de `schema.sql` e mostra os registros encontrados após a execução. Como o arquivo SQL contém um `INSERT` e um `UPDATE`, a atividade demonstrativa deverá aparecer como concluída (representada geralmente por `1` em SQLite).

Esse teste **não cria uma integração entre o aplicativo Python do Gerenciador e um banco de dados**. Ele apenas executa separadamente o exemplo SQL.

Se o comando parecer avançado, não se preocupe: para esta atividade, o foco está em entender os comandos presentes no `schema.sql`.

## 10. Comparação: lista, arquivo e tabela

| Forma de guardar informação | Como o projeto utiliza | Limitação principal neste exemplo |
|---|---|---|
| Lista Python | Dados em memória na Versão 01 | Perde tudo ao encerrar |
| Arquivo `dados.txt` | Dados persistentes nas Versões 02 e Final | Requer leitura e regravação do arquivo inteiro |
| Tabela SQL | Modelo demonstrativo nesta pasta | Não está conectada ao aplicativo Python |

**Resumo:** são formas diferentes de representar e armazenar dados. O exemplo SQL ajuda a entender o próximo passo possível, mas não significa que todo aplicativo iniciante precise de um banco de dados.

## 11. Atividade proposta

Imagine que você queira guardar as tarefas de estudo de uma turma.

1. Explique a finalidade dos campos `id`, `titulo`, `descricao`, `concluida` e `data_criacao`.
2. Identifique qual campo funciona como chave primária e por quê.
3. Escreva um `SELECT` para consultar todas as atividades.
4. Escreva outro `SELECT` que mostre apenas atividades pendentes.
5. Escreva um `UPDATE` que conclua uma atividade pelo ID.
6. **Desafio:** escreva um `INSERT` para cadastrar uma segunda tarefa, usando um ID diferente de 1.
7. **Reflexão:** que vantagens uma tabela de banco de dados pode oferecer quando o sistema e a quantidade de registros aumentam?

**Resultado esperado:** compreender a estrutura da tabela e as operações introdutórias de consulta, inserção e atualização.

## 12. Problemas comuns

- **`no such table: atividades`:** a tabela ainda não foi criada no banco utilizado.
- **Chave primária repetida:** você tentou inserir outro registro com um ID já existente.
- **Consulta não retornou registros:** a tabela pode estar vazia, ou não existem linhas que atendam ao `WHERE`.
- **`table atividades already exists`:** você repetiu o `CREATE TABLE` em um banco que já possui a tabela.
- **Resultado diferente entre programas:** o banco temporário desta demonstração e o `dados.txt` do Gerenciador são independentes; não compartilham registros automaticamente.

## 13. Para continuar

Utilize o modelo SQL como referência conceitual. No Projeto Integrador da Formação, a persistência obrigatória continua sendo feita em arquivo; conectar a aplicação a um banco de dados é **uma evolução opcional para estudos futuros**.

> **O mais importante nesta etapa:** saber o que é uma tabela, reconhecer seus campos e explicar o propósito de `CREATE TABLE`, `SELECT`, `INSERT`, `UPDATE` e `WHERE`.
