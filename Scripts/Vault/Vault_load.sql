CREATE OR ALTER  PROCEDURE [dbo].[Vault_load]
(
	@Profile_id INT,
	@Encrypted_Vault VARCHAR(MAX) = ''
	
)
AS
SET NOCOUNT ON;
IF @Encrypted_Vault = ''
	BEGIN 
		SELECT 'Vault retrived' [message] , (SELECT encrypted_vault FROM VAULT WHERE @Profile_id = profile_id) AS encrypted_vault FOR JSON PATH;
	END
	ELSE

		UPDATE Vault SET encrypted_vault = @Encrypted_Vault WHERE @Profile_id = profile_id;

GO



-- DELETE FROM Vault
