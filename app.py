from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDir, QModelIndex
from PyQt5.QtWidgets import QFileDialog, QFileSystemModel, QMainWindow, QFileDialog, QMessageBox, QDialog, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from ui_file import Ui_Dialog
import sys

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.load_button.clicked.connect(self.on_button_clicked)


    def on_button_clicked(self):
            
        real = (self.ui.spinBox_1.value(), self.ui.spinBox_4.value(),
                self.ui.spinBox_9.value(), self.ui.spinBox_8.value(),
                self.ui.spinBox_15.value(), self.ui.spinBox_14.value(),
                self.ui.spinBox_16.value(), self.ui.spinBox_24.value(),
                self.ui.spinBox_27.value(), self.ui.spinBox_48.value(),
                self.ui.spinBox_34.value(), self.ui.spinBox_35.value(),
                self.ui.spinBox_29.value(), self.ui.spinBox_32.value(),
                self.ui.spinBox_41.value(), self.ui.spinBox_44.value(),
                self.ui.spinBox_52.value(), self.ui.spinBox_77.value(),
                self.ui.spinBox_61.value(), self.ui.spinBox_62.value(),
                self.ui.spinBox_54.value(), self.ui.spinBox_58.value(),
                self.ui.spinBox_68.value(), self.ui.spinBox_73.value(),
                self.ui.spinBox_69.value(), self.ui.spinBox_56.value())
        
        im =   (self.ui.spinBox_2.value(), self.ui.spinBox_6.value(),
                self.ui.spinBox_12.value(), self.ui.spinBox_7.value(),
                self.ui.spinBox_23.value(), self.ui.spinBox_13.value(),
                self.ui.spinBox_21.value(), self.ui.spinBox_17.value(),
                self.ui.spinBox_46.value(), self.ui.spinBox_47.value(),
                self.ui.spinBox_25.value(), self.ui.spinBox_40.value(),
                self.ui.spinBox_38.value(), self.ui.spinBox_36.value(),
                self.ui.spinBox_31.value(), self.ui.spinBox_37.value(),
                self.ui.spinBox_75.value(), self.ui.spinBox_76.value(),
                self.ui.spinBox_49.value(), self.ui.spinBox_67.value(),
                self.ui.spinBox_65.value(), self.ui.spinBox_63.value(),
                self.ui.spinBox_57.value(), self.ui.spinBox_64.value(),
                self.ui.spinBox_59.value(), self.ui.spinBox_51.value())
        
        
        print(real)
        print(im)

        
        #print(result)  
        #return result  


  
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
   
    sys.exit(app.exec_())