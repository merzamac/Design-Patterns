from structural.Composite.composite import Directory
from structural.Composite.leaf import File


def client_code():
    file1 = File("File1.txt")
    file2 = File("File2.txt")
    directory1 = Directory("Directory1")
    directory1.add(file1)
    directory1.add(file2)

    directory1.details()


def composite():
    client_code()
