CREATE TABLE Female (
	Id INT NOT NULL,
	"Divorce Date" DATE NOT NULL,
	"Divorce Type" VARCHAR NOT NULL,
	"DOB Female" DATE NOT NULL,
	"Age Female" DECIMAL NOT NULL,
	"Income Female" DECIMAL NOT NULL,
	"Marriage Date" DATE NOT NULL,
	"Education Female" VARCHAR NOT NULL,
	"Marriage Year" DECIMAL NOT NULL,
	"Number Children" DECIMAL NOT NULL,
	"Zodiac_Sign" VARCHAR NOT NULL,
	"Income Category" VARCHAR NOT NULL,
	"Divorce Month" INT NOT NULL,
	FOREIGN KEY (Id) REFERENCES Male (Id),
	PRIMARY KEY (Id)
);

SELECT * FROM Female;

CREATE TABLE Male (
	Id INT NOT NULL,
	"Divorce Date" DATE NOT NULL,
	"Divorce Type" VARCHAR NOT NULL,
	"DOB Male" DATE NOT NULL,
	"Age Male" DECIMAL NOT NULL,
	"Income Male" DECIMAL NOT NULL,
	"Marriage Date" DATE NOT NULL,
	"Education Male" VARCHAR NOT NULL,
	"Marriage Year" DECIMAL NOT NULL,
	"Number Children" DECIMAL NOT NULL,
	"Zodiac_Sign" VARCHAR NOT NULL,
	"Income Category" VARCHAR NOT NULL,
	"Divorce Month" INT NOT NULL,
	FOREIGN KEY (Id) REFERENCES Female (Id),
	PRIMARY KEY (Id)
);

SELECT * FROM Male;
