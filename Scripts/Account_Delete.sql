CREATE OR ALTER  PROCEDURE [dbo].[Account_Delete]
(
	@Profile_id INT,
	@Account_id INT
)
AS
SET NOCOUNT ON;
IF NOT EXISTS (SELECT * FROM Profile WHERE @Profile_id = id)
	BEGIN
		SELECT 'Profile does not exist' [message] FOR JSON PATH;
	END

IF EXISTS (SELECT * FROM Account WHERE @Profile_id = profile_id AND @Account_id = id)
	BEGIN
		DELETE FROM Account WHERE @Profile_id = profile_id AND @Account_id = id;
		SELECT 'Account has been deleted' [message] FOR JSON PATH;
	END
ELSE
	SELECT 'Account does not exist' [message] FOR JSON PATH;
GO
EXEC [dbo].[Account_Delete] 9 , 7;