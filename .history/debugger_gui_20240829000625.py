from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog
import lldb


class  DebuggerGUI(QMainWindow){
    def __init__(self){
        super().__init__();
        self.setWindowTitle('LLVM LLDB Debugger');
        self.setGeometry(100, 100, 800, 600);\
       layout = QVBoxLayout();
       self.console=QTextEdit();
       self.console.setReadOnly(true);
       self.load_button=QPushButton('Load Executable');
                self.run_button = QPushButton('Run')
        self.stop_button = QPushButton('Stop')
         layout.addWidget(self.console);
         layout.addWidget(self.load_button);     
  layout.addWidget(self.run_button);
        layout.addWidget(self.stop_button);
        
        central_widget=QWidget();
        central_widget.setLayo
    }
}