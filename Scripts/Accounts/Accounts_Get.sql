CREATE OR ALTER  PROCEDURE [dbo].[Accounts_Get]
(
	@Profile_id INT
)
AS
SET NOCOUNT ON;
IF EXISTS (SELECT * FROM Profile WHERE @Profile_id = id)
	BEGIN
		SELECT id  AS account_id , website_app_name , username , password FROM [dbo].[Account] WHERE @Profile_id = profile_id
	END
ELSE
	SELECT 0 [profile_exists]
GO
EXEC [dbo].[Accounts_Get] 2