# Roteiro de Testes

## 1. Versão sem persistência

1. Abra `01_sem_persistencia`.
2. Execute `python main.py`.
3. Cadastre:
   - Estudar Python
   - Revisar Git
4. Liste as atividades.
5. Saia com `0`.
6. Abra novamente.
7. A lista estará vazia.

**Uso ideal:** Vídeo de Conexão 04 — mostrar o problema da informação temporária.

---

## 2. Versão com persistência

1. Abra `02_com_persistencia`.
2. Execute `python main.py`.
3. Observe que já existem atividades carregadas.
4. Cadastre uma nova.
5. Feche com `0`.
6. Abra novamente.
7. A nova atividade continuará disponível.

**Uso ideal:** Vídeos 04 e 05.

---

## 3. Projeto final

1. Abra `03_projeto_final`.
2. Execute `python main.py`.
3. Teste:
   - cadastro;
   - listagem;
   - listagem de pendentes;
   - conclusão;
   - remoção;
   - persistência.
4. Feche e abra novamente.

**Uso ideal:** demonstração do Projeto Integrador e encerramento da Formação.

---

## 4. Banco de dados

Abra `05_banco_de_dados/schema.sql`.

Ele contém:
- criação da tabela `atividades`;
- `SELECT`;
- filtro de pendentes;
- `INSERT`;
- `UPDATE`.

Não é necessária integração com Python para a Formação.

---

## 5. Repositório Git demonstrativo

A pasta `04_repositorio_demo_git` possui histórico Git local.

Dentro dela:

```bash
git log --oneline
```

Use esse histórico para capturas e demonstrações do Vídeo 03.
