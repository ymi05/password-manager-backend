CREATE OR ALTER PROCEDURE [dbo].[Auth_Code_get]
(
	@Profile_id INT
)
AS
SET NOCOUNT ON;
IF EXISTS (SELECT * FROM Authentication_Code WHERE @Profile_id = profile_id)
	BEGIN
		DECLARE @code_value VARCHAR(6);
		DECLARE @email VARCHAR(40);
		DECLARE @full_name VARCHAR(30);

		SELECT @code_value = code_value FROM Authentication_Code WHERE @Profile_id = profile_id
		SELECT @email =  email FROM Profile WHERE @Profile_id = id
		SELECT @full_name =  full_name FROM Profile WHERE @Profile_id = id

		SELECT 'Authentcation Code found' [message] 
		, @code_value [authentication_code] 
		, @email [email]  
		, @full_name  [name] FOR JSON PATH;
	END
ELSE
	SELECT 'Cannot obtain the auth code code' [message] FOR JSON PATH;
	
GO


EXEC Verification_Code_get 11