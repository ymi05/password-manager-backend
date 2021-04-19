CREATE OR ALTER   PROCEDURE [dbo].[Profile_Add]
(	     
	@Full_Name VARCHAR(30),
	@Email VARCHAR(40),
	@Password VARCHAR(MAX)
)
AS
	SET NOCOUNT ON;
	Set dateformat dmy

	IF NOT EXISTS ( SELECT * FROM Profile 
		WHERE @Email = email
	)
    BEGIN
         INSERT INTO Profile
         ( 
			full_name
			,email
		 	,[password]
		 	,creation_date
                     
         )
         VALUES
         (
		  	@Full_Name    
			,@Email
			,@Password
			,Getdate()
         )
		DECLARE @code VARCHAR(6);
		DECLARE @id INT;
		SELECT @id = SCOPE_IDENTITY();
		SELECT @code = SUBSTRING(CONVERT(varchar(255), NEWID()), 0, 7)
		EXEC Verification_Code_generate @id , @code

        SELECT 'Profile added, please verify your email.' [message] , (SELECT SCOPE_IDENTITY()) [profile_id] FOR JSON PATH
        END
        ELSE
        SELECT 'Email is already in use.'  [message] FOR JSON PATH