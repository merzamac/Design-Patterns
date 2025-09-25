from structural.Composite.component import FileSystemComponent


class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def details(self):
        return f"File: {self.name}"
