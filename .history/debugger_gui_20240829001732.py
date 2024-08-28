from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog
import lldb


class  DebuggerGUI(QMainWindow){
    def __init__(self):
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
        central_widget.setLayout(layout);
        self.setCentralWidget(central_widget);
   
   self.load_button.clicked.connect(self.load_executable);
    
     self.run_button.clicked.connect(self.run_program)
        self.stop_button.clicked.connect(self.stop_program);
        
        self.debugger = lldb.SBDebugger.Create();
        self.debugger.SetAsync(False);
        self.target = None
        self.process = None
 def log_output(message):
     self.console.append(message);
 
 def load_executable(self):
     file_path,= QFileDialog.getOpenFileName(self, "Open Executable");
     if file_path:
         self.target=self.debugger.CreateTarget(file_path);    
                     self.log_output(f"Loaded executable: {file_path}")
def run_program(self):
    if self.target:
        self.process = self.target.LaunchSimple(None,None,None)
        if self.process.IsValid():
              self.log_output("Program running.")
            else:
                self.log_output("Failed to start program.")
        else:
            self.log_output("No executable loaded.")
            
            
            
            def stop_program(self):
                if self.process nad self.process.IsValid():
                self.process.kill()
                self.log_output("program stopped .")
                 else:
            self.log_output("No program running.")
            
            if __name