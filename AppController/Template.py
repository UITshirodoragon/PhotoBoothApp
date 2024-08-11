import json

class Template:
    def __init__(self, user_id, path, style, number_of_images, images_position_list, stickers_position_list, frame_path):
        self.user_id = user_id
        self.path = path
        self.style = style
        self.number_of_images = number_of_images
        self.images_position_list = images_position_list
        self.stickers_position_list = stickers_position_list
        self.frame_path = frame_path

    def getPath(self):
        return self.path

    def getStyle(self):
        return self.style

    def getImagesPosition(self):
        return self.images_position_list

    def getStickersPosition(self):
        return self.stickers_position_list

    def getFramePath(self):
        return self.frame_path

    def setPath(self, path):
        self.path = path

    def setStyle(self, style):
        self.style = style

    def setImagesPosition(self, images_position_list):
        self.images_position_list = images_position_list

    def setStickersPosition(self, stickers_position_list):
        self.stickers_position_list = stickers_position_list

    def setFramePath(self, frame_path):
        self.frame_path = frame_path

    def save(self, filename):
        data = {
            'user_id': self.user_id,
            # ... các thuộc tính khác
            'images': self.images_position_list,
            'stickers': self.stickers_position_list
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            # Gán dữ liệu từ file vào các thuộc tính của đối tượng