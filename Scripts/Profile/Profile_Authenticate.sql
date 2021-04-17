CREATE OR ALTER PROCEDURE [dbo].[Profile_Authenticate]
(
	@Profile_id INT
	,@Authentication_Code VARCHAR(6)
)
AS
SET NOCOUNT ON;
IF EXISTS (SELECT * FROM Authentication_Code WHERE @Profile_id = profile_id AND @Authentication_Code=code_value)
	BEGIN
		DELETE FROM [dbo].[Authentication_Code] WHERE @Profile_id = profile_id AND @Authentication_Code=code_value
		SELECT 'You have been authenticated' [message] FOR JSON PATH;
	END
ELSE
	SELECT 'Invalid authenticated code' [message] FOR JSON PATH;
GO
EXEC Profile_Authenticate 13 , 'C67616'