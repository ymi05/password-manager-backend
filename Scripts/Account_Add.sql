CREATE OR ALTER  PROCEDURE [dbo].[Account_Add]
(
	@Profile_id INT,
	@URL VARCHAR(40) = NULL,
	@Website_app_name VARCHAR(20),
	@Username VARCHAR(40),
	@Password VARCHAR(100)
)
AS
SET NOCOUNT ON;
SET dateformat dmy
IF NOT EXISTS ( SELECT * FROM Profile WHERE @Profile_id = id)
	BEGIN
		SELECT 'Cannot create an account for a profile that does not exist' [message] FOR JSON PATH 
	END

IF NOT EXISTS (SELECT * FROM Account WHERE @Username = username AND @Website_app_name = website_app_name)
	BEGIN	
		INSERT INTO Account 
		(
			profile_id,
			[URL],
			website_app_name,
			username,
			password,
			creation_date
		)
		VALUES 
		(
			@Profile_id,
			@URL,
			@Website_app_name,
			@Username,
			@Password,
			GETDATE()
		);
		SELECT 'Account has been added' [message] FOR JSON PATH;
	END
ELSE
	SELECT 'Account already exist for that app' [message] FOR JSON PATH