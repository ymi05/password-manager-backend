CREATE OR ALTER PROCEDURE [dbo].[validate_profile](
    @Email VARCHAR(40),
	@Password VARCHAR(100)
)
AS
IF EXISTS (SELECT * FROM Profile WHERE @Email = email AND @Password = password)
    BEGIN 
        DECLARE @code VARCHAR(6);
		DECLARE @id INT;
		SELECT @id = id FROM Profile WHERE @Email = email;
		SELECT @code = SUBSTRING(CONVERT(varchar(255), NEWID()), 0, 7)
		EXEC Auth_Code_generate @id , @code

        SELECT @id  [profile_id] , 1 [valid] FOR JSON PATH
    END
ELSE   
    SELECT 0 [valid] FOR JSON PATH

GO
EXEC validate_profile 'dogafop603@whipjoy.com' , 'gregdfg'