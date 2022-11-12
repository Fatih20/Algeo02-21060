from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock

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
        
    # Start Processing
    def startProcessing(self):
        self.startStopwatch()
        pass

class mainApp(App):
    def build(self):
        Window.clearcolor = (209/255.0, 1, 130/255.0, 1)
        return mainLayout()

if __name__ == '__main__':
    mainApp().run()