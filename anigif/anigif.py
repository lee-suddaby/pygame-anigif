import numpy as np
import pygame

#------------------------------AnimatedGif Class------------------------------
#Custom object containing data for displaying an animated GIF
#Created as python is not very friendly when it comes to interacting with animated GIFs
class AnimatedGif:
    #Constructor - Should be relatively self-explanatory. new_paths is an array of file paths as strings
    def __init__(self, new_x, new_y, new_w, new_h, new_paths):
        self.frameCounter = 0 #Index of frame array that contains the next image to be displayed
        self.gif_x = new_x
        self.gif_y = new_y
        self.gif_w = new_w
        self.gif_h = new_h
        self.noOfFrames = len(new_paths)
        self.framePaths = np.array(new_paths) #Array of string, to store the file paths
        self.frames = np.array([None] * self.noOfFrames) #Array of pygame Surface objects, to store the actual graphical frames
        for n in range(self.noOfFrames):
            self.frames[n] = pygame.transform.scale(pygame.image.load(new_paths[n]), [self.gif_w, self.gif_h])

    #Return next frame of the GIF to be displayed
    #Set to loop the GIF indefinitely
    def getCurFrame(self):
        self.frameCounter = self.frameCounter + 1
        if self.frameCounter  >= self.noOfFrames:
            self.frameCounter = 0 #Play GIF from beginning as frame cycle completed
        return self.frames[self.frameCounter]