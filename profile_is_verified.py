from query_handler import exec_query_with_message
import json

def profile_is_verified(profile_id):
    response = exec_query_with_message("EXEC profile_is_verified @Profile_id = '"+profile_id+"';")
    response = json.loads(response)[0]
    if response["verified"] == 1:
        return True
    return False

