# 1_Qt_desi_import.py

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()  

    # uic.loadUi()를 사용하여 qt_design_1.ui 파일을
    # MainWindow 객체 (self)에 로드.
    uic.loadUi("1_qt_design_1.ui", self)    

    self.pushButton.clicked.connect(self.copy_text)

  def copy_text(self):
    text = self.textEdit.toPlainText()
    QMessageBox.information(self, "확인", "입력문자열 : " + text)    
    # QMessageBox는 메시지 박스를 생성하는 클래스
    # information() 메서드는 정보 메시지 박스를 생성
    # self는 MainWindow 객체를 참조
    # "확인"은 메시지 박스의 제목
    # "입력문자열 : " + text는 메시지 박스의 내용
    # QMessageBox는 사용자가 확인 버튼을 클릭할 때까지 대기

# QApplication은 GUI 프로그램을 실행하기 위한 필수 객체
# QApplication 객체를 생성하고, MainWindow를 실행
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
