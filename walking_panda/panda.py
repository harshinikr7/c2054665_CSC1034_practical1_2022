from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor


class WalkingPanda(ShowBase):
    def __init__(self, Audio=True, scale=True, no_rotate=False, color=True, speed_change =True, no_environment =False):
        ShowBase.__init__(self)
         ## And The rest

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        if (no_environment == False):
            self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add the spinCameraTask procedure to the task manager.
        if (no_rotate == False):
           self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")

        if (color == True):
            self.pandaActor.set_color_scale(1,0,0,1.0)
            self.pandaActor.reparentTo(self.render)
        # change color of panda

        if (Audio == True):
            mysound= self.loader.loadSfx("walking_panda/music.mp3")
            mysound.play()
         # play music along with the animation

        if (scale == True):
            self.pandaActor.set_scale(1,1,1)
        # change the size of panda to desired parameters

        if (speed_change == True):
            self.pandaActor.setPlayRate(5.0, 'walk')
        # to change the walking speed of the panda with desired parameters

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont





