# 🛠️ AcademyTeam — Manual de instalação e preparação do ambiente

**Formação Iniciante em Programação — Do Problema ao Primeiro Projeto**  
**Material de apoio aos cursos de Algoritmos, Python, Git e GitHub, Banco de Dados e ao Projeto Integrador**

> **Para quem é este manual?** Para quem nunca programou ou ainda não instalou as ferramentas necessárias. Acompanhe as etapas na ordem e faça os testes indicados antes de avançar.

> **Importante:** este guia apresenta o passo a passo principal para **Windows 10/11** e orientações resumidas para **macOS e Linux**. Os nomes dos botões podem mudar um pouco entre versões dos programas.

---

## 📌 Índice

1. [Quais ferramentas serão utilizadas?](#1-quais-ferramentas-serão-utilizadas)
2. [Antes de começar](#2-antes-de-começar)
3. [Instalar o Python](#3-instalar-o-python)
4. [Instalar o Visual Studio Code](#4-instalar-o-visual-studio-code)
5. [Configurar o Python no VS Code](#5-configurar-o-python-no-vs-code)
6. [Instalar e configurar o Git](#6-instalar-e-configurar-o-git)
7. [Criar uma conta no GitHub](#7-criar-uma-conta-no-github)
8. [Instalar PostgreSQL e pgAdmin 4](#8-instalar-postgresql-e-pgadmin-4)
9. [Criar o banco e executar o SQL do curso](#9-criar-o-banco-e-executar-o-sql-do-curso)
10. [Baixar e abrir os projetos da AcademyTeam](#10-baixar-e-abrir-os-projetos-da-academyteam)
11. [Executar as versões do Gerenciador de Estudos](#11-executar-as-versões-do-gerenciador-de-estudos)
12. [Testar o histórico Git](#12-testar-o-histórico-git)
13. [Instalação em macOS e Linux](#13-instalação-em-macos-e-linux)
14. [Problemas comuns e soluções](#14-problemas-comuns-e-soluções)
15. [Checklist de ambiente pronto](#15-checklist-de-ambiente-pronto)
16. [Sites e documentação oficiais](#16-sites-e-documentação-oficiais)

---

## 1. Quais ferramentas serão utilizadas?

| Ferramenta | Para que serve? | Precisa instalar? | Quando usar? |
|---|---|---|---|
| **Python 3** | Executar os programas e praticar programação | **Sim**, nos exercícios Python | Módulo de Python e Projeto Integrador |
| **Visual Studio Code (VS Code)** | Abrir pastas, editar arquivos e utilizar um terminal integrado | **Recomendado** | Durante toda a Formação |
| **Extensão Python (Microsoft)** | Melhorar a edição e a execução de código Python no VS Code | **Recomendada** | Módulo de Python |
| **Git** | Criar repositórios e registrar versões do código | **Sim**, para as atividades de Git | Módulo Git e GitHub |
| **GitHub** | Hospedar e compartilhar repositórios pela internet | **Conta gratuita** | Módulo Git e GitHub |
| **PostgreSQL** | Criar e utilizar um banco de dados relacional real | **Opcional** para o Gerenciador; útil para a prática de SQL | Módulo Banco de Dados |
| **pgAdmin 4** | Gerenciar o PostgreSQL por uma interface gráfica | **Opcional**, junto com PostgreSQL | Módulo Banco de Dados |
| **Navegador** | Acessar cursos, documentação e GitHub | Normalmente já instalado | Durante toda a Formação |
| **Descompactador ZIP** | Extrair os materiais baixados | Windows geralmente já tem um | Preparação dos projetos |

### O que não precisa instalar?

Os projetos `01_sem_persistencia`, `02_com_persistencia` e `03_projeto_final` usam **somente a biblioteca padrão do Python**. Por isso, **não é necessário instalar pacotes com `pip`**, criar um servidor web, usar Docker ou configurar um banco de dados para executá-los.

O **PostgreSQL não está conectado ao Gerenciador de Estudos Python**. A pasta `05_banco_de_dados` apresenta um modelo SQL **complementar**, para praticar tabelas e consultas.

**Se você ainda está estudando Algoritmos ou Python:** comece pelas seções **2 a 5**, pule para a seção **10** e execute o primeiro projeto. Instale o restante quando chegar aos módulos correspondentes.

---

## 2. Antes de começar

1. Tenha acesso à internet para baixar os programas.
2. Verifique se há espaço livre suficiente no computador; o PostgreSQL pode exigir mais espaço do que os demais programas.
3. Crie uma pasta de estudos, por exemplo: `Documentos\AcademyTeam`.
4. Baixe os materiais somente de **sites oficiais** ou do repositório indicado pela AcademyTeam.
5. Se o computador for de escola ou laboratório e bloquear instalações, solicite autorização ao responsável pelo equipamento.

**Dica:** não é obrigatório instalar todas as ferramentas de uma vez. Instale por etapa para evitar confusões.

---

## 3. Instalar o Python

**Página oficial:** https://www.python.org/downloads/

### Passo a passo — Windows

1. Acesse o endereço acima.
2. Baixe o instalador recomendado para seu Windows. Utilize uma versão estável, ainda suportada e compatível com seu Windows. Os projetos funcionam com **Python 3.10 ou superior**, mas prefira uma versão mais recente que ainda receba atualizações de segurança.
3. Execute o instalador baixado. As telas dependem da versão do instalador:
   - Se aparecer **Add Python to PATH**, marque essa opção.
   - Se o instalador oferecer um **Python Install Manager**, siga as instruções para instalar uma versão do Python 3; nesse modelo, os comandos `py` e/ou `python` poderão ser configurados pelo gerenciador.
4. Conclua a instalação.
5. Feche e reabra o terminal, caso ele já estivesse aberto.

### Testar a instalação

Abra o **PowerShell** ou o **Prompt de Comando** do Windows e digite:

```powershell
py --version
```

Se não funcionar, teste:

```powershell
python --version
```

**Resultado esperado:** a versão instalada, por exemplo `Python 3.x.x`.

Para testar o interpretador:

```powershell
py -c "print('Python funcionando!')"
```

Ou substitua `py` por `python`, se esse for o comando reconhecido no seu computador.

**Atenção:** a versão específica mostrada no seu terminal pode ser diferente do exemplo. O importante é que o programa execute sem erro.

---

## 4. Instalar o Visual Studio Code

**Página oficial:** https://code.visualstudio.com/download

### Passo a passo — Windows

1. Acesse a página oficial.
2. Escolha a versão do **Visual Studio Code para Windows**. Para uso pessoal, o **User Installer** normalmente é suficiente.
3. Execute o instalador.
4. Aceite os termos e prossiga pelas etapas.
5. Se aparecerem opções como **Adicionar ao PATH** e **Abrir com o Code**, você pode habilitá-las para facilitar o uso.
6. Conclua a instalação e abra o VS Code.

### Conhecendo as partes principais

- **Explorador:** mostra as pastas e arquivos do projeto.
- **Editor:** área central onde os arquivos são abertos.
- **Terminal:** permite executar comandos sem sair do VS Code.
- **Extensões:** permite instalar recursos de suporte à linguagem Python.

Para abrir o terminal, utilize **Terminal > Novo Terminal**. O atalho costuma ser **Ctrl + Shift + tecla de acento grave** (`).

> O VS Code é o **editor**. Ele não instala automaticamente o interpretador Python, o Git nem o PostgreSQL.

---

## 5. Configurar o Python no VS Code

### Instalar a extensão oficial

1. Abra o VS Code.
2. Clique em **Extensões** na barra lateral ou pressione `Ctrl + Shift + X`.
3. Pesquise por **Python**.
4. Escolha a extensão **Python**, publicada pela **Microsoft**.
5. Clique em **Instalar**.
6. Aguarde a instalação. Recursos complementares podem ser sugeridos ou instalados automaticamente.

### Selecionar o interpretador

1. Pressione `Ctrl + Shift + P`.
2. Digite `Python: Select Interpreter`.
3. Selecione a instalação de Python 3 que você acabou de configurar.
4. Se não aparecer nenhuma, confirme primeiro se o Python funciona no terminal (seção 3) e reinicie o VS Code.

### Seu primeiro teste no VS Code

1. Crie uma pasta chamada `teste_python` em `Documentos\AcademyTeam`.
2. No VS Code, vá em **Arquivo > Abrir Pasta** e selecione essa pasta.
3. Crie o arquivo `ola.py`.
4. Cole este conteúdo:

```python
print("Olá, AcademyTeam!")
```

5. Salve com `Ctrl + S`.
6. Abra o terminal e execute:

```powershell
py ola.py
```

Se necessário, utilize `python ola.py`.

**Resultado esperado:** `Olá, AcademyTeam!`.

Você também pode utilizar o botão de execução do arquivo Python no VS Code, desde que o interpretador correto esteja selecionado.

---

## 6. Instalar e configurar o Git

**Página oficial:** https://git-scm.com/install/

### Passo a passo — Windows

1. Acesse a página oficial do Git.
2. Escolha **Windows** e baixe o instalador compatível com seu computador.
3. Execute o instalador.
4. Para esta Formação, as **configurações padrão** geralmente são suficientes. Caso apareça uma tela sobre integração do Git com o terminal, mantenha uma opção que permita usá-lo na linha de comando.
5. Conclua a instalação.
6. Feche e reabra o VS Code e seus terminais.

### Testar o Git

```powershell
git --version
```

**Resultado esperado:** `git version ...`.

### Identificar seus commits

Configure um nome e um e-mail que você queira associar aos seus commits:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
```

**Substitua** esses valores pelos seus dados. Se você pretende publicar repositórios, considere usar o e-mail privado `noreply` fornecido pelo GitHub para não expor o seu e-mail pessoal nos commits públicos.

Confira a configuração:

```bash
git config --global user.name
git config --global user.email
```

### Teste com um repositório próprio

Crie uma pasta nova para praticar, entre nela no terminal e execute:

```bash
git init
git status
```

Crie um arquivo `README.md` com qualquer descrição, salve e execute:

```bash
git add README.md
git commit -m "Primeiro registro do projeto"
git log --oneline
```

**Resultado esperado:** o terminal apresenta um commit no histórico.

> **Importante:** não execute `git init` dentro de `04_repositorio_demo_git` se a pasta `.git` do exemplo estiver presente. Esse projeto já contém um histórico preparado para estudo.

---

## 7. Criar uma conta no GitHub

**Página oficial:** https://github.com/signup

O **Git** funciona no seu computador. O **GitHub** é um serviço online usado para hospedar e compartilhar repositórios; são coisas diferentes.

### Criar a conta

1. Acesse o endereço oficial.
2. Cadastre-se com o método oferecido (e-mail, Google ou outro disponível).
3. Escolha um nome de usuário.
4. Verifique o endereço de e-mail, se solicitado.
5. Configure a autenticação em duas etapas quando possível.
6. Entre em https://github.com/ e confirme que sua conta está acessível.

### Criar seu primeiro repositório

1. Entre no GitHub.
2. Escolha **New repository** ou **Novo repositório**.
3. Dê um nome, por exemplo `meu-gerenciador-de-estudos`.
4. Escolha a visibilidade solicitada pela atividade. Para compartilhar com o público, selecione **Public**.
5. Crie o repositório.
6. A própria página mostrará instruções para vincular o repositório local ao GitHub. Siga os comandos apropriados ao estado do seu projeto, sem criar outro `git init` desnecessariamente.

> **Segurança:** nunca publique senhas, tokens, chaves privadas, dados reais de outras pessoas ou arquivos de configuração contendo segredos. Não compartilhe sua senha do GitHub com ninguém.

Para a demonstração do histórico Git na AcademyTeam, não é obrigatório entrar no GitHub: o histórico pode ser examinado localmente com `git log --oneline`.

---

## 8. Instalar PostgreSQL e pgAdmin 4

**PostgreSQL (oficial):** https://www.postgresql.org/download/  
**Instalador Windows indicado pelo PostgreSQL:** https://www.postgresql.org/download/windows/  
**pgAdmin (oficial):** https://www.pgadmin.org/download/

### Antes de instalar: qual a diferença?

- **PostgreSQL** é o **servidor de banco de dados**, responsável por armazenar e consultar informações.
- **pgAdmin 4** é a **interface gráfica** que permite acessar e administrar esse servidor.
- Instalar só o pgAdmin **não instala necessariamente o servidor PostgreSQL**.

**Para esta Formação, ambos são opcionais para os projetos Python.** Eles serão usados somente se você quiser executar as atividades SQL em um PostgreSQL real.

### Passo a passo — Windows

1. Abra https://www.postgresql.org/download/windows/.
2. Acesse o **instalador interativo indicado pela página** (distribuído pela EDB).
3. Baixe uma versão estável e compatível com seu Windows.
4. Execute o instalador e prossiga pelas telas.
5. Na seleção de componentes, mantenha marcados, se disponíveis:
   - **PostgreSQL Server**;
   - **pgAdmin 4**;
   - **Command Line Tools** (úteis, mas não essenciais para a primeira aula).
6. Escolha o diretório de instalação (o padrão geralmente é adequado).
7. Quando o instalador solicitar a **senha do superusuário `postgres`**, defina uma senha forte e **guarde-a em local seguro**. Você precisará dela para conectar ao banco.
8. Mantenha a porta **5432** se não houver conflito com outra instalação de PostgreSQL. Caso utilize outra porta, anote-a.
9. Escolha o locale padrão, salvo se houver uma orientação específica.
10. Conclua a instalação e aguarde a configuração do serviço.
11. Se for oferecido o **Stack Builder**, você pode ignorá-lo por enquanto: os projetos desta Formação não precisam de extensões adicionais do PostgreSQL.

**Observação:** o instalador do PostgreSQL para Windows normalmente **já oferece o pgAdmin 4 como componente**. Verifique isso antes de instalar o pgAdmin separadamente, para evitar duplicações.

### Se o pgAdmin não tiver sido instalado

1. Acesse https://www.pgadmin.org/download/.
2. Escolha a versão para Windows.
3. Baixe e execute o instalador oficial.
4. Abra o pgAdmin 4.

### Abrir o pgAdmin e conectar ao PostgreSQL

1. Abra **pgAdmin 4** pelo menu Iniciar.
2. Na primeira utilização, ele pode solicitar a criação de uma **senha mestra (master password)**. Essa senha protege os dados de conexão salvos no pgAdmin e **não substitui** a senha do usuário `postgres`.
3. No painel lateral, procure **Servers**.
4. Se existir um servidor PostgreSQL já cadastrado, expanda-o. Caso seja solicitada uma senha, use a senha definida para `postgres` durante a instalação.
5. Se nenhum servidor estiver cadastrado, clique com o botão direito em **Servers > Register > Server** (ou equivalente).
6. Na aba **General**, informe um nome, por exemplo `PostgreSQL local`.
7. Na aba **Connection**, preencha:

   | Campo | Valor para uma instalação local padrão |
   |---|---|
   | Host name/address | `localhost` |
   | Port | `5432` (ou a porta anotada) |
   | Maintenance database | `postgres` |
   | Username | `postgres` |
   | Password | Sua senha definida na instalação |

8. Clique em **Save** ou **Salvar**.
9. Se o servidor conectar, você verá seus bancos de dados na árvore lateral.

> Se a conexão falhar, confira a senha, a porta e se o serviço PostgreSQL está iniciado. **Não desative o firewall nem abra a porta para a internet** apenas para fazer um exercício local.

---

## 9. Criar o banco e executar o SQL do curso

### Etapa A — Criar um banco de estudos

1. No pgAdmin, expanda o servidor local.
2. Clique com o botão direito em **Databases > Create > Database**.
3. Em **Database**, informe `academyteam_formacao`.
4. Confirme o proprietário, normalmente `postgres` na instalação local usada neste guia.
5. Clique em **Save**.
6. Selecione o novo banco `academyteam_formacao`.
7. Abra o **Query Tool** (Ferramenta de Consulta).

### Etapa B — Criar a tabela de atividades

No **Query Tool**, execute o seguinte SQL:

```sql
CREATE TABLE atividades (
    id INTEGER PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descricao VARCHAR(500),
    concluida BOOLEAN NOT NULL DEFAULT FALSE,
    data_criacao TIMESTAMP NOT NULL
);
```

Use o botão **Execute** do Query Tool (geralmente representado por um ícone de reprodução).

**Resultado esperado:** a tabela `atividades` foi criada sem erros. Caso não apareça na árvore, atualize a seção **Tables**.

### Etapa C — Inserir uma atividade

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

**Resultado esperado:** uma linha foi inserida.

### Etapa D — Consultar os registros

```sql
SELECT * FROM atividades;
```

**Resultado esperado:** uma atividade chamada **Estudar Python** será exibida na tabela de resultados.

Para consultar somente as pendentes:

```sql
SELECT * FROM atividades
WHERE concluida = FALSE;
```

**Resultado esperado:** a atividade aparece porque ainda não foi concluída.

### Etapa E — Atualizar a conclusão

```sql
UPDATE atividades
SET concluida = TRUE
WHERE id = 1;
```

Agora execute novamente:

```sql
SELECT * FROM atividades;
```

**Resultado esperado:** a coluna `concluida` passa para `true`.

Se repetir a consulta de pendentes, ela não retornará essa atividade.

### E o arquivo `05_banco_de_dados/schema.sql`?

A pasta do curso já possui o **arquivo original `schema.sql`**, com `CREATE TABLE`, consultas, inserção e atualização. Você pode abri-lo pelo **Query Tool** ou copiar cada comando para a ferramenta.

**Atenção à ordem:** no arquivo original, as consultas `SELECT` aparecem **antes** do `INSERT`. Se você executar o arquivo inteiro de uma vez, essas consultas iniciais podem mostrar uma tabela vazia. Para enxergar a sequência didática com resultados, siga a ordem das etapas **B → C → D → E** deste manual.

Se executar `CREATE TABLE` novamente em um banco onde a tabela já existe, receberá um erro informando que a relação existe. **Não apague tabelas ou bancos que contenham informações importantes.** Para repetir o exercício, crie outro banco de testes ou peça orientação.

> **Limite do projeto:** os programas Python nas pastas `01`, `02` e `03` **não acessam essa tabela**. Eles usam memória ou o arquivo `dados.txt`. O PostgreSQL é uma demonstração complementar dos conceitos de banco de dados.

---

## 10. Baixar e abrir os projetos da AcademyTeam

### Opção 1 — Baixar pelo GitHub

1. Abra o link do repositório compartilhado pela AcademyTeam.
2. Clique em **Code > Download ZIP**.
3. Aguarde o download.
4. Clique com o botão direito no arquivo ZIP e escolha **Extrair Tudo** (Windows).
5. Extraia para uma pasta de fácil acesso, por exemplo `Documentos\AcademyTeam`.

**Importante:** um ZIP baixado pelo botão **Download ZIP** de um repositório GitHub **não traz o histórico Git `.git`** do repositório. Para estudar o histórico, clone um repositório preparado para isso ou utilize o pacote de demonstração disponibilizado pela equipe, quando incluir essa pasta oculta.

### Opção 2 — Clonar com Git

Se o Git já estiver instalado e a AcademyTeam fornecer o endereço do repositório:

```bash
git clone URL_DO_REPOSITORIO
```

**Substitua `URL_DO_REPOSITORIO` pelo endereço real.** Não copie literalmente esse texto como se fosse um link válido.

### Estrutura esperada dos materiais

```text
AcademyTeam_Formacao_Iniciante_Projetos/
├── README_GERAL.md
├── MANUAL_DE_INSTALACAO.md         # este manual, após adicioná-lo à raiz
├── 01_sem_persistencia/
│   ├── main.py
│   └── README.md
├── 02_com_persistencia/
│   ├── main.py
│   ├── dados.txt
│   └── README.md
├── 03_projeto_final/
│   ├── main.py
│   ├── dados.txt
│   └── README.md
├── 04_repositorio_demo_git/
│   ├── main.py
│   └── README.md
├── 05_banco_de_dados/
│   ├── schema.sql
│   ├── modelo_tabela.md
│   └── README.md
└── 06_exemplos/
```

*Representação resumida: o pacote pode conter arquivos adicionais, como testes e histórico Git.*

### Abrir a pasta no VS Code

1. Abra o VS Code.
2. Vá em **Arquivo > Abrir Pasta**.
3. Escolha `AcademyTeam_Formacao_Iniciante_Projetos`.
4. Confira se as pastas `01_sem_persistencia`, `02_com_persistencia` e `03_projeto_final` aparecem no Explorador.
5. Abra o `README.md` da atividade que está estudando.

---

## 11. Executar as versões do Gerenciador de Estudos

O programa é executado no terminal. **Não é necessário PostgreSQL nem pgAdmin para essas três versões.**

### Versão 01 — Sem persistência

1. No VS Code, abra a pasta `01_sem_persistencia` usando **Arquivo > Abrir Pasta**, ou abra um terminal dentro dessa pasta.
2. Digite:

   ```powershell
   py main.py
   ```

   Se necessário, use `python main.py`.

3. No menu, escolha `1` e cadastre `Estudar Algoritmos`.
4. Escolha `2` para listar a atividade.
5. Escolha `3` para concluí-la, informando o ID exibido.
6. Escolha `0` para sair.
7. Execute novamente `py main.py` e escolha `2`.

**O que observar:** os dados sumiram, porque essa versão guarda tudo **apenas na memória**.

### Versão 02 — Com persistência

1. Abra a pasta `02_com_persistencia` no VS Code.
2. Execute:

   ```powershell
   py main.py
   ```

3. Escolha `1`, informe um título e, se desejar, uma descrição.
4. Escolha `2` para conferir o cadastro.
5. Escolha `0` para encerrar.
6. Execute novamente o programa e escolha `2`.

**O que observar:** a atividade permanece salva em `dados.txt`.

### Versão 03 — Projeto Integrador

1. Abra a pasta `03_projeto_final`.
2. Execute:

   ```powershell
   py main.py
   ```

3. Utilize o menu:

   | Opção | Ação |
   |---|---|
   | `1` | Cadastrar atividade |
   | `2` | Listar todas |
   | `3` | Listar pendentes |
   | `4` | Marcar como concluída |
   | `5` | Remover atividade |
   | `0` | Sair |

4. Cadastre duas atividades.
5. Conclua uma delas e liste as pendentes.
6. Encerre e reabra o programa para verificar que os dados foram preservados.

**Cuidado:** as versões com persistência modificam o arquivo `dados.txt` ao cadastrar, concluir ou remover atividades. **Faça uma cópia da pasta** se quiser preservar os dados de exemplo originais.

### Se o terminal estiver na raiz do repositório

É possível executar um projeto sem abrir outra janela do VS Code. No terminal da raiz, entre na pasta desejada:

```powershell
cd 01_sem_persistencia
py main.py
```

Para voltar à pasta anterior, digite:

```powershell
cd ..
```

Troque o nome da pasta conforme a atividade. Em macOS/Linux, use `python3 main.py` se esse for o comando disponível.

---

## 12. Testar o histórico Git

O material da AcademyTeam inclui um exemplo de repositório na pasta `04_repositorio_demo_git`.

1. Abra essa pasta no VS Code.
2. Abra um terminal **dentro dela**.
3. Execute:

```bash
git status
git log --oneline
```

**O que observar:** o histórico apresenta as diferentes etapas registradas no Git.

**Se `git log` disser que não existem commits ou que a pasta não é um repositório:** confira se o diretório oculto `.git` veio junto com o material. Downloads em ZIP pelo GitHub não incluem o histórico `.git`; nesse caso, utilize o pacote de demonstração original fornecido pela equipe ou pratique criando seus próprios commits.

---

## 13. Instalação em macOS e Linux

As ferramentas também podem ser utilizadas nesses sistemas. Os nomes exatos dos instaladores e os comandos variam conforme a versão do sistema e a distribuição Linux.

### macOS

1. **Python:** consulte https://www.python.org/downloads/ e instale a versão estável indicada para macOS. Verifique no Terminal com `python3 --version`.
2. **VS Code:** consulte https://code.visualstudio.com/download, baixe o arquivo para macOS e mova o aplicativo para a pasta **Aplicativos**.
3. **Extensão Python:** abra o VS Code, procure **Python** da Microsoft em Extensões e selecione o interpretador instalado.
4. **Git:** consulte https://git-scm.com/install/mac. Em alguns sistemas, o Git já pode estar instalado; verifique com `git --version`.
5. **GitHub:** crie uma conta em https://github.com/signup.
6. **PostgreSQL:** escolha o instalador adequado em https://www.postgresql.org/download/macosx/.
7. **pgAdmin:** consulte https://www.pgadmin.org/download/ e escolha o pacote compatível com macOS. Se o instalador do PostgreSQL já incluir o pgAdmin, não é necessário instalá-lo novamente.

Para os projetos Python, utilize normalmente:

```bash
python3 main.py
```

### Linux

1. **Python:** muitas distribuições já incluem o Python 3. Confirme com `python3 --version`. Caso falte, consulte a documentação da distribuição para instalar o pacote Python 3.
2. **VS Code:** baixe o pacote adequado em https://code.visualstudio.com/download e siga as instruções oficiais da sua distribuição.
3. **Extensão Python:** instale a extensão **Python** da Microsoft pelo VS Code.
4. **Git:** confirme com `git --version`; caso necessário, instale pelo gerenciador de pacotes da distribuição, seguindo https://git-scm.com/install/linux.
5. **PostgreSQL:** escolha sua distribuição em https://www.postgresql.org/download/linux/ e siga as instruções oficiais.
6. **pgAdmin:** consulte https://www.pgadmin.org/download/ para os pacotes e repositórios disponíveis.

Para os projetos Python, utilize normalmente:

```bash
python3 main.py
```

> No macOS e Linux, o PostgreSQL pode exigir uma etapa adicional de inicialização do serviço e configuração de um usuário do banco. Siga as instruções do pacote utilizado. Os parâmetros `localhost`, porta `5432` e usuário `postgres` só se aplicam se sua instalação tiver sido configurada dessa maneira.

---

## 14. Problemas comuns e soluções

### `py` ou `python` não é reconhecido

- Confirme que o Python foi instalado.
- Feche e reabra o terminal ou o VS Code.
- No Windows, teste ambos: `py --version` e `python --version`.
- Verifique as instruções atuais de instalação/PATH na documentação oficial do Python.
- Se o comando `python` abrir a Microsoft Store, confira os aliases de execução de aplicativos do Windows e a instalação do Python.

### `No such file or directory: main.py` ou `can't open file`

Você provavelmente está **na pasta errada**. Abra no VS Code a pasta que contém `main.py` e tente novamente. Use `dir` no Windows ou `ls` no macOS/Linux para conferir os arquivos da pasta atual.

### O VS Code não identifica o Python

Instale a extensão **Python** da Microsoft e escolha **Python: Select Interpreter** pela paleta de comandos (`Ctrl + Shift + P`). O Python deve estar instalado no computador, não somente a extensão.

### `git` não é reconhecido

Verifique a instalação do Git, feche e reabra o terminal e teste `git --version`.

### `fatal: not a git repository`

O terminal não está dentro de um repositório Git, ou a pasta `.git` está ausente. Entre na pasta correta ou inicialize **um novo projeto seu** com `git init`.

### Não consigo conectar o pgAdmin ao PostgreSQL

- Confirme se o **servidor PostgreSQL** foi instalado e está em execução.
- Confira o host `localhost` e a porta configurada durante a instalação.
- Use a senha do **usuário `postgres`**, não a senha mestra do pgAdmin.
- Se já existir outra instalação, a porta pode ser diferente de `5432`.
- Não exponha o servidor à internet para solucionar o problema de uma prática local.

### `relation "atividades" already exists`

A tabela já foi criada. Não execute novamente o `CREATE TABLE` no mesmo banco. Use a tabela existente ou crie um **novo banco de testes**.

### `duplicate key value violates unique constraint`

Você está tentando cadastrar outro registro com um `id` já utilizado. Para um novo registro de exemplo, utilize outro `id` disponível. **Não apague dados reais** para contornar o erro.

### O projeto Python não mostra os dados da tabela SQL

Isso é esperado! Os programas Python deste repositório **não possuem integração com PostgreSQL**. As versões persistentes guardam as atividades em `dados.txt`, enquanto `schema.sql` é um exercício separado.

### O arquivo `dados.txt` mudou depois de testar

Isso também é esperado nas versões com persistência. Se quiser preservar o exemplo original, restaure uma cópia da pasta antes de gravar ou repetir os exercícios.

---

## 15. Checklist de ambiente pronto

Marque as ferramentas conforme avançar na Formação:

- [ ] Python 3 instalado e funcionando (`py --version`, `python --version` ou `python3 --version`).
- [ ] VS Code instalado.
- [ ] Extensão **Python**, da Microsoft, instalada no VS Code.
- [ ] Arquivo `ola.py` executado com sucesso.
- [ ] Pastas dos projetos da AcademyTeam baixadas e abertas no VS Code.
- [ ] Gerenciador sem persistência executado.
- [ ] Gerenciador com persistência executado e testado após reiniciar.
- [ ] Git instalado e funcionando (`git --version`).
- [ ] Nome e e-mail do Git configurados.
- [ ] Conta no GitHub criada, se for realizar publicação de repositórios.
- [ ] PostgreSQL instalado, **caso queira fazer a prática SQL em servidor real**.
- [ ] pgAdmin conectado ao PostgreSQL, **caso tenha instalado o banco**.
- [ ] Banco `academyteam_formacao` criado e atividade SQL executada, **caso vá realizar a demonstração prática**.

**Concluiu as etapas correspondentes ao seu módulo?** Então seu ambiente está preparado para acompanhar as atividades da Formação Iniciante!

---

## 16. Sites e documentação oficiais

- **Python — download:** https://www.python.org/downloads/
- **Python — instalação no Windows:** https://docs.python.org/pt-br/3/using/windows.html
- **Visual Studio Code — download:** https://code.visualstudio.com/download
- **VS Code — Python:** https://code.visualstudio.com/docs/languages/python
- **Git — download:** https://git-scm.com/install/
- **GitHub — cadastro:** https://github.com/signup
- **PostgreSQL — download:** https://www.postgresql.org/download/
- **PostgreSQL — Windows:** https://www.postgresql.org/download/windows/
- **pgAdmin 4 — download:** https://www.pgadmin.org/download/
- **pgAdmin 4 — documentação:** https://www.pgadmin.org/docs/pgadmin4/latest/

> **AcademyTeam — Educação tecnológica para todos.** Este material foi preparado para o contexto didático da Formação Iniciante. As interfaces e versões dos instaladores podem mudar; se uma etapa estiver diferente, consulte a documentação oficial correspondente.
