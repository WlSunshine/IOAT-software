from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter,QPalette,QColor
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
import sys
import Survival_Curve_thread
import Survival_Curve_feature_thread

font_color="color:white;"
background_color="background-color:#37474F"
MainWindow_background_color="background-color:#363636"
border_style="border:1px solid gray;"

modleborder_style = "border:1px solid #4F4F4F;"
modlepadding = "padding:5ex;"
modlefont_color = "QWidget{ color:white }"

class Survival_Curve(QtWidgets.QMainWindow, Survival_Curve_thread.Survival_Curve_feature_class, Survival_Curve_feature_thread.Survival_Curve_feature_thread):

    def __init__(self):

        QtWidgets.QMainWindow.__init__(self)
        Survival_Curve_thread.Survival_Curve_feature_class.__init__(self)
        Survival_Curve_feature_thread.Survival_Curve_feature_thread.__init__(self)

        
        self.font_max = QtGui.QFont()
        self.font_max.setPointSize(12)
        self.font_max.setBold(True)
        self.font_max.setWeight(75)
        
        self.font_min = QtGui.QFont()
        self.font_min.setPointSize(10)
        self.font_min.setBold(False)
        self.font_min.setWeight(50)
        
        
        self.font_result = QtGui.QFont("Consolas")
        self.font_result.setPointSize(10)
        self.font_result.setBold(False)
        self.font_result.setWeight(50)
        


    def _getsizePolicy(self, item, horizontal, vertical):
        '''
        :param item:object to add
        :param horizontal,vertical: Fixed,Minimum,Maximum,Preferred,Expanding,Ignored,MinimumExpanding
        :return:
        '''
        horizontal = 'QtWidgets.QSizePolicy.' + horizontal
        vertical = 'QtWidgets.QSizePolicy.' + vertical
        sizePolicy = QtWidgets.QSizePolicy(eval(horizontal), eval(vertical))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(item.sizePolicy().hasHeightForWidth())
        return sizePolicy

    def _setupStep2_Survival_Curve(self):
        # ===============Step2_setupStep2_Survival_Curve BOX  
        self.Step2_Survival_Curve = QtWidgets.QGroupBox(self.Survival_curve_frame)
        self.Step2_Survival_Curve.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Step2_Survival_Curve.setFont(self.font_max)
        self.Step2_Survival_Curve.setObjectName("Step2_Survival_Curve")
        self.Step2_Survival_Curve.setTitle("Survival Curve for label")
        
        self.Step2_Survival_Curve.setStyleSheet(
            "QWidget#Step2_Survival_Curve" + "{" + modleborder_style + modlepadding + "}" + modlefont_color)

        # ===============Step1_data_path_label "Data path   "label
        self.Step2_data_path_label_survival = QtWidgets.QLabel(self.Step2_Survival_Curve)
        # self.Step2_data_path_label_survival.setSizePolicy(self._getsizePolicy_survival(self.Step2_data_path_label_survival, 'Fixed', 'Preferred'))
        self.Step2_data_path_label_survival.setFont(self.font_min)
        self.Step2_data_path_label_survival.setObjectName("Step2_data_path_label")
        self.Step2_data_path_label_survival.setText("Data path   ")

        # ===============Step2_data_path
        self.Step2_data_path_survival = QtWidgets.QLineEdit(self.Step2_Survival_Curve)
        # self.Step2_data_path_survival.setSizePolicy(self._getsizePolicy_survival(self.Step2_data_path_survival, 'Expanding', 'Fixed'))
        self.Step2_data_path_survival.setFont(self.font_min)
        self.Step2_data_path_survival.setObjectName("Step2_data_path")
        
        self.Step2_data_path_survival.setStyleSheet(modleborder_style)

        # ===============Step2_data_path_ok_survival   Select path
        self.Step2_data_path_ok_survival = QtWidgets.QPushButton(self.Step2_Survival_Curve)
        # self.Step2_data_path_ok_survival.setSizePolicy(self._getsizePolicy_survival(self.Step2_data_path_ok_survival, 'Fixed', 'Fixed'))
        self.Step2_data_path_ok_survival.setFont(self.font_min)
        self.Step2_data_path_ok_survival.setMouseTracking(False)
        self.Step2_data_path_ok_survival.setObjectName("Step2_data_path_ok_survival")
        self.Step2_data_path_ok_survival.setText("Select Path")
       
        self.Step2_data_path_ok_survival.setStyleSheet(background_color)

        # Survival Picture
        self.Step2_Survival_Curve_label = QtWidgets.QLabel(self.Step2_Survival_Curve)
        self.Step2_Survival_Curve_label.setSizePolicy(self._getsizePolicy(self.Step2_Survival_Curve_label, 'Fixed', 'Fixed'))
        self.Step2_Survival_Curve_label.setFont(self.font_min)
        self.Step2_Survival_Curve_label.setObjectName("Step2_Truncation_label")
        self.Step2_Survival_Curve_label.setText("Survival Curve")

        self.Step2_Survival_Curve_Picture = QtWidgets.QComboBox(self.Step2_Survival_Curve)
        self.Step2_Survival_Curve_Picture.setFont(self.font_min)
        self.Step2_Survival_Curve_Picture.setObjectName("Step2_Survival_Curve_Picture")
        self.Step2_Survival_Curve_Picture.addItems(['              Survival Analysis'])
       
        self.Step2_Survival_Curve_Picture.setStyleSheet(background_color)

        # ===============Step2_Survival_Picture_ok   Select ok
        self.Step2_Survival_Picture_ok = QtWidgets.QPushButton(self.Step2_Survival_Curve)
        self.Step2_Survival_Picture_ok.setSizePolicy(self._getsizePolicy(self.Step2_Survival_Picture_ok, 'Fixed', 'Fixed'))
        self.Step2_Survival_Picture_ok.setFont(self.font_min)
        self.Step2_Survival_Picture_ok.setMouseTracking(False)
        self.Step2_Survival_Picture_ok.setObjectName("Step2_Survival_Picture_ok")
        self.Step2_Survival_Picture_ok.setText("     OK    ")
       
        self.Step2_Survival_Picture_ok.setStyleSheet(background_color)

        # Set the layout position of the Step2 control
        self.gridLayout_1step2 = QtWidgets.QGridLayout(self.Step2_Survival_Curve)
        self.gridLayout_1step2.setObjectName("gridLayout_1step2")

        self.gridLayout_1step2.addWidget(self.Step2_data_path_label_survival, 0, 0, 1, 1)
        self.gridLayout_1step2.addWidget(self.Step2_data_path_survival, 0, 1, 1, 3)
        self.gridLayout_1step2.addWidget(self.Step2_data_path_ok_survival, 0, 4, 1, 1)

        self.gridLayout_1step2.addWidget(self.Step2_Survival_Curve_label, 1, 0, 1, 1)
        self.gridLayout_1step2.addWidget(self.Step2_Survival_Curve_Picture, 1, 1, 1, 3)
        self.gridLayout_1step2.addWidget(self.Step2_Survival_Picture_ok, 1, 4, 1, 1)

    def _setupSurvival_Curve(self):
        # ===============setupStep5_Survival_Curve BOX  
        self.Survival_Curve = QtWidgets.QGroupBox(self.Survival_curve_frame)
        self.Survival_Curve.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Survival_Curve.setFont(self.font_max)
        self.Survival_Curve.setObjectName("Survival_Curve")
        self.Survival_Curve.setTitle("Survival Curve for Features")
    
        self.Survival_Curve.setStyleSheet(
            "QWidget#Survival_Curve" + "{" + modleborder_style + modlepadding + "}" + modlefont_color)

        # ===============Survival_Curve_data_label "Data path   "label
        self.Survival_Curve_data_label = QtWidgets.QLabel(self.Survival_Curve)
        self.Survival_Curve_data_label.setSizePolicy(
            self._getsizePolicy(self.Survival_Curve_data_label, 'Fixed', 'Fixed'))
        self.Survival_Curve_data_label.setFont(self.font_min)
        self.Survival_Curve_data_label.setObjectName("Survival_Curve_data_label")
        self.Survival_Curve_data_label.setText("data path      ")

        # ===============Survival_Curve_data_path
        self.Survival_Curve_data_path = QtWidgets.QLineEdit(self.Survival_Curve)
        self.Survival_Curve_data_path.setSizePolicy(
            self._getsizePolicy(self.Survival_Curve_data_path, 'Preferred', 'Preferred'))
        self.Survival_Curve_data_path.setFont(self.font_min)
        self.Survival_Curve_data_path.setObjectName("Survival_Curve_data_path")
        
        self.Survival_Curve_data_path.setStyleSheet(modleborder_style)

        # ===============Survival_Curve_data_path_ok   Select path
        self.Survival_Curve_data_path_ok = QtWidgets.QPushButton(self.Survival_Curve)
        self.Survival_Curve_data_path_ok.setSizePolicy(
            self._getsizePolicy(self.Survival_Curve_data_path_ok, 'Fixed', 'Fixed'))
        self.Survival_Curve_data_path_ok.setFont(self.font_min)
        self.Survival_Curve_data_path_ok.setMouseTracking(False)
        self.Survival_Curve_data_path_ok.setObjectName("Survival_Curve_data_path_ok")
        self.Survival_Curve_data_path_ok.setText("Select Path")
        
        self.Survival_Curve_data_path_ok.setStyleSheet(background_color)

        # variable name_label
        self.Survival_Curve_Variable_Name_label = QtWidgets.QLabel(self.Survival_Curve)
        self.Survival_Curve_Variable_Name_label.setSizePolicy(
            self._getsizePolicy(self.Survival_Curve_Variable_Name_label, 'Fixed', 'Fixed'))
        self.Survival_Curve_Variable_Name_label.setFont(self.font_min)
        self.Survival_Curve_Variable_Name_label.setObjectName("Survival_Curve_Variable_Name_label")
        self.Survival_Curve_Variable_Name_label.setText("Variable      ")

        # variable_name
        self.Survival_Curve_Variable_name = QtWidgets.QLineEdit(self.Survival_Curve)
        self.Survival_Curve_Variable_name.setSizePolicy(
            self._getsizePolicy(self.Survival_Curve_Variable_name, 'Preferred', 'Preferred'))
        self.Survival_Curve_Variable_name.setFont(self.font_min)
        self.Survival_Curve_Variable_name.setObjectName("Survival_Curve_Variable_name")
        self.Survival_Curve_Variable_name.setStyleSheet(modleborder_style)

        # Survival curve ok
        self.Survival_Curve_ok = QtWidgets.QPushButton(self.Survival_Curve)
        self.Survival_Curve_ok.setSizePolicy(self._getsizePolicy(self.Survival_Curve_ok, 'Fixed', 'Fixed'))
        self.Survival_Curve_ok.setFont(self.font_min)
        self.Survival_Curve_ok.setMouseTracking(False)
        self.Survival_Curve_ok.setObjectName("Survival_Curve_ok")
        self.Survival_Curve_ok.setText("     OK    ")
     
        self.Survival_Curve_ok.setStyleSheet(background_color)

        # Step5 Control layout position setting
        self.gridLayout_1 = QtWidgets.QGridLayout(self.Survival_Curve)
        self.gridLayout_1.setObjectName("gridLayout_1")
       
        self.gridLayout_1.addWidget(self.Survival_Curve_data_label, 0, 0, 1, 1)
        self.gridLayout_1.addWidget(self.Survival_Curve_data_path, 0, 1, 1, 3)
        self.gridLayout_1.addWidget(self.Survival_Curve_data_path_ok, 0, 4, 1, 1)
        
        self.gridLayout_1.addWidget(self.Survival_Curve_Variable_Name_label, 1, 0, 1, 1)
        self.gridLayout_1.addWidget(self.Survival_Curve_Variable_name, 1, 1, 1, 3)
        self.gridLayout_1.addWidget(self.Survival_Curve_ok, 1, 4, 1, 1)

    def _setupResult(self):
        self.Result = QtWidgets.QGroupBox(self.Survival_curve_frame)
        self.Result.setSizePolicy(self._getsizePolicy(self.Result, 'Preferred', 'Preferred'))
        self.Result.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Result.setFont(self.font_max)
        self.Result.setObjectName("result")
        self.Result.setTitle("Result")
    
        self.Result.setStyleSheet("border:1px solid #4F4F4F ; padding : 5ex ; color : white ")

        self.Result_text = QtWidgets.QTextBrowser(self.Result)
        self.Result_text.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Result_text.setObjectName("result_text")
        self.Result_text.setFont(self.font_result)
        self.Result_text.focusNextPrevChild(True)

        self.gridLayout_result = QtWidgets.QGridLayout(self.Result)
        self.gridLayout_result.setObjectName("gridLayout_result")
        self.gridLayout_result.addWidget(self.Result_text, 0, 1, 1, 1)

    def setupSurvival_curve(self):
        self.Survival_curve_frame = QtWidgets.QWidget()
        self.Survival_curve_frame.setObjectName("Survival_curve_frame")

        self.Survival_curve_frame.setStyleSheet(MainWindow_background_color)
        
        ## result box
        self._setupStep2_Survival_Curve()
        self._setupSurvival_Curve()
        self._setupResult()
        
        self.gridLayout_Survival_curve_frame = QtWidgets.QGridLayout(self.Survival_curve_frame)
        self.gridLayout_Survival_curve_frame.setObjectName("gridLayout_Survival_curve_frame")

        self.gridLayout_Survival_curve_frame.addWidget(self.Step2_Survival_Curve, 0, 0, 3, 1)
        self.gridLayout_Survival_curve_frame.addWidget(self.Survival_Curve, 3, 0, 3, 1)
        self.gridLayout_Survival_curve_frame.addWidget(self.Result, 0, 1, 15, 1)
        
        self.gridLayout_Survival_curve_frame.setColumnStretch(0, 5)
        self.gridLayout_Survival_curve_frame.setColumnStretch(1, 5)

        ### connect to the functions
        # =================================================================== #
#==============================================================================
#         sys.stdout = Survival_Curve_thread.port(self.Result_text)
#==============================================================================
        self.Step2_data_path_ok_survival.clicked.connect(self.Select_a_path)
        self.Step2_Survival_Picture_ok.clicked.connect(self._Survival_Curve)
        self.Survival_Curve_data_path_ok.clicked.connect(self.Select_a_path_feature)
        self.Survival_Curve_ok.clicked.connect(self.Survival_Curve_feature)

        
        # =================================================================== #
        return self.Survival_curve_frame
