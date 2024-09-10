import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel, QPushButton, QVBoxLayout  

class Pencere(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.yazi_alani = QTextEdit()
        self.buton = QPushButton("Çekiliş yap")
        self.sonuc = QLabel("")

        v_box = QVBoxLayout()

        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.sonuc)
        v_box.addWidget(self.buton)

        self.buton.clicked.connect(self.karistir)

        self.setLayout(v_box)
        self.show()


    def karistir(self):
        
        data = self.yazi_alani.toPlainText()
        args = data.split("\n")
        rastgele_arg = random.choice(args)
        self.sonuc.setText(rastgele_arg + " " + "Çekilişi kazandı !!")



     

app = QApplication(sys.argv)
pencere = Pencere()

sys.exit(app.exec_())

