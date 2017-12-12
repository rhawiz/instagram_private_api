from instagram_private_api import Client

if __name__ == '__main__':
    username = ""
    password = ""

    api = Client(username, password)
    if api.checkpoint_required:
        print("Checkpoint triggered, check your email")
        api.trigger_checkpoint()

    security_code = None
    while not security_code:
        security_code = input('Security code (6-digit code emailed to you): ')

    success = api.respond_to_checkpoint(security_code)
    if success:
        print(api.user_following(api.authenticated_user_id))
    else:
        print("Couldn't respond to checkpoint")