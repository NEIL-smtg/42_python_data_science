import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """generating random str"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """defining attr, field is to set default value
    in the right way to avoid using mutable default arguments"""
    name: str
    surname: str
    active: bool = field(default=True, init=False)
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """post init, init that will wait"""
        self.login = self.name[0] + self.surname
