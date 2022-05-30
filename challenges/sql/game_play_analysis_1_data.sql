USE labs;

CREATE TABLE activity (
    player_id       int not null,   
    device_id       int not null,
    event_date      date not null,
    games_played    int not null,
    PRIMARY KEY (player_id, event_date)
)

INSERT INTO activity VALUES (1, 2, '2016-03-01', 5);
INSERT INTO activity VALUES (1, 2, '2016-05-02', 6);
INSERT INTO activity VALUES (2, 3, '2017-06-25', 1);
INSERT INTO activity VALUES (3, 1, '2016-03-02', 0);
INSERT INTO activity VALUES (3, 4, '2018-07-03', 5);
