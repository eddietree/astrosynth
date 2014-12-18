import Object
import SceneIntro

class SceneManager(Object.Object):
    """A simple scene class"""

    def __init__(self):
    	self.stack = [] 
        self.scene = None

        self.pushScene(SceneIntro.SceneIntro())
        
    def pushScene(self, scene):
        self.stack.append(scene)
        self.scene = scene

    def popScene(self):
        self.stack.pop()
        self.scene = self.stack[-1]

    def currScene(self):
        return self.scene      

    def update(self):
        if self.scene != None:
            self.scene.update()

    def draw(self):
        if self.scene != None:
            self.scene.draw()

def GetSceneItem(id):
	return g_core.scene_mngr.scene.getItem(id)