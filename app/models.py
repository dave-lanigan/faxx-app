
class HTMLTag:
    def __init__(self,
            tag,
            id: str = "",
            classes: list = "",
            content: str = "",
        ):
        self.tag = tag
        self.id = id
        self.classes = classes
        self.content = content
    
    def dumps(self):
        return f'<{self.tag} id="{self.id}" class="{" ".join(self.classes)}">{self.content}</{self.tag}>'
