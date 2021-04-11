
CREATE TABLE Profile(
	id [INT] IDENTITY(1, 1) NOT NULL, 
	full_name VARCHAR(30) NOT NULL,
	email VARCHAR(40) NOT NULL UNIQUE,
	phone_no VARCHAR(20) NOT NULL UNIQUE,
	[password] VARCHAR(100) NOT NULL,
	creation_date DATETIME NOT NULL,
	verified BIT,
	CONSTRAINT PK_Profile PRIMARY KEY(id)
);

CREATE TABLE Account(
	id [INT] IDENTITY(1, 1) NOT NULL, 
	[URL] VARCHAR(40) NULL,
	website_app_name VARCHAR(20) NOT NULL,
	username VARCHAR(40) NOT NULL,
	password VARCHAR(100),
	creation_date DATETIME NOT NULL,
	[profile_id] INT NOT NULL FOREIGN KEY REFERENCES Profile(id) ON DELETE CASCADE
	CONSTRAINT PK_Account  PRIMARY KEY(id)

);
CREATE INDEX profile_accounts
ON Account ([profile_id]);


CREATE TABLE Verification_Code(
	id [INT] IDENTITY(1, 1) NOT NULL,
	code_value VARCHAR(6) UNIQUE,
	[profile_id] INT NOT NULL FOREIGN KEY REFERENCES Profile(id) ON DELETE CASCADE
	CONSTRAINT PK_Code  PRIMARY KEY(id)
);
CREATE UNIQUE INDEX code_id
on Verification_Code (id);

CREATE TABLE Verfied_Profile(
	id [INT] IDENTITY(1, 1) NOT NULL PRIMARY KEY,
	[profile_id] INT NOT NULL FOREIGN KEY REFERENCES Profile(id) ON DELETE CASCADE

)
