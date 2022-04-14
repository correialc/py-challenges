USE labs;

CREATE TABLE node (
    id  int not null,
    pid int null
);

INSERT INTO node VALUES (1, null);
INSERT INTO node VALUES (2, 1);
INSERT INTO node VALUES (3, 1);
INSERT INTO node VALUES (4, 2);
INSERT INTO node VALUES (5, 2);

