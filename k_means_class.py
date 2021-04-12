from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QPalette, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
import sys
import k_means_Thread

font_color = "color:white;"
background_color = "background-color:#37474F"
MainWindow_background_color = "background-color:#363636"
border_style = "border:1px solid gray;"

modleborder_style = "border:1px solid #4F4F4F;"
modlepadding = "padding:5ex;"
modlefont_color = "QWidget{ color:white }"


class StepByStep_K_Means(QtWidgets.QMainWindow, k_means_Thread.Step_by_step_k_means):

    def __init__(self):

        QtWidgets.QMainWindow.__init__(self)
        k_means_Thread.Step_by_step_k_means.__init__(self)

       
        self.font_max_survival = QtGui.QFont()
        self.font_max_survival.setPointSize(12)
        self.font_max_survival.setBold(True)
        self.font_max_survival.setWeight(75)
        
        self.font_min_survival = QtGui.QFont()
        self.font_min_survival.setPointSize(10)
        self.font_min_survival.setBold(False)
        self.font_min_survival.setWeight(50)

        
        self.font_result_survival = QtGui.QFont("Consolas")
        self.font_result_survival.setPointSize(10)
        self.font_result_survival.setBold(False)
        self.font_result_survival.setWeight(50)

    def _getsizePolicy_survival(self, item, horizontal, vertical):
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

    def _setupStep1_load_data_survival(self):
        # ===============Step1_load_data BOX
        self.Step1_load_data_survival = QtWidgets.QGroupBox(self.Step_by_step_survival)
        # self.Step1_load_data_survival.setSizePolicy(self._getsizePolicy_survival(self.Step1_load_data_survival, 'Preferred', 'Preferred'))
        self.Step1_load_data_survival.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Step1_load_data_survival.setFont(self.font_max_survival)
        self.Step1_load_data_survival.setObjectName("Step1_load_data")
        self.Step1_load_data_survival.setTitle("Step 1 Load data")
        
        self.Step1_load_data_survival.setStyleSheet(
            "QWidget#Step1_load_data" + "{" + modleborder_style + modlepadding + "}" + modlefont_color)

        # ===============Step1_data_path_label "Data path   "label
        self.Step1_data_path_label_survival = QtWidgets.QLabel(self.Step1_load_data_survival)
        # self.Step1_data_path_label_survival.setSizePolicy(self._getsizePolicy_survival(self.Step1_data_path_label_survival, 'Fixed', 'Preferred'))
        self.Step1_data_path_label_survival.setFont(self.font_min_survival)
        self.Step1_data_path_label_survival.setObjectName("Step1_data_path_label")
        self.Step1_data_path_label_survival.setText("Data path   ")

        # ===============Step1_data_path
        self.Step1_data_path_survival = QtWidgets.QLineEdit(self.Step1_load_data_survival)
        # self.Step1_data_path_survival.setSizePolicy(self._getsizePolicy_survival(self.Step1_data_path_survival, 'Expanding', 'Fixed'))
        self.Step1_data_path_survival.setFont(self.font_min_survival)
        self.Step1_data_path_survival.setObjectName("Step1_data_path")
        
        self.Step1_data_path_survival.setStyleSheet(modleborder_style)

        # ===============Step1_data_path_ok_survival   Select path
        self.Step1_data_path_ok_survival = QtWidgets.QPushButton(self.Step1_load_data_survival)
        # self.Step1_data_path_ok_survival.setSizePolicy(self._getsizePolicy_survival(self.Step1_data_path_ok_survival, 'Fixed', 'Fixed'))
        self.Step1_data_path_ok_survival.setFont(self.font_min_survival)
        self.Step1_data_path_ok_survival.setMouseTracking(False)
        self.Step1_data_path_ok_survival.setObjectName("Step1_data_path_ok_survival")
        self.Step1_data_path_ok_survival.setText("Select Path")
        
        self.Step1_data_path_ok_survival.setStyleSheet(background_color)

        self.gridLayout_1step1_survival = QtWidgets.QGridLayout(self.Step1_load_data_survival)
        self.gridLayout_1step1_survival.setObjectName("gridLayout_1step1")
        self.gridLayout_1step1_survival.addWidget(self.Step1_data_path_label_survival, 0, 0, 1, 1)
        self.gridLayout_1step1_survival.addWidget(self.Step1_data_path_survival, 0, 1, 1, 5)
        self.gridLayout_1step1_survival.addWidget(self.Step1_data_path_ok_survival, 0, 5, 1, 1)

    def _setupStep2_preprocessing_survival(self):
        self.Step2_preprocessing_survival = QtWidgets.QGroupBox(self.Step_by_step_survival)
        self.Step2_preprocessing_survival.setSizePolicy(
            self._getsizePolicy_survival(self.Step2_preprocessing_survival, 'Preferred', 'Preferred'))
        self.Step2_preprocessing_survival.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Step2_preprocessing_survival.setFont(self.font_max_survival)
        self.Step2_preprocessing_survival.setObjectName("Step2_preprocessing")
        self.Step2_preprocessing_survival.setTitle("Step 2 preprocessing")
        
        self.Step2_preprocessing_survival.setStyleSheet(
            "QWidget#Step2_preprocessing" + "{" + modleborder_style + modlepadding + "}" + modlefont_color)

        self.Step2_inpute_label_survival = QtWidgets.QLabel(self.Step2_preprocessing_survival)
        self.Step2_inpute_label_survival.setSizePolicy(
            self._getsizePolicy_survival(self.Step2_inpute_label_survival, 'Fixed', 'Preferred'))
        self.Step2_inpute_label_survival.setFont(self.font_min_survival)
        self.Step2_inpute_label_survival.setObjectName("Step2_inpute_label")
        self.Step2_inpute_label_survival.setText("Filler")

        self.Step2_inpute_survival = QtWidgets.QComboBox(self.Step2_preprocessing_survival)
        self.Step2_inpute_survival.setFont(self.font_min_survival)
        self.Step2_inpute_survival.setObjectName("Step2_inpute")
        self.Step2_inpute_survival.addItems(['Median'])
        self.Step2_inpute_survival.addItems(['Mean'])
        
        self.Step2_inpute_survival.setStyleSheet(background_color)

        self.Step2_inpute_is_abnormal_nan_survival = QtWidgets.QCheckBox(self.Step2_preprocessing_survival)
        self.Step2_inpute_is_abnormal_nan_survival.setSizePolicy(
            self._getsizePolicy_survival(self.Step2_inpute_is_abnormal_nan_survival, 'Fixed', 'Fixed'))
        self.Step2_inpute_is_abnormal_nan_survival.setFont(self.font_min_survival)
        self.Step2_inpute_is_abnormal_nan_survival.setObjectName("Step2_inpute_is_abnormal_nan")
        self.Step2_inpute_is_abnormal_nan_survival.setText("Outliers")
        self.Step2_inpute_is_abnormal_nan_survival.setChecked(False)

        self.Step2_inpute_ok_survival = QtWidgets.QPushButton(self.Step2_preprocessing_survival)
        self.Step2_inpute_ok_survival.setSizePolicy(
            self._getsizePolicy_survival(self.Step2_inpute_ok_survival, 'Fixed', 'Fixed'))
        self.Step2_inpute_ok_survival.setFont(self.font_min_survival)
        self.Step2_inpute_ok_survival.setObjectName("Step2_inpute_ok")
        self.Step2_inpute_ok_survival.setText("OK")

        self.Step2_inpute_ok_survival.setStyleSheet(background_color)

        self.Step2_standardize_label_survival = QtWidgets.QLabel(self.Step2_preprocessing_survival)
        self.Step2_standardize_label_survival.setSizePolicy(
            self._getsizePolicy_survival(self.Step2_standardize_label_survival, 'Fixed', 'Preferred'))
        self.Step2_standardize_label_survival.setFont(self.font_min_survival)
        self.Step2_standardize_label_survival.setObjectName("Step2_standardize_label")
        self.Step2_standardize_label_survival.setText("Standardize")

        self.Step2_standardize_survival = QtWidgets.QComboBox(self.Step2_preprocessing_survival)
        self.Step2_standardize_survival.setFont(self.font_min_survival)
        self.Step2_standardize_survival.setObjectName("Step2_standardize")
        self.Step2_standardize_survival.addItems(['Standardization', 'MinMaxScaler'])
        
        self.Step2_standardize_survival.setStyleSheet(background_color)

        self.Step2_standardize_ok_survival = QtWidgets.QPushButton(self.Step2_preprocessing_survival)
        self.Step2_standardize_ok_survival.setSizePolicy(
            self._getsizePolicy_survival(self.Step2_standardize_ok_survival, 'Fixed', 'Fixed'))
        self.Step2_standardize_ok_survival.setFont(self.font_min_survival)
        self.Step2_standardize_ok_survival.setObjectName("Step2_standardize_ok")
        self.Step2_standardize_ok_survival.setText("OK")
       
        self.Step2_standardize_ok_survival.setStyleSheet(background_color)

        self.gridLayout_1step2_survival = QtWidgets.QGridLayout(self.Step2_preprocessing_survival)
        self.gridLayout_1step2_survival.setObjectName("gridLayout_1step2")

        self.gridLayout_1step2_survival.addWidget(self.Step2_standardize_label_survival, 2, 0, 1, 1)
        self.gridLayout_1step2_survival.addWidget(self.Step2_standardize_survival, 2, 1, 1, 1)
        self.gridLayout_1step2_survival.addWidget(self.Step2_standardize_ok_survival, 2, 3, 1, 1)

        self.gridLayout_1step2_survival.addWidget(self.Step2_inpute_label_survival, 0, 0, 1, 1)
        self.gridLayout_1step2_survival.addWidget(self.Step2_inpute_survival, 0, 1, 1, 1)
        self.gridLayout_1step2_survival.addWidget(self.Step2_inpute_is_abnormal_nan_survival, 0, 2, 1, 1)
        self.gridLayout_1step2_survival.addWidget(self.Step2_inpute_ok_survival, 0, 3, 1, 1)

        self.gridLayout_1step2_survival.setColumnStretch(0, 1)

    # For unlabeled data
    def _setupStepStep3_K_Means(self):
        self.Step3_K_Means = QtWidgets.QGroupBox(self.Step_by_step_survival)
        # self.Step3_K_Means.setSizePolicy(self._getsizePolicy_survival(self.Step3_K_Means, 'Preferred', 'Preferred'))
        self.Step3_K_Means.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Step3_K_Means.setFont(self.font_max_survival)
        self.Step3_K_Means.setObjectName("Step3_K_Means")
        self.Step3_K_Means.setTitle("Step 3 KMeans for data without label")
   
        self.Step3_K_Means.setStyleSheet(
            "QWidget#Step3_K_Means" + "{" + modleborder_style + modlepadding + "}" + modlefont_color)

        self.Step3_K_Means_label1 = QtWidgets.QLabel(self.Step3_K_Means)
        # self.Step3_K_Means_label1.setSizePolicy(self._getsizePolicy_survival(self.Step3_K_Means_label1, 'Fixed', 'Preferred'))
        self.Step3_K_Means_label1.setFont(self.font_min_survival)
        self.Step3_K_Means_label1.setObjectName("Step3_K_Means_label1")
        self.Step3_K_Means_label1.setText("K Value(User Set)")

        # k1 users set by themselves
        self.Step3_K_Means_K_Value1 = QtWidgets.QLineEdit(self.Step3_K_Means)
        self.Step3_K_Means_K_Value1.setFont(self.font_min_survival)
        self.Step3_K_Means_K_Value1.setObjectName("Step3_K_Means_K_Value1")
        self.Step3_K_Means_K_Value1.setText('3')
        self.Step3_K_Means_K_Value1.setDisabled(False)
        
        self.Step3_K_Means_K_Value1.setStyleSheet(modleborder_style)

        self.Step3_K_Means_ok1 = QtWidgets.QPushButton(self.Step3_K_Means)
        # Step3_K_Means_ok1.setSizePolicy(self._getsizePolicy_survival(self.Step3_K_Means_ok_survival, 'Fixed', 'Fixed'))
        self.Step3_K_Means_ok1.setFont(self.font_min_survival)
        self.Step3_K_Means_ok1.setObjectName("Step3_K_Means_ok1")
        self.Step3_K_Means_ok1.setText("OK")
       
        self.Step3_K_Means_ok1.setStyleSheet(background_color)

        # System setting k
        self.Step3_K_Means_label2 = QtWidgets.QLabel(self.Step3_K_Means)
        # self.Step3_K_Means_label2.setSizePolicy(self._getsizePolicy_survival(self.Step3_K_Means_label1, 'Fixed', 'Preferred'))
        self.Step3_K_Means_label2.setFont(self.font_min_survival)
        self.Step3_K_Means_label2.setObjectName("Step3_K_Means_label2")
        self.Step3_K_Means_label2.setText("K Value(System-Silhouette)")

        self.Step3_K_Means_K_Value2 = QtWidgets.QLineEdit(self.Step3_K_Means)
        self.Step3_K_Means_K_Value2.setFont(self.font_min_survival)
        self.Step3_K_Means_K_Value2.setObjectName("self.Step3_K_Means_K_Value2")
        self.Step3_K_Means_K_Value2.setText('Auto')
        self.Step3_K_Means_K_Value2.setDisabled(True)
       
        self.Step3_K_Means_K_Value2.setStyleSheet(modleborder_style)

        self.Step3_K_Means_ok2 = QtWidgets.QPushButton(self.Step3_K_Means)
        # Step3_K_Means_ok1.setSizePolicy(self._getsizePolicy_survival(self.Step3_K_Means_ok_survival, 'Fixed', 'Fixed'))
        self.Step3_K_Means_ok2.setFont(self.font_min_survival)
        self.Step3_K_Means_ok2.setObjectName("Step3_K_Means_ok2")
        self.Step3_K_Means_ok2.setText("OK")
       
        self.Step3_K_Means_ok2.setStyleSheet(background_color)

        self.gridLayout_1step3_k_means = QtWidgets.QGridLayout(self.Step3_K_Means)
        self.gridLayout_1step3_k_means.setObjectName("gridLayout_1step3")

        self.gridLayout_1step3_k_means.addWidget(self.Step3_K_Means_label1, 1, 0, 1, 1)
        self.gridLayout_1step3_k_means.addWidget(self.Step3_K_Means_K_Value1, 1, 1, 1, 1)
        self.gridLayout_1step3_k_means.addWidget(self.Step3_K_Means_ok1, 1, 3, 1, 1)

        self.gridLayout_1step3_k_means.addWidget(self.Step3_K_Means_label2, 2, 0, 1, 1)
        self.gridLayout_1step3_k_means.addWidget(self.Step3_K_Means_K_Value2, 2, 1, 1, 1)
        self.gridLayout_1step3_k_means.addWidget(self.Step3_K_Means_ok2, 2, 3, 1, 1)

    #For labeled data
    def _setupStepStep4_K_Means(self):
        self.Step4_K_Means = QtWidgets.QGroupBox(self.Step_by_step_survival)
        # self.Step3_K_Means.setSizePolicy(self._getsizePolicy_survival(self.Step3_K_Means, 'Preferred', 'Preferred'))
        self.Step4_K_Means.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Step4_K_Means.setFont(self.font_max_survival)
        self.Step4_K_Means.setObjectName("Step4_K_Means")
        self.Step4_K_Means.setTitle("Step 3 KMeans for data with label")
        
        self.Step4_K_Means.setStyleSheet(
            "QWidget#Step4_K_Means" + "{" + modleborder_style + modlepadding + "}" + modlefont_color)

        self.Step4_K_Means_label1 = QtWidgets.QLabel(self.Step4_K_Means)
        # self.Step3_K_Means_label1.setSizePolicy(self._getsizePolicy_survival(self.Step3_K_Means_label1, 'Fixed', 'Preferred'))
        self.Step4_K_Means_label1.setFont(self.font_min_survival)
        self.Step4_K_Means_label1.setObjectName("Step4_K_Means_label1")
        self.Step4_K_Means_label1.setText("K Value(User Set)")

        # k1 users set by themselves
        self.Step4_K_Means_K_Value1 = QtWidgets.QLineEdit(self.Step4_K_Means)
        self.Step4_K_Means_K_Value1.setFont(self.font_min_survival)
        self.Step4_K_Means_K_Value1.setObjectName("Step4_K_Means_K_Value1")
        self.Step4_K_Means_K_Value1.setText('3')
        self.Step4_K_Means_K_Value1.setDisabled(False)
        
        self.Step4_K_Means_K_Value1.setStyleSheet(modleborder_style)

        self.Step4_K_Means_ok1 = QtWidgets.QPushButton(self.Step4_K_Means)
        # Step3_K_Means_ok1.setSizePolicy(self._getsizePolicy_survival(self.Step3_K_Means_ok_survival, 'Fixed', 'Fixed'))
        self.Step4_K_Means_ok1.setFont(self.font_min_survival)
        self.Step4_K_Means_ok1.setObjectName("Step4_K_Means_ok1")
        self.Step4_K_Means_ok1.setText("OK")
        
        self.Step4_K_Means_ok1.setStyleSheet(background_color)

        # System setting k
        self.Step4_K_Means_label2 = QtWidgets.QLabel(self.Step4_K_Means)
        # self.Step3_K_Means_label2.setSizePolicy(self._getsizePolicy_survival(self.Step3_K_Means_label1, 'Fixed', 'Preferred'))
        self.Step4_K_Means_label2.setFont(self.font_min_survival)
        self.Step4_K_Means_label2.setObjectName("Step4_K_Means_label2")
        self.Step4_K_Means_label2.setText("K Value(System-AMI)")

        self.Step4_K_Means_K_Value2 = QtWidgets.QLineEdit(self.Step4_K_Means)
        self.Step4_K_Means_K_Value2.setFont(self.font_min_survival)
        self.Step4_K_Means_K_Value2.setObjectName("self.Step4_K_Means_K_Value2")
        self.Step4_K_Means_K_Value2.setText('Auto')
        self.Step4_K_Means_K_Value2.setDisabled(True)
       
        self.Step4_K_Means_K_Value2.setStyleSheet(modleborder_style)

        self.Step4_K_Means_ok2 = QtWidgets.QPushButton(self.Step4_K_Means)
        # Step3_K_Means_ok1.setSizePolicy(self._getsizePolicy_survival(self.Step3_K_Means_ok_survival, 'Fixed', 'Fixed'))
        self.Step4_K_Means_ok2.setFont(self.font_min_survival)
        self.Step4_K_Means_ok2.setObjectName("Step4_K_Means_ok2")
        self.Step4_K_Means_ok2.setText("OK")
       
        self.Step4_K_Means_ok2.setStyleSheet(background_color)

        self.gridLayout_1step4_k_means = QtWidgets.QGridLayout(self.Step4_K_Means)
        self.gridLayout_1step4_k_means.setObjectName("gridLayout_1step4")

        self.gridLayout_1step4_k_means.addWidget(self.Step4_K_Means_label1, 1, 0, 1, 1)
        self.gridLayout_1step4_k_means.addWidget(self.Step4_K_Means_K_Value1, 1, 1, 1, 1)
        self.gridLayout_1step4_k_means.addWidget(self.Step4_K_Means_ok1, 1, 3, 1, 1)

        self.gridLayout_1step4_k_means.addWidget(self.Step4_K_Means_label2, 2, 0, 1, 1)
        self.gridLayout_1step4_k_means.addWidget(self.Step4_K_Means_K_Value2, 2, 1, 1, 1)
        self.gridLayout_1step4_k_means.addWidget(self.Step4_K_Means_ok2, 2, 3, 1, 1)

        # self.gridLayout_1step3_k_means.setColumnStretch(0, 1)

    def _setupEdit_survival(self):

        self.Edit_survival = QtWidgets.QGroupBox(self.Step_by_step_survival)
        self.Edit_survival.setSizePolicy(self._getsizePolicy_survival(self.Edit_survival, 'Preferred', 'Preferred'))
        self.Edit_survival.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Edit_survival.setFont(self.font_max_survival)
        self.Edit_survival.setObjectName("Edit_survival")
        self.Edit_survival.setTitle("Edit")
        
        self.Edit_survival.setStyleSheet( "QWidget#Edit_survival" + "{" + modleborder_style + modlepadding + "}" + modlefont_color)

        self.Clear_all_survival = QtWidgets.QPushButton(self.Edit_survival)
        self.Clear_all_survival.setFont(self.font_min_survival)
        self.Clear_all_survival.setObjectName("Clear_all_survival")
        self.Clear_all_survival.setText("Clear all")
        
        self.Clear_all_survival.setStyleSheet(background_color)

        self.gridLayout_1Edit_survival = QtWidgets.QGridLayout(self.Edit_survival)
        self.gridLayout_1Edit_survival.addWidget(self.Clear_all_survival, 0, 1, 1, 1)
        self.gridLayout_1Edit_survival.setContentsMargins(3,13,3,1)



    # The final result is displayed
    def _setupResult_survival(self):
        self.Result_survival = QtWidgets.QGroupBox(self.Step_by_step_survival)
        self.Result_survival.setSizePolicy(self._getsizePolicy_survival(self.Result_survival, 'Preferred', 'Preferred'))
        self.Result_survival.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Result_survival.setFont(self.font_max_survival)
        self.Result_survival.setObjectName("Result")
        self.Result_survival.setTitle("Result")
        
        self.Result_survival.setStyleSheet("border:1px solid #4F4F4F ; padding : 5ex ; color : white ")

        self.Result_text_survival = QtWidgets.QTextBrowser(self.Result_survival)
        self.Result_text_survival.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Result_text_survival.setObjectName("Result_text")
        self.Result_text_survival.setFont(self.font_result_survival)

        self.gridLayout_result_survival = QtWidgets.QGridLayout(self.Result_survival)
        self.gridLayout_result_survival.setObjectName("gridLayout_result")
        self.gridLayout_result_survival.addWidget(self.Result_text_survival, 0, 1, 2, 1)

    # =====================================
        # ================================== #
    # Design and call of the entire interface
    def setupStep_by_step_K_Means(self):
        self.Step_by_step_survival = QtWidgets.QWidget()
        self.Step_by_step_survival.setObjectName("Step_by_step")

        self.Step_by_step_survival.setStyleSheet(MainWindow_background_color)

        ## Step1_load_data box
        self._setupStep1_load_data_survival()

        ## Step2_preprocessing box
        self._setupStep2_preprocessing_survival()

        ## Step3_K_Means
        self._setupStepStep3_K_Means()

        ## Step4_k_Means
        self._setupStepStep4_K_Means()


        ## Clear
        self._setupEdit_survival()

        ## result box
        self._setupResult_survival()

        self.gridLayout_stepbystep_survival = QtWidgets.QGridLayout(self.Step_by_step_survival)
        self.gridLayout_stepbystep_survival.setObjectName("gridLayout_stepbystep_survival")
        self.gridLayout_stepbystep_survival.addWidget(self.Step1_load_data_survival, 0, 0, 1, 1)
        self.gridLayout_stepbystep_survival.addWidget(self.Step2_preprocessing_survival, 1, 0, 1, 1)
        self.gridLayout_stepbystep_survival.addWidget(self.Step3_K_Means, 2, 0, 1, 1)
        self.gridLayout_stepbystep_survival.addWidget(self.Step4_K_Means, 3, 0, 1, 1)
        self.gridLayout_stepbystep_survival.addWidget(self.Edit_survival, 4, 0, 1, 1)
        self.gridLayout_stepbystep_survival.addWidget(self.Result_survival, 0, 1, 4, 1)

        self.gridLayout_stepbystep_survival.setColumnStretch(0, 5)
        self.gridLayout_stepbystep_survival.setColumnStretch(1, 5)
        self.gridLayout_stepbystep_survival.setRowStretch(0, 2)
        self.gridLayout_stepbystep_survival.setRowStretch(1, 2)
        self.gridLayout_stepbystep_survival.setRowStretch(2, 2)
        self.gridLayout_stepbystep_survival.setRowStretch(3, 2)
        self.gridLayout_stepbystep_survival.setRowStretch(4, 1)
        self.gridLayout_stepbystep_survival.setContentsMargins(3, 8, 3, 1)

        ### connect to the functions
        # =================================================================== #

        # ==============================================================================
        #         sys.stdout = Step_by_Step_Thread_Survival.port(self.Result_text)
        # ==============================================================================
        self.Step1_data_path_ok_survival.clicked.connect(self.Select_a_path)
        # self.Step1_seed_ok_survival.clicked.connect(self.Set_a_seed)
        # self.Step1_seperate_ok_survival.clicked.connect(self.Seperate_a_data)
        self.Step2_inpute_ok_survival.clicked.connect(self.Input_data)
        self.Step2_standardize_ok_survival.clicked.connect(self.Standarize_data)

        self.Step3_K_Means_ok1.clicked.connect(self.K_Means_K1)
        self.Step3_K_Means_ok2.clicked.connect(self.K_Means_K2)

        self.Step4_K_Means_ok1.clicked.connect(self.K_Means_K1)
        self.Step4_K_Means_ok2.clicked.connect(self.K_Means_K3)

        self.Clear_all_survival.clicked.connect(self.Clear_operation)

        return self.Step_by_step_survival

