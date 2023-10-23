INSERT INTO smartattendance_usuario (usuario_nome, usuario_tipo, id_externo) values ("Murta", "P", "123");
INSERT INTO smartattendance_turma (professor_id_id, turma_nome, semestre) values (1, "Engenharia de Software 2", "2023/2");
INSERT INTO smartattendance_aluno_turma (aluno_id_id, turma_id_id) values (1, 1);
INSERT INTO smartattendance_turma_horario (turma_id_id, dia_semana, hora_inicio, hora_fim) values (1, "Seg", "23:30","23:50");
INSERT INTO smartattendance_turma_horario (turma_id_id, dia_semana, hora_inicio, hora_fim) values (1, "Segunda", "20:30", "21:30");