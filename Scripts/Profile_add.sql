CREATE OR ALTER   PROCEDURE [dbo].[Profile_Add]
(	     
	@Full_Name VARCHAR(30),
	@Email VARCHAR(40),
	@Phone_No VARCHAR(20),
	@Password VARCHAR(100)
)
AS
	SET NOCOUNT ON;
	Set dateformat dmy

	IF NOT EXISTS ( SELECT * FROM Profile 
		WHERE phone_no=@Phone_NO AND @Email = email
	)
    BEGIN
         INSERT INTO Profile
         ( 
			full_name 
        	,phone_no
			,email
		 	,[password]
		 	,creation_date
                     
         )
         VALUES
         (
		  	@Full_Name    
			,@Phone_NO
			,@Email
			,@Password
			,Getdate()
         )
		DECLARE @code VARCHAR(6);
		DECLARE @id INT;
		SELECT @id = SCOPE_IDENTITY();
		SELECT @code = SUBSTRING(CONVERT(varchar(255), NEWID()), 0, 7)
		EXEC Code_generate @id , @code

        SELECT 'Profile added, please verify your phone number.' [message] , (SELECT SCOPE_IDENTITY()) [profile_id] FOR JSON PATH
        END
        ELSE
        SELECT 'Email or Phone number are already in use.'  [message] FOR JSON PATH