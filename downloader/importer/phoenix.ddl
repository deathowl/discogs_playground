CREATE TABLE COUNTRY  ( C_COUNTRYKEY  INTEGER NOT NULL primary key,
                            C_NAME       CHAR(25),
                            C_REGIONKEY  INTEGER,
                            C_COMMENT    VARCHAR(152));

CREATE TABLE GENRE  ( G_GENREKEY  INTEGER NOT NULL primary key,
                            G_NAME       CHAR(25),
                            G_REGIONKEY  INTEGER,
                            G_COMMENT    VARCHAR(152));

CREATE TABLE STYLE  ( S_STYLEKEY  INTEGER NOT NULL primary key,
                            S_NAME       CHAR(25),
                            S_REGIONKEY  INTEGER,
                            S_COMMENT    VARCHAR(152));

CREATE TABLE ARTIST  ( A_ARTISTKEY  INTEGER NOT NULL primary key,
                            A_NAME       CHAR(25),
                            A_REGIONKEY  INTEGER,
                            A_COMMENT    VARCHAR(152));



CREATE TABLE RELEASES ( R_KEY     VARCHAR(40) NOT NULL primary key,
                             R_ARTIST        CHAR(25),
                             R_GENREKEY     INTEGER,
                             R_STYLEKEY    INTEGER,
                             R_COUNTRYKEY   INTEGER,
                             R_RELEASED    char(10),
                             R_NOTES       varchar(200);
