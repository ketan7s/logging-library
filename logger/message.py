import uuid
import socket

class Message:
    def __init__(self, content: str, level: str, namespace: str, tracking_id: str=None):
        self.content = content
        self.level = level
        self.namespace = namespace
        self.tracking_id = tracking_id or str(uuid.uuid4())
        self.hostname = socket.gethostname()

    def __repr__(self):
        return (f"Message(level={self.level}, namespace={self.namespace}, content={self.content}, "
                f"tracking_id={self.tracking_id}, hostname={self.hostname})")
