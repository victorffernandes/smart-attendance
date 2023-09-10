CREATE TABLE Professor (
    professor_id int NOT NULL,
    professor_nome varchar(50) NOT NULL,
    PRIMARY KEY (professor_id)
);

CREATE TABLE Turma (
    turma_id int NOT NULL,
    professor_id int NOT NULL,
    turma_nome varchar(50) NOT NULL,
    semestre varchar(6) NOT NULL,
    PRIMARY KEY (turma_id),
    FOREIGN KEY (professor_id) REFERENCES Professor(professor_id)
); 

CREATE TABLE Aluno (
    aluno_id int NOT NULL,
    Aluno_name varchar(50) NOT NULL,
    PRIMARY KEY (aluno_id)
);

CREATE TABLE Aluno_Turma (
    turma_id int NOT NULL,
    aluno_id int NOT NULL,
    FOREIGN KEY (professor_id) REFERENCES Professor(professor_id),
    FOREIGN KEY (aluno_id) REFERENCES Aluno(aluno_id)
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
    aluno_id int NOT NULL,
    tempo_entrada time,
    tempo_saida time,
    FOREIGN KEY (chamada_id) REFERENCES Chamada(chamada_id),
    FOREIGN KEY (aluno_id) REFERENCES Aluno(aluno_id)
); 