CREATE OR ALTER PROCEDURE [dbo].[Auth_Code_generate](
	@Profile_id INT,
	@Code VARCHAR(6)
)
AS
SET NOCOUNT ON;
	IF NOT EXISTS (SELECT * FROM [dbo].[Authentication_Code] WHERE @Profile_id = profile_id OR @Code = code_value)
		BEGIN
			INSERT INTO [dbo].[Authentication_Code] (profile_id , code_value) VALUES ( @Profile_id , @Code);
		END
GO

