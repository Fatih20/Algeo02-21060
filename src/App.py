from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from plyer import filechooser
from PIL import Image
from datetime import datetime
from processing import *


class NormalWindow(Screen):
    testMatrixEigen = None
    testMatrixY = None
    testPathList = []
    testMatrixAverage = None
    testInserted = False
    trainingSetSize = 256

    def getTestImage(self):
        try:
            path = filechooser.open_file(
                title="Pick a test image", filters=["*.jpg"])
            self.ids.testImage.source = path[0]
            temp = self.ids.testImage.source.split('\\')
            self.ids.fileLabel.text = temp[len(temp)-1]
        except:
            pass

    def getFolderName(self):
        try:
            path = filechooser.choose_dir(
                title="Choose the folder containing your training set")
            self.ids.folderName.text = path[0]
            temp = self.ids.folderName.text.split('\\')
            self.ids.folderLabel.text = temp[len(temp)-1]
        except:
            pass

    def showResultImage(self, pathname):
        try:
            self.ids.resultImage.source = pathname[0]
        except:
            pass

    def getCurrentTime(self):
        time = datetime.now()
        jam = time.hour
        menit = time.minute
        detik = time.second
        mikro = time.microsecond
        return [jam, menit, detik, mikro]

    def subtractAndShowTime(self, jam2, jam1, menit2, menit1, detik2, detik1, mikro2, mikro1):
        to_show = ((jam2 - jam1)*3600*1000000 + (menit2-menit1)*60*1000000 + (detik2-detik1)*1000000 + (mikro2 - mikro1)) / 1000000
        self.ids.processingTime.text = f"{to_show:.2f} secs"

    def startTrainingSet(self):
        if (self.ids.folderName.text != ""):
            self.ids.processingTime.text = "Loading..."
            Clock.schedule_once(self.processTrainingSet, 0)

    def processTrainingSet(self, interval):
        jam1 = jam2 = menit1 = menit2 = detik1 = detik2 = mikro1 = mikro2 = 0

        timeArr = self.getCurrentTime()
        jam1 = timeArr[0]
        menit1 = timeArr[1]
        detik1 = timeArr[2]
        mikro1 = timeArr[3]

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
        mikro2 = timeArr[3]

        self.subtractAndShowTime(
            jam2, jam1, menit2, menit1, detik2, detik1, mikro2, mikro1)

    def startBestImage(self):
        if (self.ids.testImage.source != "Images/placeHolderImage.png" and self.testInserted == True):
            self.ids.processingTime.text = "Loading..."
            Clock.schedule_once(self.searchBestImage, 0)

    def searchBestImage(self, interval):
        jam1 = jam2 = menit1 = menit2 = detik1 = detik2 = mikro1 = mikro2 = 0

        timeArr = self.getCurrentTime()
        jam1 = timeArr[0]
        menit1 = timeArr[1]
        detik1 = timeArr[2]
        mikro1 = timeArr[3]

        im = Image.open(self.ids.testImage.source).resize(
            (self.trainingSetSize, self.trainingSetSize)).save("testImage.jpg", quality=100)
        testedImage = "testImage.jpg"
        self.ids.resultImage.source = bestface(
            self.testMatrixAverage, self.testMatrixEigen, self.testMatrixY, self.testPathList, testedImage)
        temp = self.ids.resultImage.source.split("\\")
        temp2 = temp[len(temp)-1].split('/')
        self.ids.bestFace.text = temp2[1]

        timeArr = self.getCurrentTime()
        jam2 = timeArr[0]
        menit2 = timeArr[1]
        detik2 = timeArr[2]
        mikro2 = timeArr[3]

        self.subtractAndShowTime(
            jam2, jam1, menit2, menit1, detik2, detik1, mikro2, mikro1)

class CameraWindow(Screen):
    testMatrixEigen = None
    testMatrixY = None
    testPathList = []
    testMatrixAverage = None
    testInserted = False
    trainingSetSize = 256

    def startCapturing(self):
        if (self.testInserted == True):
            Clock.schedule_interval(self.processCaptureImage, 2)

    def processCaptureImage(self, interval):
        self.ids.camera.export_to_png("Images/cameraImage.png")
        png = Image.open("Images/cameraImage.png").crop((256,
                                                         176, 512, 432)).convert("RGBA")
        bg = Image.new('RGBA', png.size, (255, 255, 255))
        alpha = Image.alpha_composite(bg, png).convert("RGB")
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
        return kivy

if __name__ == '__main__':
    mainApp().run()