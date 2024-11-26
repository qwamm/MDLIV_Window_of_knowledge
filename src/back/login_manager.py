from fastapi_login import LoginManager
from ..enviroments import SECRET_KEY

login_manager = LoginManager(SECRET_KEY, "/api/auth/login")

@login_manager.user_loader()
def load_user(UserStr: str):
    # loading user from db logic
    pass
