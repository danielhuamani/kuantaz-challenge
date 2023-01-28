from typing import Optional


class ProjectNotFoundException(Exception):
    code: str = "PROJECT_NOT_FOUND"
    message: str = "project not found"
    project_id: Optional[int] = None

    def __init__(self, message: Optional[str] = None, project_id: Optional[int] = None):
        if message:
            self.message = message
        self.project_id = project_id
        super().__init__(self.message)
