CREATE OR ALTER PROCEDURE [dbo].[profile_is_auth](
	@Profile_id INT
)
AS
IF EXISTS (SELECT * FROM [dbo].[Authenticated_Profile])
	BEGIN
		SELECT 1 [verified] FOR JSON PATH;
	END
ELSE 
	SELECT 0 [verified] FOR JSON PATH;

GO

EXEC profile_is_auth 1