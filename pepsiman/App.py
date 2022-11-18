from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen

from processing import *
import time


class NormalWindow(Screen):
    testMatrixEigen = None
    testMatrixY = None
    testPathList = []
    testMatrixAverage = None
    testInserted = False

    # Show test image

    def showTestImage(self, pathname):
        try:
            self.ids.testImage.source = pathname[0]
        except:
            pass

    # Save training set folder name
    def saveFolder(self, pathname):
        try:
            self.ids.folderName.text = pathname[0]
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
    def processTrainingSet(self):
        if (self.ids.folderName.text != ""):
            jam1 = jam2 = menit1 = menit2 = detik1 = detik2 = 0

            timeArr = self.getCurrentTime()
            jam1 = timeArr[0]
            menit1 = timeArr[1]
            detik1 = timeArr[2]

            # Proses training set
            sampleFolder = self.ids.folderName.text
            path_list = path_generator(sampleFolder)
            flat_matrix_list = image_f_matrix_generator(sampleFolder)
            average_matrix = average_flatten_generator(flat_matrix_list)
            training_matrix = training_matrix_generator(
                flat_matrix_list, average_matrix)
            training_matrix_t = np.transpose(training_matrix)
            covariant_acc = np.matmul(training_matrix_t, training_matrix)
            ev, e = eigen_generator(covariant_acc, training_matrix)
            y = y_generator(covariant_acc, training_matrix)

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

    # Search for best image
    def searchBestImage(self):
        if (self.ids.testImage.source != "Images/LoadingIcon.png" and self.testInserted == True):
            # Clock.schedule_interval(self.showLoading(), 0)
            jam1 = jam2 = menit1 = menit2 = detik1 = detik2 = 0

            timeArr = self.getCurrentTime()
            jam1 = timeArr[0]
            menit1 = timeArr[1]
            detik1 = timeArr[2]

            # time.sleep(3)

            # Cari bestface ada di sini
            testedImage = self.ids.testImage.source
            file_of_bestface = bestface(
                self.testMatrixAverage, self.testMatrixEigen, self.testMatrixY, self.testPathList, testedImage)
            self.ids.resultImage.source = file_of_bestface

            timeArr = self.getCurrentTime()
            jam2 = timeArr[0]
            menit2 = timeArr[1]
            detik2 = timeArr[2]

            self.subtractAndShowTime(
                jam2, jam1, menit2, menit1, detik2, detik1)


class CameraWindow(Screen):
    # testMatrixEigen = None
    # testMatrixY = None
    # testPathList = []
    # testMatrixAverage = None
    # testInserted = False

    # def startCapturing(self):
    #     if (self.cameraMatrixEigen != None and self.ids.camera.play == True):
    #         Clock.schedule_interval(self.processCaptureImage, 10)

    # def processCaptureImage(self, interval):
    #     print('a')

    # def stopCapturing(self):
    #     Clock.unschedule(self.processCaptureImage)
    
    pass


class WindowManager(ScreenManager):
    pass


kivy = Builder.load_file("GUI.kv")


class mainApp(App):
    def build(self):
        #Window.clearcolor = (209/255.0, 1, 130/255.0, 1)
        return kivy


if __name__ == '__main__':
    mainApp().run()
