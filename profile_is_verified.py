from query_handler import exec_query_with_message
import json


# TODO Intergrate this function into the other ones, except for signing up.
def profile_is_verified(profile_id: int) -> bool:
    """[summary]
        Checks if the user has been verified 
    Args:
        profile_id (int): profile id of the user logging in

    Returns:
        boolean: tells us whether the user has been verified or not
    """    
    response = exec_query_with_message("EXEC profile_is_verified @Profile_id = '"+str(profile_id)+"';")
    response = json.loads(response)[0]
    if response["verified"] == 1:
        return True
    return False

