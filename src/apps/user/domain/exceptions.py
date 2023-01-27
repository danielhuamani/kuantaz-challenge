from typing import Optional


class UserNotFoundException(Exception):
    code: str = "USER_NOT_FOUND"
    message: str = "user not found"
    user_id: Optional[int] = None

    def __init__(self, message: Optional[str] = None, user_id: Optional[int] = None):
        if message:
            self.message = message
        self.user_id = user_id
        super().__init__(self.message)
