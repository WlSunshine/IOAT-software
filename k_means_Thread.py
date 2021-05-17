from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from k_means import K_Means_Class
from k_Means_feature_selection import Feature_selection_survival
import copy
import pickle
import random
import matplotlib.pyplot as plt
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import RGBColor, Pt
import win32com.client
import socket
import pandas as pd
from docx.shared import Inches
import numpy as np
from sklearn.linear_model import Lasso
import time
import os
import re
import shutil
import numpy as np
from sklearn.model_selection import train_test_split
import rpy2.robjects as robjects
import tempfile
import pickle

import winreg

def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return (winreg.QueryValueEx(key, "Desktop")[0])


the_user_desktop = get_desktop()

dirname = tempfile.TemporaryDirectory()


class port(object):
    def __init__(self,view):
        self.view = view
    def write(self,*args):
        self.view.append(*args)


class Step_by_step_k_means():

    def __init__(self):
        # initialize two objects in the class
        self.data = None

        # define the operative times for "undo", "redo" and "clear"
        self.operative_times = 0
        # self.operative_process_model_package = list()
        # self.withdrawn_operative_process_model_package = list()
        self.operative_process = dict()
        # self.withdrawn_operative_times_operative_process = dict()

        self.input_data = None
        self.standadization = None

        ### define the functions

    # ======================================================================= #

    def Select_a_path(self):
        # path = QtWidgets.QFileDialog.getOpenFileName(self, r"open file dialog", r"C:\Users\Administrator\Desktop", r"(*.csv)")
        path = QtWidgets.QFileDialog.getOpenFileName(self, r"open file dialog", the_user_desktop, r"(*.csv)")
        if (path[0]):
            self.operative_times += 1
            self.Result_text_survival.append("\n【Operative time: %s】" % self.operative_times)
            self.Result_text_survival.append("\n【Note】Choose a file path: %s \n" % path[0])
            self.Step1_data_path_survival.setText(str(path[0]))
            self.path = path[0]
            self.operative_process[self.operative_times] = ["select a path", [self.path]]

            global page1_data_path
            _, page1_data_path = os.path.split(self.path)

    def _Input_data(self):
        self.data = Feature_selection_survival(str(self.path))
        self.operative_times += 1
        self.Result_text_survival.append("\n【Operative time: %s】" % self.operative_times)
        if (str(self.Step2_inpute_survival.currentText()) == "Mean"):
            self.input_data = "Mean"
            self.Result_text_survival.append("\n【Note】Input data by 'Mean'")
            self.data.imputer1(is_abnormal_nan=self.Step2_inpute_is_abnormal_nan_survival.isChecked())
        elif (str(self.Step2_inpute_survival.currentText()) == "Median"):
            self.input_data = "Median"
            self.Result_text_survival.append("\n【Note】Input data by 'Median'")
            self.data.imputer2(is_abnormal_nan=self.Step2_inpute_is_abnormal_nan_survival.isChecked())

        # self.operative_process_model_package.append(
        #     (copy.copy(self.data), copy.copy(self.model), copy.copy(self.input_data), copy.copy(self.standadization)))
        # self.operative_process[self.operative_times] = ["input data", [str(self.Step2_inpute_survival.currentText())]]

    def Input_data(self):
        data = copy.copy(self.data)
        try:
            self._Input_data()
        except Exception as e:
            self.operative_times += -1
            self.Result_text_survival.append("\n【Error】: %s" % e)
            self.data = copy.copy(data)

    def _Standarize_data(self):
        self.operative_times += 1
        self.Result_text_survival.append("\n【Operative time: %s】" % self.operative_times)

        if (str(self.Step2_standardize_survival.currentText()) == "Standardization"):
            self.standadization = "Standardization"
            self.Result_text_survival.append("\n【Note】Standarize data by 'Standardization'")
            self.data.Standard(method="Standardization")
        elif (str(self.Step2_standardize_survival.currentText()) == "MinMaxScaler"):
            self.standadization = "MinMaxScaler"
            self.Result_text_survival.append("\n【Note】Standarize data by 'MinMaxScaler'")
            self.data.Standard(method="MinMaxScaler")

        # self.operative_process_model_package.append(
        #     (copy.copy(self.data), copy.copy(self.model), copy.copy(self.input_data), copy.copy(self.standadization)))
        # self.operative_process[self.operative_times] = ["standardize data",
        #                                                 [str(self.Step2_standardize_survival.currentText())]]

    def Standarize_data(self):
        data = copy.copy(self.data)
        try:
            self._Standarize_data()
        except Exception as e:
            self.operative_times += -1
            self.Result_text_survival.append("\n【Error】: %s" % e)
            self.data = copy.copy(data)


    def _K_Means_K1(self):
        self.operative_times += 1
        self.Result_text_survival.append("\n【Operative time: %s】" % self.operative_times)
        self.solution_class = K_Means_Class(self.data.concat_data)
        self.Result_text_survival.append("\n【Note】User set K value by yourself'")
        self.solution_class.cluster(k=int(self.Step3_K_Means_K_Value1.text()))
        self.Result_text_survival.append("\n【Note】Done, the result of y has been loaded in your desk'")

    def K_Means_K1(self):
        data = copy.copy(self.data)
        try:
            self._K_Means_K1()
        except Exception as e:
            self.operative_times += -1
            self.Result_text_survival.append("\n【Error】: %s" % e)
            self.data = copy.copy(data)

    def _K_Means_K2(self):
        self.operative_times += 1
        self.Result_text_survival.append("\n【Operative time: %s】" % self.operative_times)
        self.solution_class = K_Means_Class(self.data.concat_data)
        self.Result_text_survival.append("\n【Note】System find the best K value ")
        self.solution_class.cluster(seed=1234,k=None,optimal_k_method="silhouette",ami_y=None,kmeans_kwargs=None)
        self.Result_text_survival.append("\n【Note】Done, the result of y has been loaded in your desk'")

    def K_Means_K2(self):
        data = copy.copy(self.data)
        try:
            # print("starting...maybe a few minute is needed")
            self._K_Means_K2()
            plt.show()
        except Exception as e:
            self.operative_times += -1
            self.Result_text_survival.append("\n【Error】: %s" % e)
            self.data = copy.copy(data)

    def _K_Means_K3(self):
        self.operative_times += 1
        self.Result_text_survival.append("\n【Operative time: %s】" % self.operative_times)
        self.solution_class = K_Means_Class(self.data.concat_data)
        self.Result_text_survival.append("\n【Note】System find the best K value ")
        self.solution_class.cluster(seed=1234,k=None,optimal_k_method="ami",ami_y=None,kmeans_kwargs=None)
        self.Result_text_survival.append("\n【Note】Done, the result of y has been loaded in your desk'")

    def K_Means_K3(self):
        data = copy.copy(self.data)
        try:
            # print("starting...maybe a few minute is needed")
            self._K_Means_K3()
            plt.show()
        except Exception as e:
            self.operative_times += -1
            self.Result_text_survival.append("\n【Error】: %s" % e)
            self.data = copy.copy(data)


    def Clear_operation(self):
        self.operative_times = 0
        self.data = None
        self.input_data = None
        self.standadization = None
        self.Step1_data_path_survival.clear()
        self.Step2_inpute_survival.setCurrentText("Median")
        self.Step2_standardize_survival.setCurrentText("Standardization")
        self.Step2_inpute_is_abnormal_nan_survival.setChecked(False)
        self.path = None
        self.Result_text_survival.clear()
        self.Result_text_survival.append("\n【Clear all operations, operation step is initialized to 0】 \n")
