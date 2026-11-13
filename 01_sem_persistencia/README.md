# Gerenciador de Estudos — Versão 01: Sem Persistência

**Formação Iniciante em Programação | AcademyTeam**

## 1. Apresentação

Este é o primeiro exemplo funcional do **Gerenciador de Estudos**, um pequeno programa executado no terminal para organizar tarefas de aprendizagem. Ele permite **cadastrar, listar e concluir atividades** utilizando conceitos básicos de lógica e Python.

A versão é propositalmente simples: as atividades existem **somente enquanto o programa está aberto**. Quando o programa termina, elas desaparecem. Esse comportamento servirá para entender, na próxima etapa, por que precisamos salvar dados.

**Onde aparece na Formação:** demonstração do planejamento lógico (Atividade 01), aplicação de Python (Atividade 02) e comparação com a persistência (Conexão 04).

## 2. Requisitos e arquivos

- Python 3 instalado (Python 3.10 ou superior recomendado).
- Terminal do sistema ou terminal integrado do VS Code.
- Não requer bibliotecas externas, conexão com a internet nem banco de dados.

```text
01_sem_persistencia/
├── main.py     # Programa executável
└── README.md   # Este guia
```

## 3. Como executar

1. Abra a pasta `01_sem_persistencia` no VS Code.
2. Abra **Terminal → Novo Terminal**.
3. Confirme que o terminal está na pasta onde está `main.py`.
4. Execute:

```bash
python main.py
```

No Windows, caso necessário:

```powershell
py main.py
```

O menu apresenta:

```text
1 - Cadastrar atividade
2 - Listar atividades
3 - Marcar atividade como concluída
0 - Sair
```

Digite uma opção e pressione **Enter**. O programa continua mostrando o menu até você escolher `0`.

## 4. Teste guiado

1. Digite `1` e informe `Estudar Python`.
2. Digite `1` novamente e informe `Revisar algoritmos`.
3. Digite `2`: as duas atividades devem aparecer com o símbolo `○`, indicando que estão pendentes.
4. Digite `3` e informe o ID exibido para `Estudar Python` (normalmente `1`, numa execução nova).
5. Digite `2`: a atividade concluída deverá aparecer com `✓`.
6. Digite `0` para sair.
7. Execute `python main.py` outra vez e escolha `2`.

**Resultado esperado:** aparece a mensagem `Nenhuma atividade cadastrada.`. Isso é proposital: a versão ainda não salva as tarefas.

## 5. Entenda o funcionamento do código

### 5.1. A lista que guarda as atividades

A função `main()` cria uma lista vazia:

```python
atividades = []
```

Uma **lista** guarda vários elementos em ordem. Aqui, cada elemento será um dicionário com informações de uma atividade. Por exemplo:

```python
{
    "id": 1,
    "titulo": "Estudar Python",
    "concluida": False
}
```

Um **dicionário** associa nomes de campos a valores. O campo `concluida` utiliza um valor booleano: `False` para pendente e `True` para concluída.

### 5.2. `mostrar_menu()`: exibir as escolhas

Essa função usa `print()` para apresentar as opções. Ela não cadastra nem altera dados; apenas mostra o que o usuário pode fazer.

### 5.3. `cadastrar(atividades)`: adicionar uma tarefa

A função recebe a lista, pede o título com `input()`, remove espaços nas extremidades com `.strip()` e verifica se a informação está vazia:

```python
titulo = input("Título da atividade: ").strip()
if not titulo:
    print("O título não pode ficar vazio.")
    return
```

Se o título for válido, `append()` acrescenta um dicionário à lista. O ID é calculado com `len(atividades) + 1`: como esta versão não remove registros, ele funciona para a sequência simples apresentada.

### 5.4. `listar(atividades)`: percorrer os registros

A função utiliza `if not atividades` para verificar se a lista está vazia. Quando existem atividades, o `for` percorre os dicionários um a um e mostra seus títulos e estados.

```python
status = "✓" if atividade["concluida"] else "○"
```

Essa expressão escolhe o símbolo conforme o valor de `concluida`. A impressão usa uma **f-string** para incluir informações dentro de um texto.

### 5.5. `concluir(atividades)`: alterar uma tarefa existente

Primeiro, o programa mostra a lista e pede um ID. Depois, transforma o texto recebido em número inteiro:

```python
atividade_id = int(input("ID da atividade concluída: "))
```

Se o usuário digitar letras, `int()` produziria um erro. Por isso, o programa utiliza `try/except ValueError` para exibir `Digite um número válido.` sem encerrar inesperadamente.

O laço `for` procura uma atividade com o ID informado. Quando encontra, altera `concluida` para `True`. Se não encontrar, informa `Atividade não encontrada.`.

### 5.6. `main()`: controlar o programa

O `while True` mantém o programa em execução. A sequência `if` / `elif` identifica a escolha do usuário e chama a função apropriada. A opção `0` executa `break` e termina o laço.

O trecho:

```python
if __name__ == "__main__":
    main()
```

faz `main()` iniciar quando o arquivo é executado diretamente.

## 6. Por que os dados desaparecem?

A lista `atividades` é criada dentro de `main()` toda vez que o programa começa. Ela fica apenas na memória utilizada durante a execução. Como não existe leitura nem gravação em arquivo, o programa não tem de onde recuperar registros anteriores.

**Resumo:** memória temporária não é a mesma coisa que armazenamento permanente. Na **Versão 02**, o programa resolverá esse problema usando `dados.txt`.

## 7. Exercícios para praticar

1. **Básico:** cadastre três atividades e conclua somente a segunda. Confira os símbolos na listagem.
2. **Intermediário:** encontre no código onde o título vazio é rejeitado e teste o comportamento no terminal.
3. **Desafio:** modifique a mensagem exibida quando a lista está vazia. Execute novamente e confira a mudança.
4. **Reflexão:** explique, com suas palavras, a diferença entre o que o usuário vê no menu e os dados que a lista armazena.

## 8. Problemas comuns

- **`python` não é reconhecido:** verifique se o Python está instalado; no Windows, experimente `py main.py`.
- **`can't open file 'main.py'`:** abra o terminal na pasta correta.
- **Título vazio:** informe pelo menos um caractere que não seja espaço.
- **ID inválido ou inexistente:** use o número apresentado na listagem.
- **Acentos/símbolos estranhos:** ajuste o terminal para exibir textos em UTF-8, se necessário.

## 9. Para continuar

Depois de entender como cadastrar, percorrer e alterar atividades, abra a pasta **`02_com_persistencia`**. Você verá como fazer os registros permanecerem disponíveis mesmo após fechar o programa.

> **Dica de aprendizagem:** tente resolver o exercício antes de consultar a solução pronta. O projeto é um exemplo de referência, não um código que precisa ser decorado.
