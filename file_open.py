
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog

def file_open(indicator):
    """Returns the path of the chosen file"""
    
    app = QApplication(sys.argv)
    
    if indicator == 'single':
        """Open a Single File"""    
        file , check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                                "", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")
        return file

    elif indicator == 'multiple':
        """Opens Multiple Files"""
        file , check = QFileDialog.getOpenFileNames(None, "QFileDialog.getOpenFileName()",
                                                "", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")                             
        return file
