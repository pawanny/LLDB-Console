from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog
import lldb


class  DebuggerGUI(QMainWindow){
    def __init__(self){
        super().__init__();
        self.setWindowTitle('LLVM LLDB Debugger');
        self.setGeometry(100, 100, 800, 600)
    }
}