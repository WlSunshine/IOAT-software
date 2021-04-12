import copy
import tempfile
import matplotlib.pyplot as plt
import numpy as np
import time
import seaborn as sns
import pandas as pd
import rpy2.robjects as robjects
from itertools import cycle
from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import Imputer
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
from prettytable import PrettyTable
import re

dirname = tempfile.TemporaryDirectory()

# Use regular expressions to make long variable names branch functions
def seperate_var_name(var_name):
    var_name_seq = re.findall("[A-Z|_][a-z0-9]*", var_name)
    var0 = ""
    var1 = ""
    var2 = ""
    var3 = ""
    for seq in var_name_seq:
        var0 += seq
        if len(var0) <= 18:
            var1 += seq
        elif 18 < len(var0) <= 36:
            var2 += seq
        else:
            var3 += seq
    var_name_string = var1 + "\n" + var2 + "\n" + var3
    return (var_name_string)


# Define the outlier value as nan to prepare for the subsequent filling of missing values
def fix_abnormal_nan(the_data, the_mean=False, the_std=False):
    the_data = copy.copy(the_data)
    the_data = np.array(the_data, dtype="float32")
    intermediate_data_finally = []

    the_used_mean = []
    the_used_std = []

    for i in np.arange(0, the_data.shape[1]):
        intermediate_data_primary = the_data[:, i]

        if ((the_mean == False) | (the_std == False)):
            the_used_mean.append(intermediate_data_primary.mean())
            the_used_std.append(intermediate_data_primary.std())
        else:
            the_used_mean.append(the_mean[i])
            the_used_std.append(the_std[i])

        intermediate_data_whether_low = intermediate_data_primary < (the_used_mean[i] - 3 * the_used_std[i])
        intermediate_data_whether_high = intermediate_data_primary > (the_used_mean[i] + 3 * the_used_std[i])

        intermediate_data_primary[intermediate_data_whether_low] = np.nan
        intermediate_data_primary[intermediate_data_whether_high] = np.nan
        intermediate_data_finally.append(intermediate_data_primary)
    intermediate_data_finally = np.array(intermediate_data_finally)
    intermediate_data_finally = intermediate_data_finally.T

    return (intermediate_data_finally, the_used_mean, the_used_std)


# Filter out variables with feature variation of 0
def select_not_zero_variance_survival(data):
    # Exclude outliers first
    data = data.replace("NAN", np.NaN)
    data = data.replace("nan", np.NaN)
    data = data.replace("Nan", np.NaN)
    data = data.replace("INF", np.NaN)
    data = data.replace("inf", np.NaN)
    data = data.replace("Inf", np.NaN)
    data = pd.DataFrame(data, dtype="float")

    whether_to_get_by_variance0 = ((data.std() != 0) & (np.array(data.std(), dtype=str) != "nan"))

    whether_to_get_by_variance0 = list(whether_to_get_by_variance0)

    data_names = list(data.columns)

    data_names_get = []
    for i in np.arange(0, len(data_names)):
        if whether_to_get_by_variance0[i]:
            data_names_get.append(data_names[i])

    data_finally = data[data_names_get]
    return (data_finally)


# Define the outlier value as nan to prepare for the subsequent filling of missing values
def fix_abnormal_nan_survival(the_data, the_mean=False, the_std=False):
    the_data = copy.copy(the_data)
    the_data = np.array(the_data, dtype="float32")
    intermediate_data_finally = []

    the_used_mean = []
    the_used_std = []

    for i in np.arange(0, the_data.shape[1]):
        intermediate_data_primary = the_data[:, i]

        if ((the_mean == False) | (the_std == False)):
            the_used_mean.append(intermediate_data_primary.mean())
            the_used_std.append(intermediate_data_primary.std())
        else:
            the_used_mean.append(the_mean[i])
            the_used_std.append(the_std[i])

        intermediate_data_whether_low = intermediate_data_primary < (the_used_mean[i] - 3 * the_used_std[i])
        intermediate_data_whether_high = intermediate_data_primary > (the_used_mean[i] + 3 * the_used_std[i])

        intermediate_data_primary[intermediate_data_whether_low] = np.nan
        intermediate_data_primary[intermediate_data_whether_high] = np.nan
        intermediate_data_finally.append(intermediate_data_primary)
    intermediate_data_finally = np.array(intermediate_data_finally)
    intermediate_data_finally = intermediate_data_finally.T

    return (intermediate_data_finally, the_used_mean, the_used_std)


class Feature_selection_survival(object):

    def __init__(self, data_path):
        self.data_pd0 = pd.DataFrame(pd.read_csv(data_path, engine="python"))

        self.data_pd_feature0 = pd.DataFrame(self.data_pd0[self.data_pd0.columns[2:]])
        self.data_pd_feature = select_not_zero_variance_survival(self.data_pd_feature0)
        self.feature = self.data_pd_feature.values

        self.data_pd_time_status = pd.DataFrame(self.data_pd0[self.data_pd0.columns[0:2]])
        self.time_status = self.data_pd_time_status.values
        self.concat_data = None

    def imputer1(self, is_abnormal_nan=False):
        if is_abnormal_nan:
            self.feature, self.store_mean, self.store_std = fix_abnormal_nan(self.feature)

        self.imp = SimpleImputer(strategy="mean").fit(self.feature)
        self.feature = self.imp.transform(self.feature)
        self.concat_data = pd.DataFrame(pd.concat([self.data_pd_time_status, pd.DataFrame(self.feature)], axis=1))


    def imputer2(self, is_abnormal_nan=False):
        if is_abnormal_nan:
            self.feature, self.store_mean, self.store_std = fix_abnormal_nan(self.feature)

        self.imp = SimpleImputer(strategy="median").fit(self.feature)
        self.feature = self.imp.transform(self.feature)
        self.concat_data = pd.DataFrame(pd.concat([self.data_pd_time_status, pd.DataFrame(self.feature)], axis=1))

    def Standard(self, method="Standardization"):
        if method == "Standardization":
            self.scaler = preprocessing.StandardScaler().fit(self.feature)
        if method == "MinMaxScaler":
            self.scaler = preprocessing.MinMaxScaler().fit(self.feature)

        self.feature = self.scaler.transform(self.feature)
        self.concat_data = pd.DataFrame(pd.concat([self.data_pd_time_status, pd.DataFrame(self.feature)], axis=1))
