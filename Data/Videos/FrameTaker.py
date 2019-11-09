import cv2
import os
VideosDir = os.getcwd()
os.chdir("../Images/")
ImagesDir = os.getcwd()
os.chdir("../Videos/")

nthFrame = 75 # interval between selected frames to downloaded
def FrameCapture(fileName):
    path = VideosDir + "\\" + fileName # Converts file name into a path
    vidObj = cv2.VideoCapture(path) # Opens the video
    count = 0 # Current Frame
    success = 1 # Manages whether we are past/on the last frame
    while success:
        for i in range(nthFrame):
            # Skipping Frames
            success, image = vidObj.read()
            count += 1

        # Saves the frames with frame-count
        cv2.imwrite("../Images//" + fileName[:-4]+ "-Frame%d.jpg" % count, image)
        print("Frame %d written" % count)
    # Delete the last image, which is usually null
    os.remove("../Images//" + fileName[:-4]+ "-Frame%d.jpg" % count)

print("What file do you want to get frames from?")
fileInput = input("File Name: ")
FrameCapture(fileInput)
print("FINISHED")
