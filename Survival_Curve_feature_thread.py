from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Survival_Curve_feature import Survival_Curve_feature
import matplotlib.pyplot as plt
import winreg
def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return(winreg.QueryValueEx(key, "Desktop")[0])

the_user_desktop = get_desktop()


class port(object):
    def __init__(self,view):
        self.view = view
    def write(self,*args):
        self.view.append(*args)


class Survival_Curve_feature_thread():
    
    def __init__(self):
        # initialize two objects in the class
        self.none = None

        
    ### define the functions
    # ======================================================================= #
    def Select_a_path_feature(self):
        # path = QtWidgets.QFileDialog.getOpenFileName(self, r"open file dialog", r"C:\Users\Administrator\Desktop", r"(*.csv)")
        path_cox = QtWidgets.QFileDialog.getOpenFileName(self, r"open file dialog", the_user_desktop, r"(*.csv)")
        if (path_cox[0]):
            self.Result_text.append("\n【Note】Choose a file path: %s \n" % path_cox[0])
            self.Survival_Curve_data_path.setText(str(path_cox[0]))
            self.path_cox_feature = path_cox[0]


    def _Survival_Curve_feature(self):
        feature_name = self.Survival_Curve_Variable_name.text()
        self.Survival_Curve_feature = Survival_Curve_feature()
        self.Survival_Curve_feature.read_data_cox(self.path_cox_feature, feature_name)
        self.Survival_Curve_feature.Cox_Label_HR()
        self.Survival_Curve_feature.estimate_kaplan_meier(feature_name)



    def Survival_Curve_feature(self):
        try:
            print("starting...maybe a few minute is needed")
            self._Survival_Curve_feature()
            plt.show()
        except Exception as e:
            self.Result_text.append("\n【Error】: %s" %e)


