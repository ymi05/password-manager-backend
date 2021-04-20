CREATE OR ALTER PROCEDURE [dbo].[Profile_Delete](
    @Profile_id INT
)
AS 
SET NOCOUNT ON;
IF EXISTS (SELECT * FROM Profile WHERE id = @Profile_id)
    BEGIN 
        DELETE FROM Vault WHERE profile_id = @Profile_id;
        DELETE FROM Verfied_Profile WHERE profile_id = @Profile_id;
        DELETE FROM Profile WHERE id = @Profile_id;
        SELECT 'Profile has been successfully deleted' [message] FOR JSON PATH;
    END
ELSE    
    SELECT 'Profile does not exist' [message] FOR JSON PATH;
GO



EXEC Profile_Delete 17

SELECT * FROM Profile

