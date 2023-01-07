import uuid
from dataclasses import dataclass, field


@dataclass
class User:
    username: str
    _chat_id: str = field(default=uuid.uuid4(), init=False)
    message: str
    @property
    def get_chat_id(self):
        return self._chat_id
    def create_message(self):
        return f'{self.username}: {self.message}'
    def new_message(self, new_msg):
        self.message = new_msg

if __name__ == "__main__":
    def_user = User('Bobby123', 'Hello')
    print(f"{def_user.username}: {def_user.message} {def_user.get_chat_id}")
