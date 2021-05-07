class GameObjectManager:
    def __init__(self):
        self.gameObjects = []

    def addObject(self, obj):
        obj.objectManager = self
        self.gameObjects.append(obj)

    def initAll(self):
      for gameObject in self.gameObjects:
            gameObject.initWithManager()

    def runAll(self):
        for gameObject in self.gameObjects:
            gameObject.run()