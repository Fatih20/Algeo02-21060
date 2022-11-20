from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from plyer import filechooser
from PIL import Image
import time

from processing import *


class NormalWindow(Screen):
    testMatrixEigen = None
    testMatrixY = None
    testPathList = []
    testMatrixAverage = None
    testInserted = False
    trainingSetSize = 256

    # Show test image

    def getTestImage(self):
        try:
            path = filechooser.open_file(
                title="Pick a test image", filters=["*.jpg"])
            self.ids.testImage.source = path[0]
            temp = self.ids.testImage.source.split('\\')
            self.ids.fileLabel.text = temp[len(temp)-1]
        except:
            pass

    # Save training set folder name
    def getFolderName(self):
        try:
            path = filechooser.choose_dir(
                title="Choose the folder containing your training set")
            self.ids.folderName.text = path[0]
            temp = self.ids.folderName.text.split('\\')
            self.ids.folderLabel.text = temp[len(temp)-1]
        except:
            pass

    # Show result image
    def showResultImage(self, pathname):
        try:
            self.ids.resultImage.source = pathname[0]
        except:
            pass

    def getCurrentTime(self):
        time_tuple = time.localtime()
        time_string = time.strftime("%m/%d/%Y %H%M%S", time_tuple)

        jam = int(time_string[11:13])
        menit = int(time_string[13:15])
        detik = int(time_string[15:17])
        return [jam, menit, detik]

    def subtractAndShowTime(self, jam2, jam1, menit2, menit1, detik2, detik1):
        to_show = (jam2 - jam1)*3600 + (menit2-menit1)*60 + (detik2-detik1)
        self.ids.processingTime.text = f"{to_show} secs"

    # Process Folder
    def startTrainingSet(self):
        if (self.ids.folderName.text != ""):
            self.ids.processingTime.text = "Loading..."
            Clock.schedule_once(self.processTrainingSet, 0)

    def processTrainingSet(self, interval):
        jam1 = jam2 = menit1 = menit2 = detik1 = detik2 = 0

        timeArr = self.getCurrentTime()
        jam1 = timeArr[0]
        menit1 = timeArr[1]
        detik1 = timeArr[2]

        # Proses training set
        sample_folder = self.ids.folderName.text
        path_list, e, y, average_matrix, image_size = process_images(
            sample_folder)
        self.trainingSetSize = image_size
        self.testMatrixEigen = e
        self.testMatrixY = y
        self.testPathList = path_list
        self.testMatrixAverage = average_matrix
        self.testInserted = True

        timeArr = self.getCurrentTime()
        jam2 = timeArr[0]
        menit2 = timeArr[1]
        detik2 = timeArr[2]

        self.subtractAndShowTime(
            jam2, jam1, menit2, menit1, detik2, detik1)

    # Search for best
    def startBestImage(self):
        if (self.ids.testImage.source != "Images/placeHolderImage.png" and self.testInserted == True):
            self.ids.processingTime.text = "Loading..."
            Clock.schedule_once(self.searchBestImage, 0)

    def searchBestImage(self, interval):
        jam1 = jam2 = menit1 = menit2 = detik1 = detik2 = 0

        timeArr = self.getCurrentTime()
        jam1 = timeArr[0]
        menit1 = timeArr[1]
        detik1 = timeArr[2]

        # time.sleep(3)

        # Cari bestface ada di sini
        im = Image.open(self.ids.testImage.source).resize(
            (self.trainingSetSize, self.trainingSetSize)).save(self.ids.testImage.source, quality=100)
        testedImage = self.ids.testImage.source
        self.ids.resultImage.source = bestface(
            self.testMatrixAverage, self.testMatrixEigen, self.testMatrixY, self.testPathList, testedImage)

        timeArr = self.getCurrentTime()
        jam2 = timeArr[0]
        menit2 = timeArr[1]
        detik2 = timeArr[2]

        self.subtractAndShowTime(
            jam2, jam1, menit2, menit1, detik2, detik1)


class CameraWindow(Screen):
    testMatrixEigen = None
    testMatrixY = None
    testPathList = []
    testMatrixAverage = None
    testInserted = False
    trainingSetSize = 256

    def startCapturing(self):
        if (self.testInserted == True):  # and self.ids.camera.play == True):
            Clock.schedule_interval(self.processCaptureImage, 2)

    def processCaptureImage(self, interval):
        self.ids.camera.export_to_png("Images/cameraImage.png")
        png = Image.open("Images/cameraImage.png").crop((256,
                                                         176, 512, 432)).convert("RGBA")
        bg = Image.new('RGBA', png.size, (255, 255, 255))
        alpha = Image.alpha_composite(bg, png).convert("RGB")

        # still in progress
        alpha.resize((self.trainingSetSize, self.trainingSetSize)).save(
            "Images/cameraImage.jpg", "JPEG", quality=100)

        testedImage = "Images/cameraImage.jpg"

        file_of_bestface = bestface(
            self.testMatrixAverage, self.testMatrixEigen, self.testMatrixY, self.testPathList, testedImage)
        self.ids.cameraResultImage.source = file_of_bestface

    def stopCapturing(self):
        Clock.unschedule(self.processCaptureImage)


class WindowManager(ScreenManager):
    pass


kivy = Builder.load_file("GUI.kv")


class mainApp(App):
    def build(self):
        #Window.clearcolor = (209/255.0, 1, 130/255.0, 1)
        return kivy


if __name__ == '__main__':
    mainApp().run()
