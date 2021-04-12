'''
The UI interface of the StepByStep tab page
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter,QPalette,QColor
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
import sys
import Step_by_Step_Thread_Survival
font_color="color:white;"
background_color="background-color:#37474F"
MainWindow_background_color="background-color:#363636"
border_style="border:1px solid gray;"
modleborder_style = "border:1px solid #4F4F4F;"
modlepadding = "padding:5ex;"
modlefont_color = "QWidget{ color:white }"
class StepByStep_Survival(QtWidgets.QMainWindow, Step_by_Step_Thread_Survival.Step_by_step_survival):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Step_by_Step_Thread_Survival.Step_by_step_survival.__init__(self)
        # Define large font
        self.font_max_survival = QtGui.QFont()
        self.font_max_survival.setPointSize(12)
        self.font_max_survival.setBold(True)
        self.font_max_survival.setWeight(75)
        # Define small font
        self.font_min_survival = QtGui.QFont()
        self.font_min_survival.setPointSize(10)
        self.font_min_survival.setBold(False)
        self.font_min_survival.setWeight(50)
        # Define the output font
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
        
        self.Step1_load_data_survival.setStyleSheet( "QWidget#Step1_load_data" + "{" + modleborder_style + modlepadding + "}" + modlefont_color)
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
        # ===============Step1_seed_label "seed"label
        self.Step1_seed_label_survival = QtWidgets.QLabel(self.Step1_load_data_survival)
        # self.Step1_seed_label_survival.setSizePolicy(self._getsizePolicy_survival(self.Step1_seed_label_survival, 'Fixed', 'Preferred'))
        self.Step1_seed_label_survival.setFont(self.font_min_survival)
        self.Step1_seed_label_survival.setObjectName("Step1_seed_label")
        self.Step1_seed_label_survival.setText("Seed")
        # ===============Step1_seed LineEdit_survival
        self.Step1_seed_survival = QtWidgets.QLineEdit(self.Step1_load_data_survival)
        self.Step1_seed_survival.setObjectName("Step1_seed")
        self.Step1_seed_survival.setFont(self.font_min_survival)
        
        self.Step1_seed_survival.setStyleSheet(modleborder_style)
        # ===============Step1_seed_ok 'OK'
        self.Step1_seed_ok_survival = QtWidgets.QPushButton(self.Step1_load_data_survival)
        # self.Step1_seed_ok_survival.setSizePolicy(self._getsizePolicy_survival(self.Step1_seed_ok_survival, 'Fixed', 'Fixed'))
        self.Step1_seed_ok_survival.setFont(self.font_min_survival)
        self.Step1_seed_ok_survival.setMouseTracking(False)
        self.Step1_seed_ok_survival.setObjectName("Step1_seed_ok")
        self.Step1_seed_ok_survival.setText("OK")
        
        self.Step1_seed_ok_survival.setStyleSheet(background_color)
        # ===============Step1_seperate_label 'seperate'
        self.Step1_seperate_label_survival = QtWidgets.QLabel(self.Step1_load_data_survival)
        self.Step1_seperate_label_survival.setFont(self.font_min_survival)
        self.Step1_seperate_label_survival.setMouseTracking(True)
        self.Step1_seperate_label_survival.setObjectName("Step1_seperate_label")
        self.Step1_seperate_label_survival.setText("Sepearte")
        # ===============Step1_seperate '
        self.Step1_seperate_survival = QtWidgets.QDoubleSpinBox(self.Step1_load_data_survival)
        self.Step1_seperate_survival.setFont(self.font_min_survival)
        self.Step1_seperate_survival.setMaximum(1.0)
        self.Step1_seperate_survival.setSingleStep(0.05)
        self.Step1_seperate_survival.setValue(0.7)
        self.Step1_seperate_survival.setObjectName("Step1_seperate")
        
        self.Step1_seperate_survival.setStyleSheet(background_color)
        # ===============Step1_seperate_ok 'ok'
        self.Step1_seperate_ok_survival = QtWidgets.QPushButton(self.Step1_load_data_survival)
        # self.Step1_seperate_ok_survival.setSizePolicy(self._getsizePolicy_survival(self.Step1_seperate_ok_survival, 'Fixed', 'Fixed'))
        self.Step1_seperate_ok_survival.setFont(self.font_min_survival)
        self.Step1_seperate_ok_survival.setMouseTracking(False)
        self.Step1_seperate_ok_survival.setObjectName("Step1_seperate_ok")
        self.Step1_seperate_ok_survival.setText("OK")
       
        self.Step1_seperate_ok_survival.setStyleSheet(background_color)
        self.gridLayout_1step1_survival = QtWidgets.QGridLayout(self.Step1_load_data_survival)
        self.gridLayout_1step1_survival.setObjectName("gridLayout_1step1")
        self.gridLayout_1step1_survival.addWidget(self.Step1_data_path_label_survival, 0, 0, 1, 1)
        self.gridLayout_1step1_survival.addWidget(self.Step1_data_path_survival, 0, 1, 1, 5)
        self.gridLayout_1step1_survival.addWidget(self.Step1_data_path_ok_survival, 0, 5, 1, 1)
        self.gridLayout_1step1_survival.addWidget(self.Step1_seed_label_survival, 2, 0, 1, 1)
        self.gridLayout_1step1_survival.addWidget(self.Step1_seed_survival, 2, 1, 1, 1)
        self.gridLayout_1step1_survival.addWidget(self.Step1_seed_ok_survival, 2, 2, 1, 1)
        self.gridLayout_1step1_survival.addWidget(self.Step1_seperate_label_survival, 2, 3, 1, 1)
        self.gridLayout_1step1_survival.addWidget(self.Step1_seperate_survival, 2, 4, 1, 1)
        self.gridLayout_1step1_survival.addWidget(self.Step1_seperate_ok_survival, 2, 5, 1, 1)
        # self.gridLayout_1step1_survival.setColumnStretch(0, 1)
    def _setupStep2_preprocessing_survival(self):
        self.Step2_preprocessing_survival = QtWidgets.QGroupBox(self.Step_by_step_survival)
        self.Step2_preprocessing_survival.setSizePolicy(self._getsizePolicy_survival(self.Step2_preprocessing_survival, 'Preferred', 'Preferred'))
        self.Step2_preprocessing_survival.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Step2_preprocessing_survival.setFont(self.font_max_survival)
        self.Step2_preprocessing_survival.setObjectName("Step2_preprocessing")
        self.Step2_preprocessing_survival.setTitle("Step 2 preprocessing")
        
        self.Step2_preprocessing_survival.setStyleSheet("QWidget#Step2_preprocessing" + "{" + modleborder_style + modlepadding + "}" + modlefont_color)
        self.Step2_inpute_label_survival = QtWidgets.QLabel(self.Step2_preprocessing_survival)
        self.Step2_inpute_label_survival.setSizePolicy(self._getsizePolicy_survival(self.Step2_inpute_label_survival, 'Fixed', 'Preferred'))
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
        self.Step2_inpute_is_abnormal_nan_survival.setSizePolicy(self._getsizePolicy_survival(self.Step2_inpute_is_abnormal_nan_survival, 'Fixed', 'Fixed'))
        self.Step2_inpute_is_abnormal_nan_survival.setFont(self.font_min_survival)
        self.Step2_inpute_is_abnormal_nan_survival.setObjectName("Step2_inpute_is_abnormal_nan")
        self.Step2_inpute_is_abnormal_nan_survival.setText("Outliers")
        self.Step2_inpute_is_abnormal_nan_survival.setChecked(False)
        self.Step2_inpute_ok_survival = QtWidgets.QPushButton(self.Step2_preprocessing_survival)
        self.Step2_inpute_ok_survival.setSizePolicy(self._getsizePolicy_survival(self.Step2_inpute_ok_survival, 'Fixed', 'Fixed'))
        self.Step2_inpute_ok_survival.setFont(self.font_min_survival)
        self.Step2_inpute_ok_survival.setObjectName("Step2_inpute_ok")
        self.Step2_inpute_ok_survival.setText("OK")
        
        self.Step2_inpute_ok_survival.setStyleSheet(background_color)
        self.Step2_standardize_label_survival = QtWidgets.QLabel(self.Step2_preprocessing_survival)
        self.Step2_standardize_label_survival.setSizePolicy(self._getsizePolicy_survival(self.Step2_standardize_label_survival, 'Fixed', 'Preferred'))
        self.Step2_standardize_label_survival.setFont(self.font_min_survival)
        self.Step2_standardize_label_survival.setObjectName("Step2_standardize_label")
        self.Step2_standardize_label_survival.setText("Standardize")
        self.Step2_standardize_survival = QtWidgets.QComboBox(self.Step2_preprocessing_survival)
        self.Step2_standardize_survival.setFont(self.font_min_survival)
        self.Step2_standardize_survival.setObjectName("Step2_standardize")
        self.Step2_standardize_survival.addItems(['Standardization', 'MinMaxScaler'])
       
        self.Step2_standardize_survival.setStyleSheet(background_color)
        self.Step2_standardize_ok_survival = QtWidgets.QPushButton(self.Step2_preprocessing_survival)
        self.Step2_standardize_ok_survival.setSizePolicy(self._getsizePolicy_survival(self.Step2_standardize_ok_survival, 'Fixed', 'Fixed'))
        self.Step2_standardize_ok_survival.setFont(self.font_min_survival)
        self.Step2_standardize_ok_survival.setObjectName("Step2_standardize_ok")
        self.Step2_standardize_ok_survival.setText("OK")
        
        self.Step2_standardize_ok_survival.setStyleSheet(background_color)
        self.gridLayout_1step2_survival = QtWidgets.QGridLayout(self.Step2_preprocessing_survival)
        self.gridLayout_1step2_survival.setObjectName("gridLayout_1step2")
        self.gridLayout_1step2_survival.addWidget(self.Step2_standardize_label_survival, 1, 0, 1, 1)
        self.gridLayout_1step2_survival.addWidget(self.Step2_standardize_survival, 1, 1, 1, 1)
        self.gridLayout_1step2_survival.addWidget(self.Step2_standardize_ok_survival, 1, 3, 1, 1)
        self.gridLayout_1step2_survival.addWidget(self.Step2_inpute_label_survival, 0, 0, 1, 1)
        self.gridLayout_1step2_survival.addWidget(self.Step2_inpute_survival, 0, 1, 1, 1)
        self.gridLayout_1step2_survival.addWidget(self.Step2_inpute_is_abnormal_nan_survival, 0, 2, 1, 1)
        self.gridLayout_1step2_survival.addWidget(self.Step2_inpute_ok_survival, 0, 3, 1, 1)
        self.gridLayout_1step2_survival.setColumnStretch(0, 1)
    # regin Step3 Factors combox change
    # Single factor analysis box
    def Step3_Univariate_survival(self):
        self.Step3_Univariate_frame_survival = QtWidgets.QFrame(self.Step3_feature_selection_survival)
        self.Step3_Univariate_frame_survival.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Step3_Univariate_frame_survival.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Step3_Univariate_frame_survival.setObjectName("Step3_Univariate_frame")
        # ===============Step3_method_label 'Method'Label
        self.Step3_Univariate_method_label_survival = QtWidgets.QLabel(self.Step3_Univariate_frame_survival)
        self.Step3_Univariate_method_label_survival.setSizePolicy(self._getsizePolicy_survival(self.Step3_Univariate_method_label_survival, 'Fixed', 'Preferred'))
        self.Step3_Univariate_method_label_survival.setFont(self.font_min_survival)
        self.Step3_Univariate_method_label_survival.setObjectName("Step3_Univariate_method_label")
        self.Step3_Univariate_method_label_survival.setText('Method      ')
        # ===============Step3_method ComboBox
        self.Step3_Univariate_method_survival = QtWidgets.QComboBox(self.Step3_Univariate_frame_survival)
        self.Step3_Univariate_method_survival.setSizePolicy(self._getsizePolicy_survival(self.Step3_Univariate_method_survival, 'Preferred', 'Fixed'))
        self.Step3_Univariate_method_survival.setFont(self.font_min_survival)
        self.Step3_Univariate_method_survival.setObjectName("Step3_Univariate_method")
        self.Step3_Univariate_method_survival.addItems(['Correlation_xx', 'Univariate_Cox', "Logrank_test"])
        self.Step3_Univariate_method_survival.setCurrentIndex(0)
        self.Step3_Univariate_method_survival.currentIndexChanged.connect(self.Step3_Univariate_comboxchange_survival)
       
        self.Step3_Univariate_method_survival.setStyleSheet(background_color)
        # ===============Step3_method_ok Button
        self.Step3_Univariate_method_ok_survival = QtWidgets.QPushButton(self.Step3_Univariate_frame_survival)
        self.Step3_Univariate_method_ok_survival.setSizePolicy(self._getsizePolicy_survival(self.Step3_Univariate_method_ok_survival, 'Fixed', 'Fixed'))
        self.Step3_Univariate_method_ok_survival.setFont(self.font_min_survival)
        self.Step3_Univariate_method_ok_survival.setObjectName("Step3_Univariate_method_ok")
        self.Step3_Univariate_method_ok_survival.setText('OK')
        
        self.Step3_Univariate_method_ok_survival.setStyleSheet(background_color)
        self.Step3_Univariate_method_ok_survival.clicked.connect(self.Select_feature1)
        self.Step3_Univariate_Temp_frame_survival = self.Step3_Univariate_Correlation_survival()
        # ===============gridLayout_1step3_survival in Step3_feature_selection BOX
        self.Step3_Univariate_gridLayout_survival = QtWidgets.QGridLayout(self.Step3_Univariate_frame_survival)
        self.Step3_Univariate_gridLayout_survival.setObjectName("Step3_Univariate_gridLayout")
        # self.Step3_Factors_MultiVariate_gridLayout.addWidget(self.Step3_Factors_label_survival, 0, 0, 1, 1)
        # self.Step3_Factors_MultiVariate_gridLayout.addWidget(self.Step3_Factors_survival, 0, 1, 1, 2)
        self.Step3_Univariate_gridLayout_survival.addWidget(self.Step3_Univariate_method_label_survival, 0, 0, 1, 1)
        self.Step3_Univariate_gridLayout_survival.addWidget(self.Step3_Univariate_method_survival, 0, 1, 1, 2)
        self.Step3_Univariate_gridLayout_survival.addWidget(self.Step3_Univariate_method_ok_survival, 0, 3, 1, 1)
        # self.gridLayout_1step3_survival.addWidget(self.N_of_factor, 2, 1, 1, 1)
        # self.gridLayout_1step3_survival.addWidget(self.N_of_factor_label, 2, 0, 1, 1)
        self.Step3_Univariate_gridLayout_survival.addWidget(self.Step3_Univariate_Temp_frame_survival, 1, 0, 1, 4)
        self.Step3_Univariate_gridLayout_survival.setContentsMargins(3,3,3,1)
        return self.Step3_Univariate_frame_survival
    # Multi-factor analysis box
    def Step3_MultiVariate_survival(self):
        self.Step3_MultiVariate_frame_survival = QtWidgets.QFrame(self.Step3_feature_selection_survival)
        self.Step3_MultiVariate_frame_survival.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Step3_MultiVariate_frame_survival.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Step3_MultiVariate_frame_survival.setObjectName("Step3_MultiVariate_frame")
        # ===============Step3_method_label 'Method'Label
        self.Step3_MultiVariate_method_label_survival = QtWidgets.QLabel(self.Step3_MultiVariate_frame_survival)
        self.Step3_MultiVariate_method_label_survival.setSizePolicy(self._getsizePolicy_survival(self.Step3_MultiVariate_method_label_survival, 'Fixed', 'Preferred'))
        self.Step3_MultiVariate_method_label_survival.setFont(self.font_min_survival)
        self.Step3_MultiVariate_method_label_survival.setObjectName("Step3_MultiVariate_method_label")
        self.Step3_MultiVariate_method_label_survival.setText('Method      ')
        # ===============Step3_method ComboBox
        self.Step3_MultiVariate_method_survival = QtWidgets.QComboBox(self.Step3_MultiVariate_frame_survival)
        self.Step3_MultiVariate_method_survival.setFont(self.font_min_survival)
        self.Step3_MultiVariate_method_survival.setObjectName("Step3_method")
        self.Step3_MultiVariate_method_survival.addItems(['MultiVariate_Cox', 'L1'])
        self.Step3_MultiVariate_method_survival.setCurrentIndex(0)
        self.Step3_MultiVariate_method_survival.currentIndexChanged.connect(self.Step3_MultiVariate_comboxchange_survival)
        self.Step3_MultiVariate_Temp_frame_survival = self.Step3_MultiVariate_Cox_survival()
        
        self.Step3_MultiVariate_method_survival.setStyleSheet(background_color)
        # ===============Step3_method_ok Button
        self.Step3_MultiVariate_method_ok_survival = QtWidgets.QPushButton(self.Step3_MultiVariate_frame_survival)
        self.Step3_MultiVariate_method_ok_survival.setSizePolicy(self._getsizePolicy_survival(self.Step3_MultiVariate_method_ok_survival, 'Fixed', 'Fixed'))
        self.Step3_MultiVariate_method_ok_survival.setFont(self.font_min_survival)
        self.Step3_MultiVariate_method_ok_survival.setObjectName("Step3_MultiVariate_method_ok")
        self.Step3_MultiVariate_method_ok_survival.setText('OK')
        
        self.Step3_MultiVariate_method_ok_survival.setStyleSheet(background_color)
        self.Step3_MultiVariate_method_ok_survival.clicked.connect(self.Select_feature2)
        # ===============gridLayout_1step3_survival in Step3_feature_selection BOX
        self.Step3_MultiVariate_gridLayout_survival = QtWidgets.QGridLayout(self.Step3_MultiVariate_frame_survival)
        self.Step3_MultiVariate_gridLayout_survival.setObjectName("Step3_MultiVariate_gridLayout_survival")
        #self.Step3_Factors_MultiVariate_gridLayout.addWidget(self.Step3_Factors_label_survival, 0, 0, 1, 1)
        #self.Step3_Factors_MultiVariate_gridLayout.addWidget(self.Step3_Factors_survival, 0, 1, 1, 2)
        self.Step3_MultiVariate_gridLayout_survival.addWidget(self.Step3_MultiVariate_method_label_survival, 0, 0, 1, 1)
        self.Step3_MultiVariate_gridLayout_survival.addWidget(self.Step3_MultiVariate_method_survival, 0, 1, 1, 2)
        self.Step3_MultiVariate_gridLayout_survival.addWidget(self.Step3_MultiVariate_method_ok_survival, 0, 3, 1, 1)
        # self.gridLayout_1step3_survival.addWidget(self.N_of_factor, 2, 1, 1, 1)
        # self.gridLayout_1step3_survival.addWidget(self.N_of_factor_label, 2, 0, 1, 1)
        self.Step3_MultiVariate_gridLayout_survival.addWidget(self.Step3_MultiVariate_Temp_frame_survival, 1, 0, 1, 4)
        self.Step3_MultiVariate_gridLayout_survival.setContentsMargins(3,3,3,1)
        return self.Step3_MultiVariate_frame_survival
    def Step3_Factors_comboxchange_survival(self, index):
        if index == 1:  # MultiVariate
            self.Step3_Factors_Temp_frame_survival.close()
            self.Step3_Univariate_Temp_frame_survival.close()
            self.Step3_Factors_Temp_frame_survival = self.Step3_MultiVariate_survival()
            self.gridLayout_1step3_survival.addWidget(self.Step3_Factors_Temp_frame_survival, 1, 0, 1, 4)
        if index == 0:  # Univariate_analysis
            self.Step3_Factors_Temp_frame_survival.close()
            self.Step3_MultiVariate_Temp_frame_survival.close()
            self.Step3_Factors_Temp_frame_survival = self.Step3_Univariate_survival()
            self.gridLayout_1step3_survival.addWidget(self.Step3_Factors_Temp_frame_survival, 1, 0, 1, 4)
    
    def Step3_Univariate_Correlation_survival(self):
        self.Step3_Univariate_Correlation_frame_survival = QtWidgets.QFrame(self.Step3_feature_selection_survival)
        self.Step3_Univariate_Correlation_frame_survival.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Step3_Univariate_Correlation_frame_survival.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Step3_Univariate_Correlation_frame_survival.setObjectName("Step3_Univariate_Correlation_frame_survival")
        self.Step3_Univariate_Correlation_corr_label_survival = QtWidgets.QLabel(self.Step3_Univariate_Correlation_frame_survival)
        # n_neighbors_label.setSizePolicy(self._getsizePolicy_survival(n_neighbors_label, 'Fixed', 'Preferred'))
        self.Step3_Univariate_Correlation_corr_label_survival.setFont(self.font_min_survival)
        self.Step3_Univariate_Correlation_corr_label_survival.setObjectName("Step3_Univariate_Correlation_corr_label_survival")
        self.Step3_Univariate_Correlation_corr_label_survival.setText("corr")
        self.Step3_Univariate_Correlation_corr_survival = QtWidgets.QLineEdit(self.Step3_Univariate_Correlation_frame_survival)
        self.Step3_Univariate_Correlation_corr_survival.setFont(self.font_min_survival)
        self.Step3_Univariate_Correlation_corr_survival.setObjectName("Step3_Univariate_Correlation_corr_survival")
        self.Step3_Univariate_Correlation_corr_survival.setText('0.7')
        
        self.Step3_Univariate_Correlation_corr_survival.setStyleSheet(modleborder_style)
        self.Step3_Univariate_Correlation_gridLayout_survival = QtWidgets.QGridLayout(self.Step3_Univariate_Correlation_frame_survival)
        self.Step3_Univariate_Correlation_gridLayout_survival.setObjectName("Step3_Univariate_Correlation_gridLayout_survival")
        self.Step3_Univariate_Correlation_gridLayout_survival.addWidget(self.Step3_Univariate_Correlation_corr_label_survival, 0, 0, 1, 1)
        self.Step3_Univariate_Correlation_gridLayout_survival.addWidget(self.Step3_Univariate_Correlation_corr_survival, 0, 1, 1, 1)
        self.Step3_Univariate_Correlation_gridLayout_survival.setColumnStretch(0, 3)
        self.Step3_Univariate_Correlation_gridLayout_survival.setColumnStretch(1, 7)
        self.Step3_Univariate_Correlation_gridLayout_survival.setColumnStretch(2, 3)
        self.Step3_Univariate_Correlation_gridLayout_survival.setColumnStretch(3, 7)
        self.Step3_Univariate_Correlation_gridLayout_survival.setContentsMargins(3,3,3,1)
        return self.Step3_Univariate_Correlation_frame_survival
    def Step3_Univariate_Cox_Logrank_survival(self):  ##Logistic regression univariate analysis
        self.Step3_Univariate_Logistic_frame_survival = QtWidgets.QFrame(self.Step3_feature_selection_survival)
        self.Step3_Univariate_Logistic_frame_survival.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Step3_Univariate_Logistic_frame_survival.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Step3_Univariate_Logistic_frame_survival.setObjectName("Step3_Univariate_Logistic_frame_survival")
        self.Step3_Univariate_Logistic_P_in_label_survival = QtWidgets.QLabel(self.Step3_Univariate_Logistic_frame_survival)
        # n_neighbors_label.setSizePolicy(self._getsizePolicy_survival(n_neighbors_label, 'Fixed', 'Preferred'))
        self.Step3_Univariate_Logistic_P_in_label_survival.setFont(self.font_min_survival)
        self.Step3_Univariate_Logistic_P_in_label_survival.setObjectName("Step3_Univariate_Logistic_P_in_label_survival")
        self.Step3_Univariate_Logistic_P_in_label_survival.setText("P_in")
        self.Step3_Univariate_Logistic_P_in_survival = QtWidgets.QLineEdit(self.Step3_Univariate_Logistic_frame_survival)
        self.Step3_Univariate_Logistic_P_in_survival.setFont(self.font_min_survival)
        self.Step3_Univariate_Logistic_P_in_survival.setObjectName("Step3_Univariate_Logistic_P_in_survival")
        self.Step3_Univariate_Logistic_P_in_survival.setText('0.05')
        self.Step3_Univariate_Logistic_P_in_survival.setDisabled(True)
        
        self.Step3_Univariate_Logistic_P_in_survival.setStyleSheet(modleborder_style)
        self.Step3_Univariate_Logistic_gridLayout_survival = QtWidgets.QGridLayout(self.Step3_Univariate_Logistic_frame_survival)
        self.Step3_Univariate_Logistic_gridLayout_survival.setObjectName("Step3_Univariate_Logistic_gridLayout_survival")
        self.Step3_Univariate_Logistic_gridLayout_survival.addWidget(self.Step3_Univariate_Logistic_P_in_label_survival, 0, 0, 1, 1)
        self.Step3_Univariate_Logistic_gridLayout_survival.addWidget(self.Step3_Univariate_Logistic_P_in_survival, 0, 1, 1, 1)
        self.Step3_Univariate_Logistic_gridLayout_survival.setColumnStretch(0, 3)
        self.Step3_Univariate_Logistic_gridLayout_survival.setColumnStretch(1, 7)
        self.Step3_Univariate_Logistic_gridLayout_survival.setColumnStretch(2, 3)
        self.Step3_Univariate_Logistic_gridLayout_survival.setColumnStretch(3, 7)
        self.Step3_Univariate_Logistic_gridLayout_survival.setContentsMargins(3,3,3,1)
        return self.Step3_Univariate_Logistic_frame_survival
    def Step3_Univariate_comboxchange_survival(self, index):
        if index == 0: # Correlation-xx
            self.Step3_Univariate_Temp_frame_survival.close()
            self.Step3_Univariate_Temp_frame_survival = self.Step3_Univariate_Correlation_survival()
            self.gridLayout_1step3_survival.addWidget(self.Step3_Univariate_Temp_frame_survival, 2, 0, 1, 4)
        if index == 1:  # Univariate_Cox
            self.Step3_Univariate_Temp_frame_survival.close()
            self.Step3_Univariate_Temp_frame_survival = self.Step3_Univariate_Cox_Logrank_survival()
            self.gridLayout_1step3_survival.addWidget(self.Step3_Univariate_Temp_frame_survival, 2, 0, 1, 4)
        if index == 2:
            self.Step3_Univariate_Temp_frame_survival.close()
            self.Step3_Univariate_Temp_frame_survival = self.Step3_Univariate_Cox_Logrank_survival()
            self.gridLayout_1step3_survival.addWidget(self.Step3_Univariate_Temp_frame_survival, 2, 0, 1, 4)
    # region Step3 Factors_MultiVariate_method combox change 
    def Step3_MultiVariate_Cox_survival(self):
        self.Step3_MultiVariate_Logistic_frame_survival = QtWidgets.QFrame(self.Step3_feature_selection_survival)
        self.Step3_MultiVariate_Logistic_frame_survival.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Step3_MultiVariate_Logistic_frame_survival.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Step3_MultiVariate_Logistic_frame_survival.setObjectName("Step3_MultiVariate_Logistic_frame_survival")
        self.Step3_MultiVariate_Logistic_Result_label_survival = QtWidgets.QLabel(self.Step3_MultiVariate_Logistic_frame_survival)
        #self.logistic_type_label.setSizePolicy(self._getsizePolicy_survival(self.logistic_type_label, 'Fixed', 'Preferred'))
        self.Step3_MultiVariate_Logistic_Result_label_survival.setFont(self.font_min_survival)
        self.Step3_MultiVariate_Logistic_Result_label_survival.setObjectName("Step3_MultiVariate_Logistic_Result_label_survival")
        self.Step3_MultiVariate_Logistic_Result_label_survival.setText("Logistic_Result")
        self.Step3_MultiVariate_Logistic_Result_survival = QtWidgets.QComboBox(self.Step3_MultiVariate_Logistic_frame_survival)
        self.Step3_MultiVariate_Logistic_Result_survival.setFont(self.font_min_survival)
        self.Step3_MultiVariate_Logistic_Result_survival.setObjectName("Step3_MultiVariate_Logistic_Result_survival")
        self.Step3_MultiVariate_Logistic_Result_survival.addItems(['Features', 'Radscore'])
        self.Step3_MultiVariate_Logistic_Result_survival.setCurrentIndex(0)
        self.Step3_MultiVariate_Logistic_Result_survival.currentIndexChanged.connect(self.Step3_MultiVariate_Logistic_comboxchange_survival)
       
        self.Step3_MultiVariate_Logistic_Result_survival.setStyleSheet(background_color)
        ### -----Control window switching
        self.Step3_Logistic_Temp_frame_survival = self.Step3_MultiVariate_Cox_Features_survival()
        self.Step3_MultiVariate_Logistic_gridLayout_survival = QtWidgets.QGridLayout(self.Step3_MultiVariate_Logistic_frame_survival)
        self.Step3_MultiVariate_Logistic_gridLayout_survival.setObjectName("Step3_MultiVariate_Logistic_gridLayout_survival")
        self.Step3_MultiVariate_Logistic_gridLayout_survival.addWidget(self.Step3_MultiVariate_Logistic_Result_label_survival, 0, 0, 1, 1)
        self.Step3_MultiVariate_Logistic_gridLayout_survival.addWidget(self.Step3_MultiVariate_Logistic_Result_survival, 0, 1, 1, 1)
        self.Step3_MultiVariate_Logistic_gridLayout_survival.addWidget(self.Step3_Logistic_Temp_frame_survival, 0, 2, 1, 1)
        self.Step3_MultiVariate_Logistic_gridLayout_survival.setColumnStretch(0, 3)
        self.Step3_MultiVariate_Logistic_gridLayout_survival.setColumnStretch(1, 7)
        self.Step3_MultiVariate_Logistic_gridLayout_survival.setColumnStretch(2, 3)
        self.Step3_MultiVariate_Logistic_gridLayout_survival.setColumnStretch(3, 7)
        self.Step3_MultiVariate_Logistic_gridLayout_survival.setContentsMargins(3,3,3,1)
        return self.Step3_MultiVariate_Logistic_frame_survival
    def Step3_MultiVariate_comboxchange_survival(self, index):
        if index == 0:  # Logistic
            self.Step3_MultiVariate_Temp_frame_survival.close()
            self.Step3_MultiVariate_Temp_frame_survival = self.Step3_MultiVariate_Cox_survival()
            self.gridLayout_1step3_survival.addWidget(self.Step3_MultiVariate_Temp_frame_survival, 2, 0, 1, 4)
        if index == 1:  # L1
            self.Step3_MultiVariate_Temp_frame_survival.close()
    # region Step3 method Logistic result combox change  
    def Step3_MultiVariate_Cox_Features_survival(self):
        self.Step3_MultiVariate_Logistic_Features_frame_survival = QtWidgets.QFrame(self.Step3_feature_selection_survival)
        self.Step3_MultiVariate_Logistic_Features_frame_survival.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Step3_MultiVariate_Logistic_Features_frame_survival.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Step3_MultiVariate_Logistic_Features_frame_survival.setObjectName("Step3_MultiVariate_Logistic_Features_frame_survival")
        self.Step3_MultiVariate_Logistic_Features_Select_survival = QtWidgets.QCheckBox(self.Step3_MultiVariate_Logistic_Features_frame_survival)
        self.Step3_MultiVariate_Logistic_Features_Select_survival.setSizePolicy(self._getsizePolicy_survival(self.Step3_MultiVariate_Logistic_Features_Select_survival, 'Fixed', 'Fixed'))
        self.Step3_MultiVariate_Logistic_Features_Select_survival.setFont(self.font_min_survival)
        self.Step3_MultiVariate_Logistic_Features_Select_survival.setObjectName("Step3_MultiVariate_Logistic_Features_Select_in_survival")
        self.Step3_MultiVariate_Logistic_Features_Select_survival.setText(' Select')
        self.Step3_MultiVariate_Logistic_Features_Select_survival.setChecked(True)
        self.Step3_MultiVariate_Logistic_Features_gridLayout_survival = QtWidgets.QGridLayout(self.Step3_MultiVariate_Logistic_Features_frame_survival)
        self.Step3_MultiVariate_Logistic_Features_gridLayout_survival.setObjectName("Step3_Method_Logistic_Features_gridLayout")
        self.Step3_MultiVariate_Logistic_Features_gridLayout_survival.addWidget(self.Step3_MultiVariate_Logistic_Features_Select_survival, 0, 2, 1, 1)
        self.Step3_MultiVariate_Logistic_Features_gridLayout_survival.setColumnStretch(0, 3)
        self.Step3_MultiVariate_Logistic_Features_gridLayout_survival.setColumnStretch(1, 7)
        self.Step3_MultiVariate_Logistic_Features_gridLayout_survival.setColumnStretch(2, 3)
        self.Step3_MultiVariate_Logistic_Features_gridLayout_survival.setColumnStretch(3, 7)
        self.Step3_MultiVariate_Logistic_Features_gridLayout_survival.setContentsMargins(3,3,3,1)
        return self.Step3_MultiVariate_Logistic_Features_frame_survival
    def Step3_MultiVariate_Cox_Radscore_survival(self):
        self.Step3_MultiVariate_Logistic_Radscore_frame_survival = QtWidgets.QFrame(self.Step3_feature_selection_survival)
        self.Step3_MultiVariate_Logistic_Radscore_frame_survival.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Step3_MultiVariate_Logistic_Radscore_frame_survival.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Step3_MultiVariate_Logistic_Radscore_frame_survival.setObjectName("Step3_MultiVariate_Logistic_Radscore_frame_survival")
        self.Step3_MultiVariate_Logistic_Radscore_Select_survival = QtWidgets.QCheckBox(self.Step3_MultiVariate_Logistic_Radscore_frame_survival)
        self.Step3_MultiVariate_Logistic_Radscore_Select_survival.setSizePolicy(self._getsizePolicy_survival(self.Step3_MultiVariate_Logistic_Radscore_Select_survival, 'Fixed', 'Fixed'))
        self.Step3_MultiVariate_Logistic_Radscore_Select_survival.setFont(self.font_min_survival)
        self.Step3_MultiVariate_Logistic_Radscore_Select_survival.setObjectName("Step3_MultiVariate_Logistic_Radscore_Select_in_survival")
        self.Step3_MultiVariate_Logistic_Radscore_Select_survival.setText(' Select')
        self.Step3_MultiVariate_Logistic_Radscore_Select_survival.setChecked(True)
        self.Step3_MultiVariate_Logistic_Radscore_gridLayout_survival = QtWidgets.QGridLayout(self.Step3_MultiVariate_Logistic_Radscore_frame_survival)
        self.Step3_MultiVariate_Logistic_Radscore_gridLayout_survival.setObjectName("Step3_MultiVariate_Logistic_Features_gridLayout_survival")
        self.Step3_MultiVariate_Logistic_Radscore_gridLayout_survival.addWidget(self.Step3_MultiVariate_Logistic_Radscore_Select_survival, 0, 2, 1, 1)
        self.Step3_MultiVariate_Logistic_Radscore_gridLayout_survival.setColumnStretch(0, 3)
        self.Step3_MultiVariate_Logistic_Radscore_gridLayout_survival.setColumnStretch(1, 7)
        self.Step3_MultiVariate_Logistic_Radscore_gridLayout_survival.setColumnStretch(2, 3)
        self.Step3_MultiVariate_Logistic_Radscore_gridLayout_survival.setColumnStretch(3, 7)
        self.Step3_MultiVariate_Logistic_Radscore_gridLayout_survival.setContentsMargins(3,3,3,1)
        return self.Step3_MultiVariate_Logistic_Radscore_frame_survival
    def Step3_MultiVariate_Logistic_comboxchange_survival(self,index):
        if index == 0:  # Features
            self.Step3_Logistic_Temp_frame_survival.close()
            self.Step3_Logistic_Temp_frame_survival = self.Step3_MultiVariate_Cox_Features_survival()
            self.Step3_MultiVariate_Logistic_gridLayout_survival.addWidget(self.Step3_Logistic_Temp_frame_survival, 0, 2, 1, 1)
    # Module three main body
    def _setupStep3_feature_selection_survival(self):
        # ===============Step3_feature_selection BOX
        self.Step3_feature_selection_survival = QtWidgets.QGroupBox(self.Step_by_step_survival)
        self.Step3_feature_selection_survival.setSizePolicy(self._getsizePolicy_survival(self.Step3_feature_selection_survival, 'Preferred', 'Preferred'))
        self.Step3_feature_selection_survival.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Step3_feature_selection_survival.setFont(self.font_max_survival)
        self.Step3_feature_selection_survival.setObjectName("Step3_feature_selection")
        self.Step3_feature_selection_survival.setTitle("Step 3 feature selection")
       
        self.Step3_feature_selection_survival.setStyleSheet("QWidget#Step3_feature_selection" + "{" + modleborder_style + modlepadding + "}" + modlefont_color)
        # ===============Step3_Factors_label_survival 'Method'Label
        self.Step3_Factors_label_survival = QtWidgets.QLabel(self.Step3_feature_selection_survival)
        self.Step3_Factors_label_survival.setSizePolicy(self._getsizePolicy_survival(self.Step3_Factors_label_survival, 'Fixed', 'Preferred'))
        self.Step3_Factors_label_survival.setFont(self.font_min_survival)
        self.Step3_Factors_label_survival.setObjectName("Step3_Factors_label_survival")
        self.Step3_Factors_label_survival.setText('Factors      ')
        # ===============Step3_Factors ComboBox
        self.Step3_Factors_survival = QtWidgets.QComboBox(self.Step3_feature_selection_survival)
        self.Step3_Factors_survival.setFont(self.font_min_survival)
        self.Step3_Factors_survival.setObjectName("Step3_Factors_survival")
        self.Step3_Factors_survival.addItems(['Univariate','MultiVariate'])
        self.Step3_Factors_survival.setCurrentIndex(0)
        self.Step3_Factors_survival.currentIndexChanged.connect(self.Step3_Factors_comboxchange_survival)
        self.Step3_Factors_Temp_frame_survival = self.Step3_Univariate_survival()
       
        self.Step3_Factors_survival.setStyleSheet(background_color)
        # ===============gridLayout_1step3_survival in Step3_feature_selection BOX
        self.gridLayout_1step3_survival = QtWidgets.QGridLayout(self.Step3_feature_selection_survival)
        self.gridLayout_1step3_survival.setObjectName("gridLayout_1step3_survival")
        self.gridLayout_1step3_survival.addWidget(self.Step3_Factors_label_survival, 0, 0, 1, 1)
        self.gridLayout_1step3_survival.addWidget(self.Step3_Factors_survival, 0, 1, 1, 2)
        self.gridLayout_1step3_survival.addWidget(self.Step3_Factors_Temp_frame_survival, 1, 0, 1, 4)
        self.gridLayout_1step3_survival.setContentsMargins(3,13,3,1)
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
    def _setupSave_survival(self):
        self.Save_survival = QtWidgets.QGroupBox(self.Step_by_step_survival)
        self.Save_survival.setSizePolicy(self._getsizePolicy_survival(self.Save_survival, 'Preferred', 'Preferred'))
        self.Save_survival.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Save_survival.setFont(self.font_max_survival)
        self.Save_survival.setObjectName("Save_survival")
        self.Save_survival.setTitle("Step 4 Save")
        
        self.Save_survival.setStyleSheet("QWidget#Save_survival" + "{" + modleborder_style + modlepadding + "}" + modlefont_color)
        self.Save_Data_path_label_survival = QtWidgets.QLabel(self.Save_survival)
        self.Save_Data_path_label_survival.setFont(self.font_min_survival)
        self.Save_Data_path_label_survival.setObjectName("Save_Data_path_label_survival")
        self.Save_Data_path_label_survival.setText('Data path')
        self.Save_Data_path_survival = QtWidgets.QLineEdit(self.Save_survival)
        self.Save_Data_path_survival.setObjectName("Save_Data_path_survival")
        self.Save_Data_path_survival.setFont(self.font_min_survival)
        
        self.Save_Data_path_survival.setStyleSheet(modleborder_style)
        self.Save_Data_path_select_survival = QtWidgets.QToolButton(self.Save_survival)
        self.Save_Data_path_select_survival.setFont(self.font_min_survival)
        self.Save_Data_path_select_survival.setObjectName("Save_Data_path_select_survival")
        self.Save_Data_path_select_survival.setText("Select path")
        
        self.Save_Data_path_select_survival.setStyleSheet(background_color)
        self.Save_Data_ok_survival = QtWidgets.QPushButton(self.Save_survival)
        self.Save_Data_ok_survival.setFont(self.font_min_survival)
        self.Save_Data_ok_survival.setObjectName("Save_Data_ok_survival")
        self.Save_Data_ok_survival.setText("OK")
        
        self.Save_Data_ok_survival.setStyleSheet(background_color)
        self.gridLayout_Save_survival = QtWidgets.QGridLayout(self.Save_survival)
        self.gridLayout_Save_survival.setObjectName("gridLayout_Save_survival")
        self.gridLayout_Save_survival.addWidget(self.Save_Data_path_label_survival, 4, 0, 1, 1)
        self.gridLayout_Save_survival.addWidget(self.Save_Data_path_survival, 4, 1, 1, 1)
        self.gridLayout_Save_survival.addWidget(self.Save_Data_path_select_survival, 4, 2, 1, 1)
        self.gridLayout_Save_survival.addWidget(self.Save_Data_ok_survival, 4, 3, 1, 1)
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
        self.gridLayout_result_survival.addWidget(self.Result_text_survival, 0, 1, 4, 1)
    def setupStep_by_step_survival(self):
        self.Step_by_step_survival = QtWidgets.QWidget()
        self.Step_by_step_survival.setObjectName("Step_by_step")
        
        self.Step_by_step_survival.setStyleSheet(MainWindow_background_color)
        ## Step1_load_data box
        self._setupStep1_load_data_survival()
        ## Step2_preprocessing box
        self._setupStep2_preprocessing_survival()
        ## Step3_feature_selection box
        self._setupStep3_feature_selection_survival()
        ## Save_survival box
        self._setupSave_survival()
        ## Edit_survival box
        self._setupEdit_survival()
        ## result box
        self._setupResult_survival()
        self.gridLayout_stepbystep_survival = QtWidgets.QGridLayout(self.Step_by_step_survival)
        self.gridLayout_stepbystep_survival.setObjectName("gridLayout_stepbystep_survival")
        self.gridLayout_stepbystep_survival.addWidget(self.Step1_load_data_survival, 0, 0, 1, 1)
        self.gridLayout_stepbystep_survival.addWidget(self.Step2_preprocessing_survival, 1, 0, 2, 1)
        self.gridLayout_stepbystep_survival.addWidget(self.Step3_feature_selection_survival, 3, 0, 2, 1)
        self.gridLayout_stepbystep_survival.addWidget(self.Save_survival, 5, 0, 1, 1)
        self.gridLayout_stepbystep_survival.addWidget(self.Edit_survival, 6, 0, 1, 1)
        self.gridLayout_stepbystep_survival.addWidget(self.Result_survival, 0, 1, 7, 1)
        self.gridLayout_stepbystep_survival.setColumnStretch(0, 5)
        self.gridLayout_stepbystep_survival.setColumnStretch(1, 5)
        self.gridLayout_stepbystep_survival.setRowStretch(0, 2.2)
        self.gridLayout_stepbystep_survival.setRowStretch(1, 2.2)
        self.gridLayout_stepbystep_survival.setRowStretch(2, 3)
        self.gridLayout_stepbystep_survival.setRowStretch(3, 4)
        self.gridLayout_stepbystep_survival.setRowStretch(4, 1)
        self.gridLayout_stepbystep_survival.setContentsMargins(3,8,3,1)
        self.Step1_data_path_ok_survival.clicked.connect(self.Select_a_path)
        self.Step1_seed_ok_survival.clicked.connect(self.Set_a_seed)
        self.Step1_seperate_ok_survival.clicked.connect(self.Seperate_a_data)
        self.Step2_inpute_ok_survival.clicked.connect(self.Input_data)
        self.Step2_standardize_ok_survival.clicked.connect(self.Standarize_data)
        self.Save_Data_path_select_survival.clicked.connect(self.Data_select_a_path)
        self.Save_Data_ok_survival.clicked.connect(self.Data_save)
        self.Clear_all_survival.clicked.connect(self.Clear_operation)
        return self.Step_by_step_survival
