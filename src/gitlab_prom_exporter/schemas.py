"""
Definitions of webhook request schemas.
"""

from typing import Literal

from pydantic import BaseModel


class User(BaseModel):
    username: str


class Project(BaseModel):
    path_with_namespace: str


class JobEvent(BaseModel):
    object_kind: Literal["build"]
    ref: str
    build_name: str
    build_status: str
    user: User
    project: Project