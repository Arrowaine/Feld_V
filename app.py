from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QDialog, QGraphicsScene, QGraphicsPixmapItem, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from ui_file import Ui_Dialog
import sys
import setup_body,setup

def display_image_in_graphicsview(pixmap, graphics_view):

    scene = QGraphicsScene()
    pixmap_item = QGraphicsPixmapItem(pixmap)
    scene.addItem(pixmap_item)
    graphics_view.setScene(scene)
    graphics_view.fitInView(pixmap_item, Qt.KeepAspectRatio)


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.load_button.clicked.connect(self.on_button_clicked)
        self.ui.saveButton.clicked.connect(self.save_as_image)

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
               
        #Генерация персонажа
        factors = setup.create_factors(real=real,im = im)
        pixmap = setup_body.pil_to_pixmap(setup_body.assemble_body(factors[0]))
        display_image_in_graphicsview(pixmap, self.ui.graphicsView_2)
        
        pixmap2 = QPixmap("assets\\real_human.jpg")
        scene = QGraphicsScene()

        pixmap_item = QGraphicsPixmapItem(pixmap2)
        scene.addItem(pixmap_item)

        self.ui.graphicsView.setScene(scene)
        self.ui.graphicsView.fitInView(pixmap_item, Qt.KeepAspectRatio)

        # Вывод факторного анализа   
        self.ui.s_0.setText(f'{factors[1][0]}')
        self.ui.s_1.setText(f'{factors[1][1]}')
        self.ui.s_2.setText(f'{factors[1][2]}')
        self.ui.s_3.setText(f'{factors[1][3]}')
        self.ui.s_4.setText(f'{factors[1][4]}')
        self.ui.s_5.setText(f'{factors[1][5]}')
        self.ui.s_6.setText(f'{factors[1][6]}')

        self.ui.stext_0.setText(setup.text_s_score(factors[1][0]))
        self.ui.stext_1.setText(setup.text_s_score(factors[1][1]))
        self.ui.stext_2.setText(setup.text_s_score(factors[1][2]))
        self.ui.stext_3.setText(setup.text_s_score(factors[1][3]))
        self.ui.stext_4.setText(setup.text_s_score(factors[1][4]))
        self.ui.stext_5.setText(setup.text_s_score(factors[1][5]))
        self.ui.stext_6.setText(setup.text_s_score(factors[1][6]))

        self.ui.im_0.setText(f'{factors[0][0]:.0f}%')
        self.ui.im_1.setText(f'{factors[0][1]:.0f}%')
        self.ui.im_2.setText(f'{factors[0][2]:.0f}%')
        self.ui.im_3.setText(f'{factors[0][3]:.0f}%')
        self.ui.im_4.setText(f'{factors[0][4]:.0f}%')
        self.ui.im_5.setText(f'{factors[0][5]:.0f}%')
        self.ui.im_6.setText(f'{factors[0][6]:.0f}%')        
        
    def save_as_image(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить", "", "PNG (*.png)")
        if file_path:
            self.grab().save(file_path)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show() 
    sys.exit(app.exec_())