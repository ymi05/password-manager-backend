CREATE OR ALTER PROCEDURE [dbo].[Profile_Auth]
(
	@Profile_id INT
	,@Auth_Code VARCHAR(6)
)
AS
SET NOCOUNT ON;
IF EXISTS (SELECT * FROM Authentication_Code WHERE @Profile_id = profile_id AND @Auth_Code=code_value) 
	BEGIN
		INSERT INTO Verified_Profile (profile_id) VALUES (@Profile_id)
		DELETE FROM [dbo].[Authentication_Code] WHERE @Profile_id = profile_id AND @Auth_Code=code_value
		SELECT 'You have been authenticated' [message] FOR JSON PATH;
	END
ELSE
	SELECT 'Invalid authenticaiton code' [message] FOR JSON PATH;
GO
EXEC Profile_Auth 1 , '43fF3'