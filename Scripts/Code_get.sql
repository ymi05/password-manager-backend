CREATE OR ALTER   PROCEDURE [dbo].[Code_get]
(
	@Profile_id INT
)
AS
SET NOCOUNT ON;
IF EXISTS (SELECT * FROM Verification_Code WHERE @Profile_id = profile_id)
	BEGIN
		SELECT 'Verificaiton Code found' [message] , (SELECT code_value FROM Verification_Code WHERE @Profile_id = profile_id) [verification code]  FOR JSON PATH;
	END
ELSE
	SELECT 'Cannot obtain the verification code' [message] FOR JSON PATH;
	
GO