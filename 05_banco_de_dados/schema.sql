-- Modelo conceitual simples para o Gerenciador de Estudos.
-- Exemplo didático para a Formação Iniciante.

CREATE TABLE atividades (
    id INTEGER PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descricao VARCHAR(500),
    concluida BOOLEAN NOT NULL DEFAULT FALSE,
    data_criacao TIMESTAMP NOT NULL
);

-- Exibir todas as atividades
SELECT * FROM atividades;

-- Exibir somente atividades pendentes
SELECT * FROM atividades
WHERE concluida = FALSE;

-- Exemplo de inserção
INSERT INTO atividades (id, titulo, descricao, concluida, data_criacao)
VALUES (
    1,
    'Estudar Python',
    'Revisar estruturas de repetição',
    FALSE,
    CURRENT_TIMESTAMP
);

-- Exemplo de atualização
UPDATE atividades
SET concluida = TRUE
WHERE id = 1;
