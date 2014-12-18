import Object

class Scene(Object.Object):
    """A simple scene class"""

    def __init__(self):
    	self.data = {}

    def add(self, item, id):
    	self.data[name] = item

    def update(self):
    	for key in self.data:
    		self.data[key].update()

    def draw(self):
    	for key in self.data:
    		self.data[key].draw()

def GetSceneItem(id):
	return g_core.scene_mngr.scene[id]