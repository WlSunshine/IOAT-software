import Step_by_Step_Thread_Survival
import k_means_Thread
import Survival_Curve_thread
import Survival_Curve_feature_thread


class port(object):
    def __init__(self,view):
        self.view = view
    def write(self,*args):
        self.view.append(*args)


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter,QPalette,QColor
from PyQt5.QtCore import Qt, pyqtSignal
import sys

from StepByStepClass_Survival import StepByStep_Survival
from k_means_class import StepByStep_K_Means
from Survival_Curve_class import Survival_Curve


MainWindow_background_color="background-color:#363636"
background_color="background-color:#37474F"
font_color="color:white"

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.tab1 = StepByStep_Survival()
        self.tab2 = StepByStep_K_Means()
        self.tab3 = Survival_Curve()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 780)
        MainWindow.setWindowTitle('Features Selection Of Integrated Data ')

     
        MainWindow.setStyleSheet(MainWindow_background_color)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)


        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setCurrentIndex(0)

       
        stylesheet = """ 
            QTabBar::tab:selected {background: gray;}
            QTabBar::tab{ background-color: #37474F } 
            QTabBar::tab{ color: white }
            QTabWidget::pane{ border:1px solid #4F4F4F }
            """
        self.tabWidget.setStyleSheet(stylesheet)

        ###########################
        ###### Cox Stepbystep #####
        self.Stepbystep_cox = self.tab1.setupStep_by_step_survival()
        self.tabWidget.addTab(self.Stepbystep_cox, "Feature Selection: Step by step")
        stylesheet = """ 
            QTabBar::tab:selected {background: gray;}
            QTabBar::tab{ background-color: #37474F } 
            QTabBar::tab{ color: white }
            QTabWidget::pane{ border:1px solid #4F4F4F }
            """
        self.tabWidget.setStyleSheet(stylesheet)

        #############################
        ##K_means TabWidget ##
        #############################
        self.K_Means = self.tab2.setupStep_by_step_K_Means()
        self.tabWidget.addTab(self.K_Means, 'K_Means')
        stylesheet = """
                    QTabBar::tab:selected {background: gray;}
                    QTabBar::tab{ background-color: #37474F }
                    QTabBar::tab{ color: white }
                    QTabWidget::pane{ border:1px solid #4F4F4F }
                    """
        self.tabWidget.setStyleSheet(stylesheet)

        #############################
        ##Survival Curve TabWidget ##
        #############################
        self.Survival_curve = self.tab3.setupSurvival_curve()
        self.tabWidget.addTab(self.Survival_curve, 'Survival curve')
        stylesheet = """ 
                   QTabBar::tab:selected {background: gray;}
                   QTabBar::tab{ background-color: #37474F } 
                   QTabBar::tab{ color: white }
                   QTabWidget::pane{ border:1px solid #4F4F4F }
                   """
        self.tabWidget.setStyleSheet(stylesheet)

        # Center the entire interface
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        
        self.tabWidget.currentChanged.connect(self.output_box)
    def output_box(self):
        if self.tabWidget.currentIndex() == 0:
            sys.stdout = Step_by_Step_Thread_Survival.port(self.tab1.Result_text_survival)
        elif self.tabWidget.currentIndex() == 1:
            sys.stdout = k_means_Thread.port(self.tab2.Result_survival)
        elif self.tabWidget.currentIndex() == 2:
            sys.stdout = Survival_Curve_thread.port(self.tab3.Result_text)



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

