
# This is class User

class User:
    def __init__(self, id = 0, name = "", email = "", folder_path = ""):
        self.id = id
        self.name = name
        self.email = email
        self.folder_path = folder_path

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getFolderPath(self):
        return self.folder_path

    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setEmail(self, email):
        self.email = email

    def setFolderPath(self, folder_path):
        self.folder_path = folder_path