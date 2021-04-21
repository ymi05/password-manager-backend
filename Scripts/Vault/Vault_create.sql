CREATE OR ALTER  PROCEDURE [dbo].[Vault_create]
(
	@Profile_id INT,
    @Encrypted_Vault VARCHAR(MAX)
	
)
AS
SET NOCOUNT ON;
IF  EXISTS (SELECT * FROM Profile WHERE id = @Profile_id)
	BEGIN	
        INSERT INTO Vault 
            (profile_id , encrypted_vault) 
            VALUES 
            (@Profile_id , @Encrypted_Vault)
        SELECT 'Vault created' [message] FOR JSON PATH;
    END
GO

-- DELETE FROM Vault
-- EXEC Vault_load 26 