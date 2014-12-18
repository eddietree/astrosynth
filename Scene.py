import Object

class Scene(Object.Object):
    """A simple scene class"""

    def __init__(self):
    	self.data = {}

    def add(self, item, id):
    	self.data[name] = item

    def getItem(self, id):
        return self.data[id]

    def update(self):
    	for key in self.data:
    		self.data[key].update()

    def draw(self):
    	for key in self.data:
    		self.data[key].draw()