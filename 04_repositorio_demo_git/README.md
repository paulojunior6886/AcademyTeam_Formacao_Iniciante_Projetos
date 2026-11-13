# Gerenciador de Estudos — Demonstração de Git e Versionamento

**Formação Iniciante em Programação | AcademyTeam**

## 1. Qual é o objetivo desta pasta?

Este diretório contém uma versão funcional do Gerenciador de Estudos e um **repositório Git local com histórico de commits**. Seu propósito é mostrar que um projeto de software pode evoluir por etapas e que o Git permite registrar essas mudanças.

**Onde aparece na Formação:** Conexão 03 (organização de projeto) e Atividade 03 (Git e GitHub).

**Importante:** este é um repositório **local** de demonstração. A existência do histórico Git não significa que ele já esteja publicado no GitHub.

## 2. Requisitos e arquivos

- Python 3 para executar `main.py`.
- Git instalado para usar `git log`, `git status` e outros comandos.
- Terminal ou VS Code.

```text
04_repositorio_demo_git/
├── .git/                  # Histórico e configurações locais do Git
├── main.py                # Programa Python
├── dados.txt              # Atividades armazenadas
├── README.md              # Este guia
└── HISTORICO_COMMITS.txt  # Resumo de parte do histórico
```

A pasta `.git` costuma ficar **oculta**. Verifique se ela veio junto com a extração do pacote; sem ela, o comando `git log` não encontrará o histórico de demonstração.

## 3. Como explorar o histórico do projeto

Abra um terminal **dentro de `04_repositorio_demo_git`** e execute:

```bash
git log --oneline
```

O comando mostra commits do mais recente para o mais antigo, com um identificador curto e uma mensagem descritiva.

Para visualizar a evolução em ordem cronológica:

```bash
git log --oneline --reverse
```

O pacote registra etapas como:

1. Estrutura inicial do projeto.
2. Cadastro de atividades.
3. Listagem de atividades.
4. Conclusão de atividades.
5. Persistência e documentação.
6. Inclusão de um resumo textual do histórico.

O arquivo `HISTORICO_COMMITS.txt` reúne as cinco etapas principais; o histórico real também contém um commit posterior relacionado à documentação.

### Outros comandos úteis

```bash
git status
```

Mostra arquivos alterados, não rastreados e o estado da pasta de trabalho. Se você executou o Python, podem aparecer arquivos de `__pycache__`; isso não significa que o projeto esteja com defeito.

```bash
git show --stat HEAD
```

Mostra um resumo dos arquivos envolvidos no commit mais recente.

```bash
git log --oneline --max-count=3
```

Exibe apenas os três commits mais recentes.

## 4. Como executar o programa Python

Dentro da mesma pasta:

```bash
python main.py
```

Ou, no Windows:

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

Assim como na versão `02_com_persistencia`, as atividades são gravadas em `dados.txt` e recuperadas ao abrir o programa novamente. **O Git e a execução do Python são duas coisas diferentes:** o Git registra versões do código; o arquivo de dados armazena as atividades do usuário.

## 5. Entenda os conceitos essenciais

### Repositório

É a pasta de projeto acompanhada pelo Git. O diretório `.git` guarda o histórico e as informações necessárias ao versionamento.

### Commit

É um registro de uma etapa do trabalho. Uma mensagem de commit deve explicar de forma clara o que mudou, por exemplo: `Adiciona cadastro de atividades`.

### Histórico

É a sequência de commits que ajuda a entender como o programa foi construído ao longo do tempo. Para visualizar esse histórico, usamos `git log`.

### Arquivo rastreado e não rastreado

Um arquivo **rastreado** é conhecido pelo Git. Um arquivo **não rastreado** está na pasta, mas ainda não foi adicionado ao controle de versão. `git status` permite distinguir essas situações.

### Git não é GitHub

**Git** é a ferramenta de controle de versão. **GitHub** é um serviço que pode hospedar repositórios e facilitar o compartilhamento e a colaboração. Você pode usar Git localmente sem ter uma conta no GitHub.

### README

O `README.md` é um documento em Markdown usado para apresentar o projeto, explicar como executá-lo e orientar outras pessoas. É parte importante da organização e da comunicação técnica.

## 6. Como o histórico ajuda a entender a evolução?

Imagine a construção gradual do Gerenciador:

```text
Menu inicial
   ↓
Cadastro
   ↓
Listagem
   ↓
Conclusão
   ↓
Persistência de dados
```

Em vez de manter arquivos chamados `programa_final.py`, `programa_final2.py` e `programa_agora_vai.py`, podemos registrar mudanças com commits e consultar o histórico quando necessário.

**Atenção:** o repositório demonstra essa sequência, mas não substitui a necessidade de compreender e testar cada versão.

## 7. Atividade guiada — Criar seu próprio histórico

O exemplo pronto serve para observação. Para praticar de verdade, use **uma cópia do seu próprio Gerenciador**, em outra pasta:

1. Abra a pasta do seu projeto.
2. Inicie um repositório local:

```bash
git init
```

3. Adicione os arquivos desejados:

```bash
git add main.py README.md
```

4. Crie o primeiro commit:

```bash
git commit -m "Versao inicial do Gerenciador"
```

5. Faça uma pequena alteração no código ou no README.
6. Confira o que mudou:

```bash
git status
git diff
```

7. Adicione os arquivos alterados e registre outro commit:

```bash
git add main.py README.md
git commit -m "Melhora as instrucoes do projeto"
```

8. Confira o histórico:

```bash
git log --oneline
```

Se o Git pedir identificação de autor, configure seu nome e e-mail conforme as instruções exibidas no terminal. Para iniciar o exercício, não é obrigatório publicar na internet.

## 8. Como publicar no GitHub? (Etapa opcional)

Depois de criar um repositório vazio em sua conta do GitHub, siga as instruções que a plataforma apresentar para conectar seu repositório local. Um fluxo comum é:

```bash
git branch -M main
git remote add origin URL_DO_SEU_REPOSITORIO
git push -u origin main
```

Substitua `URL_DO_SEU_REPOSITORIO` pelo endereço verdadeiro. O envio exigirá autenticação adequada no GitHub. Não execute `git remote add origin` sobre o repositório demonstrativo sem entender as configurações existentes; prefira sua cópia pessoal.

**Segurança:** não envie senhas, chaves, dados pessoais ou arquivos que não devem ser públicos. Uma boa prática é usar `.gitignore` para ignorar arquivos temporários, como `__pycache__/`.

## 9. Desafios para praticar

1. Encontre no `git log` o commit que adicionou a persistência.
2. Explique a diferença entre `git status` e `git log`.
3. Crie um repositório próprio com pelo menos dois commits feitos em momentos distintos.
4. Melhore o README do seu projeto para explicar as funcionalidades e a execução.
5. **Opcional:** publique seu repositório no GitHub e confira se o histórico aparece na plataforma.

## 10. Problemas comuns

- **`git` não é reconhecido:** instale o Git e abra novamente o terminal.
- **`not a git repository`:** confirme que você está dentro da pasta certa e que `.git` foi extraída.
- **Arquivos temporários no `git status`:** a execução de Python pode criar `__pycache__/`; não é necessário versioná-los.
- **Commit solicita nome/e-mail:** configure a identidade do Git antes de continuar.
- **`git push` falhou:** verifique o endereço do remoto, a conexão e a autenticação da conta; o repositório local continua disponível.

## 11. Para continuar

Acompanhe o Projeto Integrador em `03_projeto_final` e utilize o Git para registrar sua própria evolução. O objetivo é conseguir explicar **o que mudou**, **por que mudou** e **em qual etapa** cada recurso foi adicionado.

## Como consultar o histórico Git original

O histórico didático deste projeto está disponível no arquivo
`06_exemplos/historico_git_demo.bundle`.

A partir da raiz do repositório da Formação, execute:

```bash
git clone 06_exemplos/historico_git_demo.bundle ../Exemplo_Git_Historico
cd ../Exemplo_Git_Historico
git log --oneline

