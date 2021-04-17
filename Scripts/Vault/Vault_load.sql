CREATE OR ALTER  PROCEDURE [dbo].[Vault_load]
(
	@Profile_id INT,
	@Encrypted_Vault VARCHAR(MAX) = ''
	
)
AS
SET NOCOUNT ON;
IF  EXISTS (SELECT * FROM Vault WHERE @Profile_id = profile_id)
	BEGIN	
		IF @Encrypted_Vault = ''
			SELECT 'Vault retrived' [message] , (SELECT encrypted_vault FROM VAULT WHERE @Profile_id = profile_id) AS encrypted_vault FOR JSON PATH;
		ELSE
			BEGIN
				UPDATE Vault SET encrypted_vault = @Encrypted_Vault WHERE @Profile_id = profile_id;
				SELECT 'Vault has been updated' [message] , (SELECT encrypted_vault FROM VAULT WHERE @Profile_id = profile_id) AS encrypted_vault FOR JSON PATH;
				END
		
	END
ELSE
	INSERT INTO Vault 
		(
			profile_id,
			encrypted_vault
		)
		VALUES 
		(
			@Profile_id,
			@Encrypted_Vault
		);
		SELECT 'Vault has been created' [message]  , (SELECT SCOPE_IDENTITY()) [vault_id] , (SELECT encrypted_vault FROM VAULT WHERE @Profile_id = profile_id) AS encrypted_vault FOR JSON PATH;
GO

DELETE FROM Vault
EXEC Vault_load 26 