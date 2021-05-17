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
def return_range_for_heat_figure_survival(train_feature, *test_feature): # 使用百分位数
    if test_feature:
        test_feature = test_feature[0]
        train_min = np.percentile(train_feature, 0.5)
        test_min = np.percentile(test_feature, 0.5)
        train_max = np.percentile(train_feature, 99.5)
        test_max = np.percentile(test_feature, 99.5)
        feature_min = min(train_min, test_min)
        feature_max = max(train_max, test_max)
    else:
        feature_min = np.percentile(train_feature, 0.5)
        feature_max = np.percentile(train_feature, 99.5)
    return(feature_min, feature_max)
def report_heat_figure(data, title = "Clustermap of the features", rotation = 45, vmin=None, vmax=None):
    # 设置是否显示轴坐标
    if (data.shape[0] <= 20):
        the_yticklabels = True
    else:
        the_yticklabels = False
    if (data.shape[1] <= 20):
        the_xticklabels = True
    else:
        the_xticklabels = False
    # 设置标签刻度范围，设置函数的vmin和vmax
    g = sns.clustermap(data, xticklabels = the_xticklabels, yticklabels = the_yticklabels, cmap="seismic", 
                       figsize=(6, 6), vmin = vmin, vmax = vmax)
    ax = g.ax_heatmap
    label_x = ax.get_xticklabels()
    plt.setp(label_x, rotation = rotation, horizontalalignment = "right")
    label_y = ax.get_yticklabels()
    plt.setp(label_y, rotation = 360, horizontalalignment = "left")
    plt.title(title, loc = 'left')
    filename = "\\".join([dirname.name, "".join([str(time.time()), "figure.png"])])
    plt.savefig(filename)
    plt.show()
    return(filename)
# 用正则表达式，使长变量名分行的函数
def seperate_var_name(var_name):
    var_name_seq = re.findall("[A-Z|_][a-z0-9]*", var_name)
    var0 = ""
    var1 = ""
    var2 = ""
    var3 = ""
    for seq in var_name_seq:
        var0 += seq
        if len(var0)<=18:
            var1 += seq
        elif 18<len(var0)<=36:
            var2 += seq
        else:
            var3 += seq
    var_name_string = var1 + "\n" + var2 + "\n" + var3
    return(var_name_string)
# 定义离群值为nan，为后续的缺失值填补做准备
def fix_abnormal_nan(the_data, the_mean=False, the_std=False):
    the_data = copy.copy(the_data)
    the_data = np.array(the_data, dtype="float32")
    intermediate_data_finally = []
    the_used_mean = []
    the_used_std = []
    for i in np.arange(0, the_data.shape[1]):
        intermediate_data_primary = the_data[:,i]
        if ((the_mean==False) | (the_std==False)):
            the_used_mean.append(intermediate_data_primary.mean())
            the_used_std.append(intermediate_data_primary.std())
        else:
            the_used_mean.append(the_mean[i])
            the_used_std.append(the_std[i])
        intermediate_data_whether_low = intermediate_data_primary<(the_used_mean[i]-3*the_used_std[i])
        intermediate_data_whether_high = intermediate_data_primary>(the_used_mean[i]+3*the_used_std[i])
        intermediate_data_primary[intermediate_data_whether_low] = np.nan
        intermediate_data_primary[intermediate_data_whether_high] = np.nan
        intermediate_data_finally.append(intermediate_data_primary)
    intermediate_data_finally = np.array(intermediate_data_finally)
    intermediate_data_finally = intermediate_data_finally.T
    return(intermediate_data_finally, the_used_mean, the_used_std)
# 筛选掉特征变异度为0的变量
def select_not_zero_variance_survival(data):
    # 先排除异常值
    data = data.replace("NAN", np.NaN)
    data = data.replace("nan", np.NaN)
    data = data.replace("Nan", np.NaN)
    data = data.replace("INF", np.NaN)
    data = data.replace("inf", np.NaN)
    data = data.replace("Inf", np.NaN)
    data = pd.DataFrame(data, dtype = "float")
    whether_to_get_by_variance0 = ((data.std()!=0) & (np.array(data.std(), dtype = str)!="nan"))
    whether_to_get_by_variance0 = list(whether_to_get_by_variance0)
    data_names = list(data.columns)
    data_names_get = []
    for i in np.arange(0, len(data_names)):
        if whether_to_get_by_variance0[i]:
            data_names_get.append(data_names[i])
    data_finally = data[data_names_get]
    return(data_finally)
# 定义离群值为nan，为后续的缺失值填补做准备
def fix_abnormal_nan_survival(the_data, the_mean=False, the_std=False):
    the_data = copy.copy(the_data)
    the_data = np.array(the_data, dtype="float32")
    intermediate_data_finally = []
    the_used_mean = []
    the_used_std = []
    for i in np.arange(0, the_data.shape[1]):
        intermediate_data_primary = the_data[:,i]
        if ((the_mean==False) | (the_std==False)):
            the_used_mean.append(intermediate_data_primary.mean())
            the_used_std.append(intermediate_data_primary.std())
        else:
            the_used_mean.append(the_mean[i])
            the_used_std.append(the_std[i])
        intermediate_data_whether_low = intermediate_data_primary<(the_used_mean[i]-3*the_used_std[i])
        intermediate_data_whether_high = intermediate_data_primary>(the_used_mean[i]+3*the_used_std[i])
        intermediate_data_primary[intermediate_data_whether_low] = np.nan
        intermediate_data_primary[intermediate_data_whether_high] = np.nan
        intermediate_data_finally.append(intermediate_data_primary)
    intermediate_data_finally = np.array(intermediate_data_finally)
    intermediate_data_finally = intermediate_data_finally.T
    return(intermediate_data_finally, the_used_mean, the_used_std)
# 特征筛选相关系数图
def correlation_analysis_survival(feature, is_train=True):
    if len(feature.columns.values.tolist()) <= 10:
        # 定义输出图形的位置
        filename = "\\".join([dirname.name, "".join([str(time.time()), "figure.png"])])
        # 计算相关系数
        corr_matrix = feature.corr() # pearson相关系数
        # corr_matrix = feature.corr("kendall") # Kendall Tau相关系数
        # corr_matrix = feature.corr("spearman") # spearman相关系数
        # 热力图显示和保存
        fig, ax = plt.subplots(figsize=(9,9)) # 设置画面大小
        plt.subplots_adjust(left=0.2, bottom=0.15, right=0.95, top=0.9)
        if is_train:
            plt.title("Correlation coefficient figure of the training samples")
        else:
            plt.title("Correlation coefficient figure of the testing samples" )
        ax = sns.heatmap(corr_matrix, annot=True, square=True, cmap="seismic", vmin=-1, vmax=1)
        label_x = ax.get_xticklabels()
        plt.setp(label_x, rotation = 45, horizontalalignment = "center")
        label_y = ax.get_yticklabels()
        plt.setp(label_y, rotation = 45, verticalalignment="center")
        plt.savefig(filename)
        plt.show()
        return(filename)
# 定义自变量之间的相关性来筛选变量
def correlation_xx_survival(feature_data, cutoff):
    """ 由R语言caret包findCorrelation函数改写而来 """
    feature_data = pd.DataFrame(feature_data)
    corr_matrix = feature_data.corr().abs()
    corr_mean = corr_matrix.mean()
    corr_mean = pd.DataFrame({"values": corr_mean})
    corr_order = pd.Categorical(corr_mean["values"]).codes
    corr_matrix2 = np.triu(corr_matrix, 1)
    rowsToCheck, colsToCheck = np.where(corr_matrix2 > cutoff)
    colsToDiscard = list(corr_order[colsToCheck]) > np.array(corr_order[rowsToCheck])
    rowsToDiscard = ~colsToDiscard
    deletecol = list(colsToCheck[colsToDiscard]) + list(rowsToCheck[rowsToDiscard])
    deletecol = np.unique(deletecol)
    allcol = list(range(feature_data.shape[1]))
    remaincol = [i for i in allcol if i not in deletecol]
    return(remaincol)
# 使用R求lasso_cox，筛选变量
def Lasso_cox_data_from_R_survival(data_path):
    lasso_result_1 = "\\".join([dirname.name, "lasso_result.csv"])
    lasso_result_2 = "\\".join([dirname.name, "lasso_result_cutvalue.csv"])
    r = robjects.r
    r('''
    library(glmnet)
    ''')
    r('''
    import_to_r <- function(data_path_r, lasso_result_r, lasso_result_2){
            data_path <<- data_path_r
            lasso_result_1 <<- lasso_result_r
            lasso_result_2 <<- lasso_result_2
            }
    ''')
    r['import_to_r'](data_path, lasso_result_1, lasso_result_2)
    r('''
    data <- read.csv(data_path, header=TRUE, sep=",")
    time <- data[, 1]
    event <- data[, 2]
    rad <- as.matrix(data[, -c(1,2)])
    y <- cbind(time=time, status=event)
    cox_model <- glmnet(rad, y, family = "cox")
    bl_lambda <- cox_model$lambda
    data_for_export <- data.frame(bl_lambda)
    i = 1
    while (i <= length(row.names(cox_model$beta))){
        if (i == 1){
            bl_lambda_for_export <- data.frame(cox_model$beta[row.names(cox_model$beta)[i],])
        }else{
            bl_lambda_for_export <- cbind(bl_lambda_for_export, cox_model$beta[row.names(cox_model$beta)[i],])
        }
    i = i + 1
    }
    names(bl_lambda_for_export) <- row.names(cox_model$beta)
    data_for_export <- cbind(data_for_export, bl_lambda_for_export)
    cv_cox_model <- cv.glmnet(rad, y, family = "cox")
    cv_lambda <- cv_cox_model$lambda
    data_for_export <- cbind(data_for_export, cv_lambda)
    cv_cvm <- cv_cox_model$cvm
    data_for_export <- cbind(data_for_export, cv_cvm)
    write.csv(data_for_export, lasso_result_1)
    write.csv(cv_cox_model$lambda.min, lasso_result_2)
    ''')
    return(lasso_result_1, lasso_result_2)
# 根据R导出的数据，绘制lasso图
def Lasso_cox_survival(data_path, data_path_best):
    data = pd.read_csv(data_path)
    data_value = data.values
    data1 = data_value[:, -2:]       # 读取cvm数据
    data2 = data_value[:, :-2]       # 读取coefficients数据
    data_best = pd.read_csv(data_path_best)
    value_best = data_best.values[0,1]
    # figure1
    m_log_alphas = np.log(list(data1[:, 0]))
    cvm_mean = data1[:, 1]
    plt.figure()
    plt.plot(m_log_alphas, cvm_mean, color = "black")
    plt.axvline(np.log(value_best), linestyle="--", color = "k", label = "alpha CV")
    plt.legend()
    plt.xlabel("ln(alpha)")
    plt.ylabel("cvm")
    plt.title("Mean square error: Lars")
    plt.axis("tight")
    filename_cv = "\\".join([dirname.name, "".join([str(time.time()), "figure.png"])])
    plt.savefig(filename_cv)
    plt.show()
    # figure2
    m_log_alphas = np.log(list(data2[:, 1]))
    colors = cycle(['b', 'r', 'g', 'c', 'k'])
    plt.figure()
    data_for_lasso_path = data2[:, 2: ]
    data_for_lasso_path = np.array(data_for_lasso_path)
    data_for_lasso_path = data_for_lasso_path.T
    for coef_1, c in zip(data_for_lasso_path, colors):
        plt.plot(m_log_alphas, coef_1, c = c)
    plt.xlabel("ln(alpha)")
    plt.ylabel("coefficients")
    plt.title("Lasso paths")
    plt.axis("tight")
    plt.axvline(np.log(value_best), linestyle = "--", color = "k", label = "alpha CV")
    filename_lasso_path = "\\".join([dirname.name, "".join([str(time.time()), "figure.png"])])
    plt.savefig(filename_lasso_path)
    plt.show()
    # return the two filenames
    return(filename_cv, filename_lasso_path)
def Lasso_cox_remain_feature_name_survival(data_path, data_path_best):
    data = pd.read_csv(data_path)
    data_var_name = data.columns[2:-2]
    data_value = data.values[:,2:-2]
    data_best = pd.read_csv(data_path_best)
    value_best = data_best.values[0, 1]
    alpha_list = data.values[:, 1]
    whether_get = list(alpha_list).index(value_best)
    coef_list = data_value[whether_get, ]
    whether_get_var = [a != 0 for a in coef_list]
    data_var_name_get = [data_var_name[i] for i in np.arange(len(data_var_name)) if whether_get_var[i] == True]
    return(data_var_name_get)
def stepwise_cox_from_R_survival(data_path):
    stepwise_result = "\\".join([dirname.name, "stepwise_result.csv"])
    r = robjects.r
    r('''
    library(survival)
    library(survminer)
    ''')
    r('''
    import_to_r <- function(data_path_r, stepwise_result_r){
            data_path <<- data_path_r
            stepwise_result <<- stepwise_result_r
            }
    ''')
    r['import_to_r'](data_path, stepwise_result)
    r('''
    data <- read.csv(data_path)
    f <- coxph(Surv(time, status) ~ ., data = data)
    f2 <- step(f, direction = "both", steps = 10000)
    f3 <- summary(f2)
    result <- data.frame(f3$coefficients)
    write.csv(result, stepwise_result)
    ''')
    return(stepwise_result)
def stepwise_cox_remain_feature_name_survival(data_path):
    data = pd.read_csv(data_path)
    name = list(data[data.columns[0]])
    return(name)
def univariate_cox_from_R_survival(data_path):
    univariate_result = "\\".join([dirname.name, "univariate_result.csv"])
    r = robjects.r
    r('''
    library(survival)
    library(survminer)
    ''')
    r('''
    import_to_r <- function(data_path_r, univariate_result_r){
            data_path <<- data_path_r
            univariate_result <<- univariate_result_r
            }
    ''')
    r['import_to_r'](data_path, univariate_result)
    r('''
    data <- read.csv(data_path)
    i <- 1
    result_total <- data.frame()
    while (i <= (length(colnames(data)) - 2)){
        the_colname <- colnames(data)[i + 2]
        data2 <- data[c("time", "status", the_colname)]
        f <- coxph(Surv(time, status) ~ ., data = data2)
        f2 <- summary(f)
        result <- data.frame(f2$coefficients)
        if (result[5] <= 0.05){
            result_total <- rbind(result_total, result)
        }
        i <- i + 1
    }
    write.csv(result_total, univariate_result)
    ''')
    return(univariate_result)
def univariate_cox_remain_feature_name_survival(data_path):
    data = pd.read_csv(data_path)
    name = list(data[data.columns[0]])
    return(name)
def logrank_from_R_survival(data_path):
    logrank_result = "\\".join([dirname.name, "logrank_result.csv"])
    r = robjects.r
    r('''
    library(survival)
    library(survminer)
    library(coin)
    ''')
    r('''
    import_to_r <- function(data_path_r, logrank_result_r){
            data_path <<- data_path_r
            logrank_result <<- logrank_result_r
            }
    ''')
    r['import_to_r'](data_path, logrank_result)
    r('''
    data <- read.csv(data_path)
    i <- 1
    result_total <- data.frame()
    while (i <= (length(colnames(data)) - 2)){
        the_colname <- colnames(data)[i + 2]
        data2 <- data[c("time", "status", the_colname)]
        data2[,3] <- as.factor(data2[,3])
        f <- logrank_test(Surv(time, status) ~ ., data2)
        z <- f@statistic@teststatistic
        if (z < 0){
          p <- 2 * pnorm(z)
        }else{
          p <- 2 * (1 - pnorm(z))
        }
        result <- data.frame(the_colname, z, p)
        if (p <= 0.05){
            result_total <- rbind(result, result_total)
        }
        i <- i + 1
    }
    write.csv(result_total, logrank_result)
      ''')
    return(logrank_result)
def logrank_remain_feature_name_survival(data_path):
    data = pd.read_csv(data_path)
    name = list(data[data.columns[1]])
    return(name)
def select_by_variable_names_survival(variable_names, variable_values, remain_feature_name):
    remain_variable_names = []
    remain_variable_values = []
    i = 0
    while i < len(variable_names):
        if variable_names[i] in remain_feature_name:
            remain_variable_names.append(variable_names[i])
            remain_variable_values.append(variable_values[:, i])
        i += 1
    remain_variable_values = np.array(remain_variable_values)
    remain_variable_values = remain_variable_values.T
    return(remain_variable_names, remain_variable_values)
def calculate_coefficients_for_radscore_from_R_survival(data_path):
    coefficients_path = "\\".join([dirname.name, "coefficients_path.csv"])
    r = robjects.r
    r('''
    library(survival)
    ''')
    r('''
    import_to_r <- function(data_path_r, coefficients_path_r){
            data_path <<- data_path_r
            coefficients_path <<- coefficients_path_r
            }
    ''')
    r['import_to_r'](data_path, coefficients_path)
    r('''
    data <- read.csv(data_path, header = TRUE, sep = ",")
    f <- coxph(Surv(time, status) ~ ., data)
    f2 <- summary(f)
    f3 <- data.frame(f2$coefficients)[1]
    write.csv(f3, coefficients_path)
    ''')
    return(coefficients_path)
def calculate_radscore_survival(coefficients, features):
    radscore = np.dot(coefficients, features)
    return(radscore)
class Feature_selection_survival(object):
    def __init__(self, data_path):
        self.data_pd0 = pd.read_csv(data_path, engine = "python")
        self.data_pd_feature0 = self.data_pd0[self.data_pd0.columns[2:]]
        self.data_pd_feature = select_not_zero_variance_survival(self.data_pd_feature0)
        self.feature = self.data_pd_feature.values
        self.data_pd_time_status = self.data_pd0[self.data_pd0.columns[0:2]]
        self.time_status = self.data_pd_time_status.values
        self.data_variable_names = list(self.data_pd_feature.columns[0:])
        self.coefficients_values_for_radscore = None
        self.test = True
    def split(self, train_size = 0.7, seed = 1234):
        if train_size == 1.0:
            self.test = False
            self.train_feature = self.feature
            self.train_time_status = self.time_status
        else:
            self.test = True
            self.train_time_status, self.test_time_status = train_test_split(self.time_status, train_size = train_size, random_state=seed)
            self.train_feature, self.test_feature = train_test_split(self.feature, train_size = train_size, random_state=seed)
        self.split_report_result_list = None
    def imputer1(self, is_abnormal_nan = False):
        if is_abnormal_nan:
            self.train_feature, self.store_mean, self.store_std = fix_abnormal_nan(self.train_feature)
        if self.test:
            if is_abnormal_nan:
                self.test_feature, _, __ = fix_abnormal_nan(self.test_feature, self.store_mean, self.store_std)
        self.imp = SimpleImputer(strategy="mean").fit(self.train_feature)
        self.train_feature = self.imp.transform(self.train_feature)
        if self.test:
            self.test_feature = self.imp.transform(self.test_feature)
    def imputer2(self, is_abnormal_nan = False):
        if is_abnormal_nan:
            self.train_feature, self.store_mean, self.store_std = fix_abnormal_nan(self.train_feature)
        if self.test:
            if is_abnormal_nan:
                self.test_feature, _, __ = fix_abnormal_nan(self.test_feature, self.store_mean, self.store_std)
        self.imp = SimpleImputer(strategy="median").fit(self.train_feature)
        self.train_feature = self.imp.transform(self.train_feature)
        if self.test:
            self.test_feature = self.imp.transform(self.test_feature)
    def Standard(self, method="Standardization"):
        if method == "Standardization":
            self.scaler = preprocessing.StandardScaler().fit(self.train_feature)
        if method == "MinMaxScaler":
            self.scaler = preprocessing.MinMaxScaler().fit(self.train_feature)
        self.train_feature = self.scaler.transform(self.train_feature)
        if self.test:
            self.test_feature = self.scaler.transform(self.test_feature)
    def select_by_lasso_cox(self):
        print("starting...")
        time.sleep(3)
        self.parameters = {"C": "auto selection"}
        train_data = np.concatenate((self.train_time_status, self.train_feature), axis=1)
        train_data = pd.DataFrame(train_data, columns = ["time", "status"] + list(self.data_variable_names))
        train_data_path = "\\".join([dirname.name, "".join([str(time.time()), "train_data_path.csv"])])
        train_data.to_csv(train_data_path, index = False)
        lasso_result_path_1, lasso_result_path_2 = Lasso_cox_data_from_R_survival(train_data_path)
        self.lasso_figure_1, self.lasso_figure_2 = Lasso_cox_survival(lasso_result_path_1, lasso_result_path_2)
        remained_variable_names = Lasso_cox_remain_feature_name_survival(lasso_result_path_1, lasso_result_path_2)
        _, self.train_feature = select_by_variable_names_survival(self.data_variable_names, self.train_feature, remained_variable_names)
        # 使两个聚类热图的图例标签一致
        if self.test:
            feature_min, feature_max = return_range_for_heat_figure_survival(self.train_feature, self.test_feature)
        else:
            feature_min, feature_max = return_range_for_heat_figure_survival(self.train_feature)
        if abs(feature_min) < abs(feature_max):
            feature_min = -abs(feature_max)
            feature_max = abs(feature_max)
        else:
            feature_max = abs(feature_min)
            feature_min = -abs(feature_min)
        self.figure_report1 = report_heat_figure(self.train_feature, title = "Heatmap of training samples for variance model", rotation = 45, vmin=feature_min, vmax=feature_max)
        data_variable_names = []
        for name in _:
            name2 = seperate_var_name(name)
            data_variable_names.append(name2)
        train_feature = pd.DataFrame(self.train_feature, columns = data_variable_names)
        self.figure_report3 = correlation_analysis_survival(train_feature)
        if self.test:
            self.data_variable_names, self.test_feature = select_by_variable_names_survival(self.data_variable_names, self.test_feature, remained_variable_names)
            self.figure_report2 = report_heat_figure(self.test_feature, title = "Heatmap of testing samples for variance model", rotation = 45, vmin=feature_min, vmax=feature_max)
            test_feature = pd.DataFrame(self.test_feature, columns = data_variable_names)
            self.figure_report4 = correlation_analysis_survival(test_feature, is_train = False)
        else:
            self.data_variable_names = _
        print("remained feature numbers: %s" %len(self.data_variable_names))
        print("remained features: %s" %self.data_variable_names)
    def select_by_stepwise_cox(self, select = True, radscore = False):
        print("starting...")
        time.sleep(3)
        if select:
            self.parameters = {"whether select features": select}
            train_data = np.concatenate((self.train_time_status, self.train_feature), axis=1)
            train_data = pd.DataFrame(train_data, columns = ["time", "status"] + list(self.data_variable_names))
            train_data_path = "\\".join([dirname.name, "".join([str(time.time()), "train_data_path.csv"])])
            train_data.to_csv(train_data_path, index = False)
            stepwise_cox_result_path = stepwise_cox_from_R_survival(train_data_path)
            remained_variable_names = stepwise_cox_remain_feature_name_survival(stepwise_cox_result_path)
            _, self.train_feature = select_by_variable_names_survival(self.data_variable_names, self.train_feature, remained_variable_names)
            # 使两个聚类热图的图例标签一致
            if self.test:
                feature_min, feature_max = return_range_for_heat_figure_survival(self.train_feature, self.test_feature)
            else:
                feature_min, feature_max = return_range_for_heat_figure_survival(self.train_feature)
            if abs(feature_min) < abs(feature_max):
                feature_min = -abs(feature_max)
                feature_max = abs(feature_max)
            else:
                feature_max = abs(feature_min)
                feature_min = -abs(feature_min)
            self.figure_report1 = report_heat_figure(self.train_feature, title = "Heatmap of training samples for variance model", rotation = 45, vmin=feature_min, vmax=feature_max)
            data_variable_names = []
            for name in _:
                name2 = seperate_var_name(name)
                data_variable_names.append(name2)
            train_feature = pd.DataFrame(self.train_feature, columns = data_variable_names)
            self.figure_report3 = correlation_analysis_survival(train_feature)
            if self.test:
                self.data_variable_names, self.test_feature = select_by_variable_names_survival(self.data_variable_names, self.test_feature, remained_variable_names)
                self.figure_report2 = report_heat_figure(self.test_feature, title = "Heatmap of testing samples for variance model", rotation = 45, vmin=feature_min, vmax=feature_max)
                test_feature = pd.DataFrame(self.test_feature, columns = data_variable_names)
                self.figure_report4 = correlation_analysis_survival(test_feature, is_train = False)
            else:
                self.data_variable_names = _
        else:
            print("【Note】Did not select features.")
        print("remained feature numbers: %s" %len(self.data_variable_names))
        print("remained features: %s" %self.data_variable_names)
        if radscore == True:
            time.sleep(3)
            print("【Note】The remained features were used to calculated the radscore.")
            train_data = np.concatenate((self.train_time_status, self.train_feature), axis=1)
            train_data = pd.DataFrame(train_data, columns = ["time", "status"] + list(self.data_variable_names))
            train_data_path = "\\".join([dirname.name, "".join([str(time.time()), "train_data_path.csv"])])
            train_data.to_csv(train_data_path, index = False)
            coefficients_path = calculate_coefficients_for_radscore_from_R_survival(train_data_path)
            coefficients = pd.read_csv(coefficients_path)
            print("The coefficients for radscore are:")
            print(coefficients.values)
            coefficients_values = np.array(coefficients.values[:,1])
            self.data_variable_names_for_radscore = np.array(coefficients.values[:,0]) # 输出用于计算radscore的变量名，用于模型预测模块
            self.coef_after_radscore = coefficients_values # 输出计算radscore的系数，用于模型预测模块
            self.whether_radscore = True
            self.data_variable_names = ["radscore"]
            self.train_feature = pd.DataFrame(calculate_radscore_survival(self.train_feature, coefficients_values.T), columns = self.data_variable_names)
            if self.test:
                self.test_feature = pd.DataFrame(calculate_radscore_survival(self.test_feature, coefficients_values.T), columns = self.data_variable_names)
    def select_by_univariate_cox(self):
        print("starting...")
        time.sleep(3)
        self.parameters = {"P_value": 0.05}
        train_data = np.concatenate((self.train_time_status, self.train_feature), axis=1)
        train_data = pd.DataFrame(train_data, columns = ["time", "status"] + list(self.data_variable_names))
        train_data_path = "\\".join([dirname.name, "".join([str(time.time()), "train_data_path.csv"])])
        train_data.to_csv(train_data_path, index = False)
        univariate_cox_result_path = univariate_cox_from_R_survival(train_data_path)
        remained_variable_names = univariate_cox_remain_feature_name_survival(univariate_cox_result_path)
        _, self.train_feature = select_by_variable_names_survival(self.data_variable_names, self.train_feature, remained_variable_names)
        # 使两个聚类热图的图例标签一致
        if self.test:
            feature_min, feature_max = return_range_for_heat_figure_survival(self.train_feature, self.test_feature)
        else:
            feature_min, feature_max = return_range_for_heat_figure_survival(self.train_feature)
        if abs(feature_min) < abs(feature_max):
            feature_min = -abs(feature_max)
            feature_max = abs(feature_max)
        else:
            feature_max = abs(feature_min)
            feature_min = -abs(feature_min)
        self.figure_report1 = report_heat_figure(self.train_feature, title = "Heatmap of training samples for variance model", rotation = 45, vmin=feature_min, vmax=feature_max)
        data_variable_names = []
        for name in _:
            name2 = seperate_var_name(name)
            data_variable_names.append(name2)
        train_feature = pd.DataFrame(self.train_feature, columns = data_variable_names)
        self.figure_report3 = correlation_analysis_survival(train_feature)
        if self.test:
            self.data_variable_names, self.test_feature = select_by_variable_names_survival(self.data_variable_names, self.test_feature, remained_variable_names)
            self.figure_report2 = report_heat_figure(self.test_feature, title = "Heatmap of testing samples for variance model", rotation = 45, vmin=feature_min, vmax=feature_max)
            test_feature = pd.DataFrame(self.test_feature, columns = data_variable_names)
            self.figure_report4 = correlation_analysis_survival(test_feature, is_train = False)
        else:
            self.data_variable_names = _
        print("remained feature numbers: %s" %len(self.data_variable_names))
        print("remained features: %s" %self.data_variable_names)
    def select_by_logrank(self):
        print("starting...")
        time.sleep(3)
        self.parameters = {"P_value": 0.05}
        train_data = np.concatenate((self.train_time_status, self.train_feature), axis=1)
        train_data = pd.DataFrame(train_data, columns = ["time", "status"] + list(self.data_variable_names))
        train_data_path = "\\".join([dirname.name, "".join([str(time.time()), "train_data_path.csv"])])
        train_data.to_csv(train_data_path, index = False)
        logrank_result_path = logrank_from_R_survival(train_data_path)
        remained_variable_names = logrank_remain_feature_name_survival(logrank_result_path)
        _, self.train_feature = select_by_variable_names_survival(self.data_variable_names, self.train_feature, remained_variable_names)
        # 使两个聚类热图的图例标签一致
        if self.test:
            feature_min, feature_max = return_range_for_heat_figure_survival(self.train_feature, self.test_feature)
        else:
            feature_min, feature_max = return_range_for_heat_figure_survival(self.train_feature)
        if abs(feature_min) < abs(feature_max):
            feature_min = -abs(feature_max)
            feature_max = abs(feature_max)
        else:
            feature_max = abs(feature_min)
            feature_min = -abs(feature_min)
        self.figure_report1 = report_heat_figure(self.train_feature, title = "Heatmap of training samples for variance model", rotation = 45, vmin=feature_min, vmax=feature_max)
        data_variable_names = []
        for name in _:
            name2 = seperate_var_name(name)
            data_variable_names.append(name2)
        train_feature = pd.DataFrame(self.train_feature, columns = data_variable_names)
        self.figure_report3 = correlation_analysis_survival(train_feature)
        if self.test:
            self.data_variable_names, self.test_feature = select_by_variable_names_survival(self.data_variable_names, self.test_feature, remained_variable_names)
            self.figure_report2 = report_heat_figure(self.test_feature, title = "Heatmap of testing samples for variance model", rotation = 45, vmin=feature_min, vmax=feature_max)
            test_feature = pd.DataFrame(self.test_feature, columns = data_variable_names)
            self.figure_report4 = correlation_analysis_survival(test_feature, is_train = False)
        else:
            self.data_variable_names = _
        print("remained feature numbers: %s" %len(self.data_variable_names))
        print("remained features: %s" %self.data_variable_names)
    def select_by_correlation_xx(self, cutoff = 0.7):
        print("starting...")
        time.sleep(3)
        self.parameters = {"correlation": cutoff}
        training_feature_name = correlation_xx_survival(self.train_feature, cutoff = cutoff)
        data_variable_names = []
        for i in training_feature_name:
            data_variable_names.append(self.data_variable_names[i])
        self.data_variable_names = copy.copy(data_variable_names)
        self.train_feature = self.train_feature[:, training_feature_name]
        # 使两个聚类热图的图例标签一致
        if self.test:
            feature_min, feature_max = return_range_for_heat_figure_survival(self.train_feature, self.test_feature)
        else:
            feature_min, feature_max = return_range_for_heat_figure_survival(self.train_feature)
        if abs(feature_min) < abs(feature_max):
            feature_min = -abs(feature_max)
            feature_max = abs(feature_max)
        else:
            feature_max = abs(feature_min)
            feature_min = -abs(feature_min)
        self.figure_report1 = report_heat_figure(self.train_feature, title = "Heatmap of training samples for variance model", rotation = 45, vmin=feature_min, vmax=feature_max)
        data_variable_names = []
        for name in self.data_variable_names:
            name2 = seperate_var_name(name)
            data_variable_names.append(name2)
        train_feature = pd.DataFrame(self.train_feature, columns = data_variable_names)
        self.figure_report3 = correlation_analysis_survival(train_feature)
        if self.test:
            self.test_feature = self.test_feature[:, training_feature_name]
            self.figure_report2 = report_heat_figure(self.test_feature, title = "Heatmap of testing samples for variance model", rotation = 45, vmin=feature_min, vmax=feature_max)
            test_feature = pd.DataFrame(self.test_feature, columns = data_variable_names)
            self.figure_report4 = correlation_analysis_survival(test_feature, is_train = False)
        print("remained feature numbers: %s" %len(self.data_variable_names))
        print("remained features: %s" %self.data_variable_names)

