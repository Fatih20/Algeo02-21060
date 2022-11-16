from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock

from processing import *

Builder.load_file("GUI.kv")


class mainLayout(Widget):
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

    def startStopwatch(self):
        Clock.schedule_interval(self.update_time, 0.01)

    def update_time(self, *args):
        self.ids.processingTime.text = f"{float(self.ids.processingTime.text) + 0.01: .2f}"
        print("a")

    def stop_time(self):
        self.ids.processingTime.text = self.ids.processingTime.text

    # Start Processing
    def startProcessing(self):
        if (self.ids.testImage.source != "Images/LoadingIcon.png" and self.ids.folderName.text != ""):
            self.ids.processingTime.text = "0.00"
            self.startStopwatch()

            testedImage = self.ids.testImage.source
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
            file_of_bestface = bestface(
                average_matrix, e, y, path_list, testedImage)
            self.ids.resultImage.source = file_of_bestface

            Clock.unschedule(self.stop_time)


class mainApp(App):
    def build(self):
        #Window.clearcolor = (209/255.0, 1, 130/255.0, 1)
        return mainLayout()


if __name__ == '__main__':
    mainApp().run()
