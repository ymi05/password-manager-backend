CREATE OR ALTER PROCEDURE [dbo].[Verification_Code_generate](
	@Profile_id INT,
	@Code VARCHAR(6)
)
AS
	IF NOT EXISTS (SELECT * FROM [dbo].[Verification_Code] WHERE @Profile_id = profile_id AND @Code = code_value)
		BEGIN
			INSERT INTO [dbo].[Verification_Code] (profile_id , code_value) VALUES ( @Profile_id , @Code);
		END
GO

