from structural.Composite.component import FileSystemComponent


class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def details(self):
        print(f"Directory: {self.name}")
        for child in self.children:
            print(child.details())
