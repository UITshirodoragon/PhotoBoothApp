class Image:
    def __init__(self, path, name, user_id, filter, brightness):
        self.path = path
        self.name = name
        self.user_id = user_id
        self.filter = filter
        self.brightness = brightness

    def getPath(self):
        return self.path

    def getName(self):
        return self.name

    def getUserId(self):
        return self.user_id

    def getFilter(self):
        return self.filter

    def getBrightness(self):
        return self.brightness

    def setPath(self, path):
        self.path = path

    def setName(self, name):
        self.name = name

    def setUserId(self, user_id):
        self.user_id = user_id

    def setFilter(self, filter):
        self.filter = filter

    def setBrightness(self, brightness):
        self.brightness = brightness
