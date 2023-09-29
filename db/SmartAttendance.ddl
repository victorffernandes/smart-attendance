CREATE TABLE Usuario (
    usuario_id int NOT NULL,
    usuario_nome varchar(50) NOT NULL,
    usuario_type boolean NOT NULL,
    PRIMARY KEY (usuario_id)
);

CREATE TABLE Turma (
    turma_id int NOT NULL,
    professor_id int NOT NULL,
    turma_nome varchar(50) NOT NULL,
    semestre varchar(6) NOT NULL,
    PRIMARY KEY (turma_id),
    FOREIGN KEY (professor_id) REFERENCES Usuario(usuario_id)
); 

CREATE TABLE Aluno_Turma (
    turma_id int NOT NULL,
    usuario_id int NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario_id),
    FOREIGN KEY (turma_id) REFERENCES Turma(turma_id)
); 

CREATE TABLE Chamada (
    chamada_id int NOT NULL,
    turma_id int NOT NULL,
    data date NOT NULL,
    coordenadas spatial NOT NULL,
    PRIMARY KEY (chamada_id),
    FOREIGN KEY (turma_id) REFERENCES Turma(turma_id)
); 

CREATE TABLE Presenca (
    chamada_id int NOT NULL,
    usuario_id int NOT NULL,
    tempo_entrada time,
    tempo_saida time,
    FOREIGN KEY (chamada_id) REFERENCES Chamada(chamada_id),
    FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario_id)
); 