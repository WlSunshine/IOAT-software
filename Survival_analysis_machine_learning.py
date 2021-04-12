# -*- coding: utf-8 -*-
import tempfile
import winreg
import rpy2.robjects as robjects
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dirname = tempfile.TemporaryDirectory()
def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return(winreg.QueryValueEx(key, "Desktop")[0])
# The output results are divided into two cases: whether there is a test set or not
def multivariate_cox_analysis_survival(data_path, data_path_test = None, whether_test = False, seed = 1234):
    r = robjects.r
    multivariate_cox_result_path = "\\".join([dirname.name, "multivariate_cox_result_path.csv"])
    c_index_path = "\\".join([dirname.name, "c_index.csv"])
    linear_predictor_path = "\\".join([dirname.name, "linear_predictor_path.csv"])
    cross_validation_path = "\\".join([dirname.name, "cross_validation.csv"])
    r('''
    library(survival)
    library(caret)
    ''')
    r('''
    import_to_r <- function(data_path_r, multivariate_cox_result_path_r, c_index_path_r, linear_predictor_path_r, seed_r, cross_validation_path_r){
            data_path <<- data_path_r
            multivariate_cox_result_path <<- multivariate_cox_result_path_r
            c_index_path <<- c_index_path_r
            linear_predictor_path <<- linear_predictor_path_r
            seed <<- seed_r
            cross_validation_path <<- cross_validation_path_r
            }
    ''')
    
    r['import_to_r'](data_path, multivariate_cox_result_path, c_index_path, linear_predictor_path, seed, cross_validation_path)
    
    r('''
    data <- read.csv(data_path, header = TRUE, sep = ",")
    
    f <- coxph(Surv(time, status) ~ ., data)
    f2 <- summary(f)
    f3 <- data.frame(f2$coefficients)
    write.csv(f3, multivariate_cox_result_path)
    c_index_total <- survConcordance(Surv(time, status) ~ predict(f), data)
    c_index <- c_index_total$concordance
    c_index_se <- c_index_total$std.err
    c_index_export <- data.frame(c_index, c_index_se)
    write.csv(c_index_export, c_index_path)
    linear_predictors <- f$linear.predictors
    write.csv(linear_predictors, linear_predictor_path, row.names = FALSE)
    # Cross-validation
    set.seed(seed)
    cross_result <- c()
    folds <- createFolds(y = 1:dim(data)[1], k = 5)
    i = 1
    while (i <= 5){
        cross_index_test <- folds[[i]]
        cross_data_train <- data[-cross_index_test,]
        cross_data_test <- data[cross_index_test,]
        cross_f <- coxph(Surv(time, status)~., cross_data_train)
        cross_c_index_test_total <- survConcordance(Surv(time, status) ~ predict(cross_f, newdata = cross_data_test), cross_data_test)
        cross_c_index_test <- cross_c_index_test_total$concordance
        cross_result[i] <- cross_c_index_test
        i = i + 1
    }
    write.csv(cross_result, cross_validation_path, sep = ",")
    ''')
    # When there is a test set
    if whether_test:
        c_index_path_test = "\\".join([dirname.name, "c_index_test.csv"])
        linear_predictor_path_test = "\\".join([dirname.name, "linear_predictor_path_test.csv"])
        r('''
        import_to_r <- function(data_path_test_r, c_index_path_test_r, linear_predictor_path_test_r){
                data_path_test <<- data_path_test_r
                c_index_path_test <<- c_index_path_test_r
                linear_predictor_path_test <<- linear_predictor_path_test_r
                }
        ''')
        r["import_to_r"](data_path_test, c_index_path_test, linear_predictor_path_test)
        r('''
        data_test <- read.csv(data_path_test, header = TRUE, sep = ",")
        c_index_total_test <- survConcordance(Surv(time, status) ~ predict(f, newdata = data_test), data_test)
        c_index_test <- c_index_total_test$concordance
        c_index_se_test <- c_index_total_test$std.err
        c_index_export_test <- data.frame(c_index_test, c_index_se_test)
        write.csv(c_index_export_test, c_index_path_test)
        linear_predictors_test <- as.vector(predict(f, data_test))
        write.csv(linear_predictors_test, linear_predictor_path_test, row.names = FALSE)
        ''')
    if not whether_test:
        return(multivariate_cox_result_path, c_index_path, linear_predictor_path, cross_validation_path)
    else:
        return(multivariate_cox_result_path, c_index_path, linear_predictor_path, c_index_path_test, linear_predictor_path_test, cross_validation_path)
def Get_cross_validation(cross_validation_path):
    cross_validation = pd.read_csv(cross_validation_path)
    cross_validation_value = cross_validation.values
    cross_validation_mean = cross_validation.mean()
    return(cross_validation_value, cross_validation_mean)
def Nomogram_figure_survival(data_path, time_point1, time_point2 = False):
    if time_point2 == False:
        time_point2 = "False"
    Your_desktop = get_desktop()
    nomogram_figure_filename = "\\".join([Your_desktop, "".join(["nomogram", str(time.time()), "figure.eps"])])
    r = robjects.r
    r('''
    library(rms)
    library(survival)
    library(stringr)
    ''')
    r('''
    import_to_r <- function(data_path_r, nomogram_figure_filename_r, time_point1_r, time_point2_r){
            data_path <<- data_path_r
            nomogram_figure_filename <<- nomogram_figure_filename_r
            time_point1 <<- time_point1_r
            time_point2 <<- time_point2_r
            }
    ''')
    r['import_to_r'](data_path, nomogram_figure_filename, time_point1, time_point2)
    r('''
    data <- read.csv(data_path, header = TRUE, sep = ",")
    
    valname_for_nomogram <- function(valname_){
            valname <- str_extract_all(valname_, "[A-Z|_][a-z0-9]*", simplify = TRUE)
            val0 <- ""
            val1 <- ""
            val2 <- ""
            val3 <- ""
            for (i in 1:length(valname)){
                    val0 <- paste(val0, valname[i], sep="")
                    if (str_length(val0) <= 18){
                            val1 <- paste(val1, valname[i], sep="")
                    }else if ((str_length(val0)-str_length(val1)) <= 18){
                            val2 <- paste(val2, valname[i], sep="")
                    }else{
                            val3 <- paste(val3, valname[i], sep="")
                    }
             }
             valname <- paste(val1, "\n", val2, "\n", val3, sep="")
             if (valname == "NA\n\n"){
                     valname <- valname_}
             return(valname)
             }
    for (i in 2:length(colnames(data))){
        colnames(data)[i] <- valname_for_nomogram(colnames(data)[i])
        }
    ddist <- datadist(data)
    options(datadist = "ddist")
    f <- cph(Surv(time, status) ~ ., data = data, x = TRUE, y = TRUE, surv = TRUE)
    if (time_point2 != "False"){
        surv <- Survival(f)
        survival1 <- function(x)surv(time_point1, x)
        survival2 <- function(x)surv(time_point2, x)
        survival_time_name1 <- paste(time_point1, "month survival")
        survival_time_name2 <- paste(time_point2, "month survival")
        nom <- nomogram(f, fun = list(survival1, survival2), fun.at = seq(0.0, 1.0, by = 0.2), lp = F, funlabel = c(survival_time_name1, survival_time_name2))
        bitmap(file=nomogram_figure_filename, res=500)
        par(cex = 1.5)
        plot(nom, cex.axis = 0.6, cex.var = 0.75, xfrac = 0.4)
        dev.off()
    }else{
        surv <- Survival(f)
        survival1 <- function(x)surv(time_point1, x)
        survival_time_name1 <- paste(time_point1, "month survival")
        
        nom <- nomogram(f, fun = list(survival1), fun.at = seq(0.0, 1.0, by = 0.2), lp = F, funlabel = c(survival_time_name1))
        bitmap(file=nomogram_figure_filename, res=500)
        par(cex = 1.5)
        plot(nom, cex.axis = 0.6, cex.var = 0.75, xfrac = 0.4)
        dev.off()
    }
    ''')
    return(nomogram_figure_filename)
def calibrate_figure_from_R_survival(train_data_path, test_data_path = False, time_point = 12):
    r = robjects.r
    r('''
    library(survival)
    library(riskRegression)
    ''')
    r('''
    calibration_curve_data <- function(train_data_path, train_data_export_path, test_data_path = FALSE, test_data_export_path = FALSE, time_point){
      # Survival Analysis Model
      train_data <- read.csv(train_data_path)
      f <- coxph(Surv(time, status) ~ ., x = TRUE, y = TRUE, train_data) 
      ### Calibration curve data on the training set
      # Divide patients into 3 groups according to the prognostic index
      train_predict_value <- as.array(predict(f, train_data))
      train_predict_value_rank <- ifelse(train_predict_value <= quantile(train_predict_value, probs = seq(0, 1, 0.333))[2], "1", ifelse(
        train_predict_value <= quantile(train_predict_value, probs = seq(0, 1, 0.333))[3], "2", ifelse(
          train_predict_value <= max(train_predict_value), "3")))
      train_data <- cbind(train_data, train_predict_value_rank)
      train_data_1 <- train_data[train_data$train_predict_value_rank == "1", ]
      train_data_2 <- train_data[train_data$train_predict_value_rank == "2", ]
      train_data_3 <- train_data[train_data$train_predict_value_rank == "3", ]
      # Calculate the predicted survival rate of each group
      train_data_1_predict_mean <- mean(predictCoxPL(f, times = time_point, newdata = train_data_1)$survival)
      train_data_2_predict_mean <- mean(predictCoxPL(f, times = time_point, newdata = train_data_2)$survival)
      train_data_3_predict_mean <- mean(predictCoxPL(f, times = time_point, newdata = train_data_3)$survival)
      train_data_predict_mean <- c(train_data_1_predict_mean, train_data_2_predict_mean, train_data_3_predict_mean)
      # Calculate the Kaplan_Meier survival rate of each group
      kaplan_meier_1 <- survfit(Surv(time, status) ~ train_predict_value_rank, train_data_1)
      train_data_1_kaplan_meier <- kaplan_meier_1$surv[kaplan_meier_1$time == time_point]
      i <- time_point - 1
      while (i > 0){
          if (length(train_data_1_kaplan_meier) == 0){
              train_data_1_kaplan_meier <- kaplan_meier_1$surv[kaplan_meier_1$time == i]}
          i <- i - 1
      }
      if (length(train_data_1_kaplan_meier) == 0){
        train_data_1_kaplan_meier <- 1.0
      }
      kaplan_meier_2 <- survfit(Surv(time, status) ~ train_predict_value_rank, train_data_2)
      train_data_2_kaplan_meier <- kaplan_meier_2$surv[kaplan_meier_2$time == time_point]
      i <- time_point - 1
      while (i > 0){
          if (length(train_data_2_kaplan_meier) == 0){
              train_data_2_kaplan_meier <- kaplan_meier_2$surv[kaplan_meier_2$time == i]}
          i <- i - 1
      }
      if (length(train_data_2_kaplan_meier) == 0){
        train_data_2_kaplan_meier <- 1.0
      }
      kaplan_meier_3 <- survfit(Surv(time, status) ~ train_predict_value_rank, train_data_3)
      train_data_3_kaplan_meier <- kaplan_meier_3$surv[kaplan_meier_3$time == time_point]
      i <- time_point - 1
      while (i > 0){
          if (length(train_data_3_kaplan_meier) == 0){
              train_data_3_kaplan_meier <- kaplan_meier_3$surv[kaplan_meier_3$time == i]}
          i <- i - 1
      }
      if (length(train_data_3_kaplan_meier) == 0){
        train_data_3_kaplan_meier <- 1.0
      }
      train_data_kaplan_meier <- c(train_data_1_kaplan_meier, train_data_2_kaplan_meier, train_data_3_kaplan_meier)

      train_data_export <- data.frame(train_data_predict_mean, train_data_kaplan_meier)
      write.csv(train_data_export, train_data_export_path, row.names = FALSE)
      if(test_data_path != FALSE){
        test_data <- read.csv(test_data_path)
        
        test_predict_value <- as.array(predict(f, test_data))
        test_predict_value_rank <- ifelse(test_predict_value <= quantile(test_predict_value, probs = seq(0, 1, 0.333))[2], "1", ifelse(
          test_predict_value <= quantile(test_predict_value, probs = seq(0, 1, 0.333))[3], "2", ifelse(
            test_predict_value <= max(test_predict_value), "3")))
        test_data <- cbind(test_data, test_predict_value_rank)
        test_data_1 <- test_data[test_data$test_predict_value_rank == "1", ]
        test_data_2 <- test_data[test_data$test_predict_value_rank == "2", ]
        test_data_3 <- test_data[test_data$test_predict_value_rank == "3", ]
        # Calculate the predicted survival rate of each group
        test_data_1_predict_mean <- mean(predictCoxPL(f, times = time_point, newdata = test_data_1)$survival)
        test_data_2_predict_mean <- mean(predictCoxPL(f, times = time_point, newdata = test_data_2)$survival)
        test_data_3_predict_mean <- mean(predictCoxPL(f, times = time_point, newdata = test_data_3)$survival)
        test_data_predict_mean = c(test_data_1_predict_mean, test_data_2_predict_mean, test_data_3_predict_mean)
        # Calculate the Kaplan_Meier survival rate of each group
        kaplan_meier_1 <- survfit(Surv(time, status) ~ test_predict_value_rank, test_data_1)
        test_data_1_kaplan_meier <- kaplan_meier_1$surv[kaplan_meier_1$time == time_point]
        i <- time_point - 1
        while (i > 0){
            if (length(test_data_1_kaplan_meier) == 0){
                test_data_1_kaplan_meier <- kaplan_meier_1$surv[kaplan_meier_1$time == i]}
            i <- i - 1
        }
        if (length(test_data_1_kaplan_meier) == 0){
          test_data_1_kaplan_meier <- 1.0
        }
        kaplan_meier_2 <- survfit(Surv(time, status) ~ test_predict_value_rank, test_data_2)
        test_data_2_kaplan_meier <- kaplan_meier_2$surv[kaplan_meier_2$time == time_point]
        i <- time_point - 1
        while (i > 0){
            if (length(test_data_2_kaplan_meier) == 0){
                test_data_2_kaplan_meier <- kaplan_meier_2$surv[kaplan_meier_2$time == i]}
            i <- i - 1
        }
        if (length(test_data_2_kaplan_meier) == 0){
          test_data_2_kaplan_meier <- 1.0
        }
        kaplan_meier_3 <- survfit(Surv(time, status) ~ test_predict_value_rank, test_data_3)
        test_data_3_kaplan_meier <- kaplan_meier_3$surv[kaplan_meier_3$time == time_point]
        i <- time_point - 1
        while (i > 0){
            if (length(test_data_3_kaplan_meier) == 0){
                test_data_3_kaplan_meier <- kaplan_meier_3$surv[kaplan_meier_3$time == i]}
            i <- i - 1
        }
        if (length(test_data_3_kaplan_meier) == 0){
          test_data_3_kaplan_meier <- 1.0
        }
        test_data_kaplan_meier <- c(test_data_1_kaplan_meier, test_data_2_kaplan_meier, test_data_3_kaplan_meier)
        # Data_frame output on the training set
        test_data_export <- data.frame(test_data_predict_mean, test_data_kaplan_meier)
        write.csv(test_data_export, test_data_export_path, row.names = FALSE)
      }
    }
    ''')
    if test_data_path == False:
        train_calibrate_figure_data_path = "\\".join([dirname.name, "".join([str(time.time()), "train_calibrate_figure_data_path.csv"])])
    else:
        train_calibrate_figure_data_path = "\\".join([dirname.name, "".join([str(time.time()), "train_calibrate_figure_data_path.csv"])])
        test_calibrate_figure_data_path = "\\".join([dirname.name, "".join([str(time.time()), "test_calibrate_figure_data_path.csv"])])
    r('''
    train_import_to_r <- function(train_data_path_r, train_calibrate_figure_data_path_r, time_point_r){
            train_data_path <<- train_data_path_r
            train_calibrate_figure_data_path <<- train_calibrate_figure_data_path_r
            time_point <<- time_point_r
            }
    ''')
    r('''
    test_import_to_r <- function(test_data_path_r, test_calibrate_figure_data_path_r, time_point_r){
            test_data_path <<- test_data_path_r
            test_calibrate_figure_data_path <<- test_calibrate_figure_data_path_r
            time_point <<- time_point_r
            }
    ''')
    if test_data_path == False:
        r['train_import_to_r'](train_data_path, train_calibrate_figure_data_path, time_point)
    else:
        r['train_import_to_r'](train_data_path, train_calibrate_figure_data_path, time_point)
        r['test_import_to_r'](test_data_path, test_calibrate_figure_data_path, time_point)
    if test_data_path == False:
        r('''
        calibration_curve_data(train_data_path, train_calibrate_figure_data_path, test_data_path = FALSE, test_data_export_path = FALSE, time_point)
        ''')
        return(train_calibrate_figure_data_path)
    else:
        r('''
        calibration_curve_data(train_data_path, train_calibrate_figure_data_path, test_data_path = test_data_path, test_data_export_path = test_calibrate_figure_data_path, time_point)
        ''')
        return(train_calibrate_figure_data_path, test_calibrate_figure_data_path)

def tdROC_from_R_survival(data_path1, data_path2, time_point_1 = 12, time_point_2 = False):
    if time_point_2 == False:
        tdROC_data_path = "\\".join([dirname.name, "tdROC_data_path.csv"])
        tdROC_AUC_path = "\\".join([dirname.name, "tdROC_AUC_path.csv"])
        r = robjects.r
        r('''
        import_to_r <- function(data_path1_r, data_path2_r, tdROC_data_path_r, tdROC_AUC_path_r, time_point_1_r){
                data_path1 <<- data_path1_r
                data_path2 <<- data_path2_r
                tdROC_data_path <<- tdROC_data_path_r
                tdROC_AUC_path <<- tdROC_AUC_path_r
                time_point_1 <<- time_point_1_r
                }
        ''')
        r['import_to_r'](data_path1, data_path2, tdROC_data_path, tdROC_AUC_path, time_point_1)
        r('''
        library(tdROC)
        ''')
        r('''
        mydata1 <- read.csv(data_path1)
        mydata2 <- read.csv(data_path2)
        my_tdROC <- tdROC(X = as.matrix(mydata1[1]), Y = as.matrix(mydata2[1]), delta = as.matrix(mydata2[2]), tau = time_point_1)
        write.csv(my_tdROC$ROC, tdROC_data_path)
        write.csv(my_tdROC$AUC, tdROC_AUC_path)
        ''')
        return(tdROC_data_path, tdROC_AUC_path)
    else:
        # Output time_point_1 information
        tdROC_data_path = "\\".join([dirname.name, "td_ROC_data_path.csv"])
        tdROC_AUC_path = "\\".join([dirname.name, "tdROC_AUC_path.csv"])
        r = robjects.r
        r('''
        import_to_r <- function(data_path1_r, data_path2_r, tdROC_data_path_r, tdROC_AUC_path_r, time_point_1_r){
                data_path1 <<- data_path1_r
                data_path2 <<- data_path2_r
                tdROC_data_path <<- tdROC_data_path_r
                tdROC_AUC_path <<- tdROC_AUC_path_r
                time_point_1 <<- time_point_1_r
                }
        ''')
        r['import_to_r'](data_path1, data_path2, tdROC_data_path, tdROC_AUC_path, time_point_1)
        r('''
        library(tdROC)
        ''')
        r('''
        mydata1 <- read.csv(data_path1)
        mydata2 <- read.csv(data_path2)
        my_tdROC <- tdROC(X = as.matrix(mydata1[1]), Y = as.matrix(mydata2[1]), delta = as.matrix(mydata2[2]), tau = time_point_1)
        write.csv(my_tdROC$ROC, tdROC_data_path)
        write.csv(my_tdROC$AUC, tdROC_AUC_path)
        ''')
        # Output time_point_2 information
        tdROC_data_path_time_point_2 = "\\".join([dirname.name, "td_ROC_data_path_time_point_2.csv"])
        tdROC_AUC_path_time_point_2 = "\\".join([dirname.name, "tdROC_AUC_path_time_point_2.csv"])
        r = robjects.r
        r('''
        import_to_r <- function(data_path1_r, data_path2_r, tdROC_data_path_r_time_point_2, tdROC_AUC_path_r_time_point_2, time_point_2_r){
                data_path1_time <<- data_path1_r
                data_path2_time <<- data_path2_r
                tdROC_data_path_time_point_2 <<- tdROC_data_path_r_time_point_2
                tdROC_AUC_path_time_point_2 <<- tdROC_AUC_path_r_time_point_2
                time_point_2 <<- time_point_2_r
                }
        ''')
        r['import_to_r'](data_path1, data_path2, tdROC_data_path_time_point_2, tdROC_AUC_path_time_point_2, time_point_2)
        r('''
        library(tdROC)
        ''')
        r('''
        mydata1 <- read.csv(data_path1)
        mydata2 <- read.csv(data_path2)
        my_tdROC <- tdROC(X = as.matrix(mydata1[1]), Y = as.matrix(mydata2[1]), delta = as.matrix(mydata2[2]), tau = time_point_2)
        write.csv(my_tdROC$ROC, tdROC_data_path_time_point_2)
        write.csv(my_tdROC$AUC, tdROC_AUC_path_time_point_2)
        ''')
        return(tdROC_data_path, tdROC_AUC_path, tdROC_data_path_time_point_2, tdROC_AUC_path_time_point_2)
def calibrate_figure_survival(train_data_path, test_data_path = False, time_point1 = 12, time_point2 = False, label1 = "calibrate plot", label2 = False):
    calibrate_figure1 = "\\".join([dirname.name, "".join([str(time.time()), "figure.png"])])
    time.sleep(1)
    calibrate_figure2 = "\\".join([dirname.name, "".join([str(time.time()), "figure.png"])])
    
    
    if time_point2 == False:
        if test_data_path == False:
        
            train_calibrate_figure_data_path_time_point1_path = calibrate_figure_from_R_survival(train_data_path, test_data_path, time_point = time_point1)
            
            train_calibrate_figure_data_path_time_point1 = pd.read_csv(train_calibrate_figure_data_path_time_point1_path)
            train_calibrate_figure_data_path_time_point1_value = train_calibrate_figure_data_path_time_point1.values
            plt.figure()
            plt.plot([0,1], [0,1], linestyle = "--", color = "k", alpha = 0.5)
            plt.plot(train_calibrate_figure_data_path_time_point1_value[:, 0], train_calibrate_figure_data_path_time_point1_value[:, 1], marker = "o", label = "time: %s" %time_point1)
            plt.title(label1)
            plt.xlabel("Predicted probability")
            plt.ylabel("KM probability")
            plt.legend(loc = "lower right")
            plt.savefig(calibrate_figure1, dpi=500)
            plt.show()
        else:
            train_calibrate_figure_data_path_time_point1_path, test_calibrate_figure_data_path_time_point1_path = calibrate_figure_from_R_survival(train_data_path, test_data_path, time_point = time_point1)
            train_calibrate_figure_data_path_time_point1 = pd.read_csv(train_calibrate_figure_data_path_time_point1_path)
            train_calibrate_figure_data_path_time_point1_value = train_calibrate_figure_data_path_time_point1.values
            plt.figure()
            plt.plot([0,1], [0,1], linestyle = "--", color = "k", alpha = 0.5)
            plt.plot(train_calibrate_figure_data_path_time_point1_value[:, 0], train_calibrate_figure_data_path_time_point1_value[:, 1], marker = "o", label = "time: %s" %time_point1)
            plt.title(label1)
            plt.xlabel("Predicted probability")
            plt.ylabel("KM probability")
            plt.legend(loc = "lower right")
            plt.savefig(calibrate_figure1, dpi=500)
            plt.show()
            test_calibrate_figure_data_path_time_point1 = pd.read_csv(test_calibrate_figure_data_path_time_point1_path)
            test_calibrate_figure_data_path_time_point1_value = test_calibrate_figure_data_path_time_point1.values
            plt.figure()
            plt.plot([0,1], [0,1], linestyle = "--", color = "k", alpha = 0.5)
            plt.plot(test_calibrate_figure_data_path_time_point1_value[:, 0], test_calibrate_figure_data_path_time_point1_value[:, 1], marker = "o", label = "time: %s" %time_point1)
            plt.title(label2)
            plt.xlabel("Predicted probability")
            plt.ylabel("KM probability")
            plt.legend(loc = "lower right")
            plt.savefig(calibrate_figure2, dpi=500)
            plt.show()
    else:
        if test_data_path == False:
            train_calibrate_figure_data_path_time_point1_path = calibrate_figure_from_R_survival(train_data_path, test_data_path, time_point = time_point1)
            train_calibrate_figure_data_path_time_point2_path = calibrate_figure_from_R_survival(train_data_path, test_data_path, time_point = time_point2)
            train_calibrate_figure_data_path_time_point1 = pd.read_csv(train_calibrate_figure_data_path_time_point1_path)
            train_calibrate_figure_data_path_time_point2 = pd.read_csv(train_calibrate_figure_data_path_time_point2_path)
            train_calibrate_figure_data_path_time_point1_value = train_calibrate_figure_data_path_time_point1.values
            train_calibrate_figure_data_path_time_point2_value = train_calibrate_figure_data_path_time_point2.values
            plt.figure()
            plt.plot([0,1], [0,1], linestyle = "--", color = "k", alpha = 0.5)
            plt.plot(train_calibrate_figure_data_path_time_point1_value[:, 0], train_calibrate_figure_data_path_time_point1_value[:, 1], marker = "o", label = "time: %s" %time_point1)
            plt.plot(train_calibrate_figure_data_path_time_point2_value[:, 0], train_calibrate_figure_data_path_time_point2_value[:, 1], marker = "o", label = "time: %s" %time_point2)
            plt.title(label1)
            plt.xlabel("Predicted probability")
            plt.ylabel("KM probability")
            plt.legend(loc = "lower right")
            plt.savefig(calibrate_figure1, dpi=500)
            plt.show()
        else:
            train_calibrate_figure_data_path_time_point1_path, test_calibrate_figure_data_path_time_point1_path = calibrate_figure_from_R_survival(train_data_path, test_data_path, time_point = time_point1)
            train_calibrate_figure_data_path_time_point2_path, test_calibrate_figure_data_path_time_point2_path = calibrate_figure_from_R_survival(train_data_path, test_data_path, time_point = time_point2)
            train_calibrate_figure_data_path_time_point1 = pd.read_csv(train_calibrate_figure_data_path_time_point1_path)
            train_calibrate_figure_data_path_time_point2 = pd.read_csv(train_calibrate_figure_data_path_time_point2_path)
            train_calibrate_figure_data_path_time_point1_value = train_calibrate_figure_data_path_time_point1.values
            train_calibrate_figure_data_path_time_point2_value = train_calibrate_figure_data_path_time_point2.values
            plt.figure()
            plt.plot([0,1], [0,1], linestyle = "--", color = "k", alpha = 0.5)
            plt.plot(train_calibrate_figure_data_path_time_point1_value[:, 0], train_calibrate_figure_data_path_time_point1_value[:, 1], marker = "o", label = "time: %s" %time_point1)
            plt.plot(train_calibrate_figure_data_path_time_point2_value[:, 0], train_calibrate_figure_data_path_time_point2_value[:, 1], marker = "o", label = "time: %s" %time_point2)
            plt.title(label1)
            plt.xlabel("Predicted probability")
            plt.ylabel("KM probability")
            plt.legend(loc = "lower right")
            plt.savefig(calibrate_figure1, dpi=500)
            plt.show()
            test_calibrate_figure_data_path_time_point1 = pd.read_csv(test_calibrate_figure_data_path_time_point1_path)
            test_calibrate_figure_data_path_time_point2 = pd.read_csv(test_calibrate_figure_data_path_time_point2_path)
            test_calibrate_figure_data_path_time_point1_value = test_calibrate_figure_data_path_time_point1.values
            test_calibrate_figure_data_path_time_point2_value = test_calibrate_figure_data_path_time_point2.values
            plt.figure()
            plt.plot([0,1], [0,1], linestyle = "--", color = "k", alpha = 0.5)
            plt.plot(test_calibrate_figure_data_path_time_point1_value[:, 0], test_calibrate_figure_data_path_time_point1_value[:, 1], marker = "o", label = "time: %s" %time_point1)
            plt.plot(test_calibrate_figure_data_path_time_point2_value[:, 0], test_calibrate_figure_data_path_time_point2_value[:, 1], marker = "o", label = "time: %s" %time_point2)
            plt.title(label2)
            plt.xlabel("Predicted probability")
            plt.ylabel("KM probability")
            plt.legend(loc = "lower right")
            plt.savefig(calibrate_figure2, dpi=500)
            plt.show()
    return(calibrate_figure1, calibrate_figure2)
def tdROC_survival(train_data_path1, train_data_path2, test_data_path1 = False, test_data_path2 = False, time_point_1 = 12, time_point_2 = False, figure_label1 = "tdROC", figure_label2 = False):
    tdROC_figure1 = "\\".join([dirname.name, "".join([str(time.time()), "figure.png"])])
    time.sleep(1)
    tdROC_figure2 = "\\".join([dirname.name, "".join([str(time.time()), "figure.png"])])
    if time_point_2 == False:
        if test_data_path1 == False:
            train_tdROC_path_time_point_1, train_tdAUC_path_time_point_1 = tdROC_from_R_survival(train_data_path1, train_data_path2, time_point_1 = time_point_1, time_point_2 = time_point_2)
            train_tdROC_time_point_1 = pd.read_csv(train_tdROC_path_time_point_1)
            train_tdAUC_time_point_1 = pd.read_csv(train_tdAUC_path_time_point_1)
            train_tdAUC_value_time_point_1 = train_tdAUC_time_point_1.values[0, 1]
            train_sens_time_point_1 = train_tdROC_time_point_1.values[:, 2]
            train_spec_time_point_1 = train_tdROC_time_point_1.values[:, 3]
            x_standard = [0, 1]
            y_standard = [0, 1]
            plt.figure()
            plt.plot(x_standard, y_standard, linestyle = "--", color = "k", alpha = 0.5)
            plt.plot(1-train_spec_time_point_1, train_sens_time_point_1, label='AUC = %0.3f (time: %s)' %(train_tdAUC_value_time_point_1, time_point_1))
            plt.title(figure_label1)
            plt.xlabel("1 - spec")
            plt.ylabel("sens")
            plt.legend(loc = "lower right")
            plt.savefig(tdROC_figure1, dpi=500)
            plt.show()
        else:
            # The situation on the training set
            train_tdROC_path_time_point_1, train_tdAUC_path_time_point_1 = tdROC_from_R_survival(train_data_path1, train_data_path2, time_point_1 = time_point_1, time_point_2= time_point_2)
            train_tdROC_time_point_1 = pd.read_csv(train_tdROC_path_time_point_1)
            train_tdAUC_time_point_1 = pd.read_csv(train_tdAUC_path_time_point_1)
            train_tdAUC_value_time_point_1 = train_tdAUC_time_point_1.values[0, 1]
            train_sens_time_point_1 = train_tdROC_time_point_1.values[:, 2]
            train_spec_time_point_1 = train_tdROC_time_point_1.values[:, 3]
            x_standard = [0, 1]
            y_standard = [0, 1]
            plt.figure()
            plt.plot(x_standard, y_standard, linestyle = "--", color = "k", alpha = 0.5)
            plt.plot(1-train_spec_time_point_1, train_sens_time_point_1, label='AUC = %0.3f (time: %s)' %(train_tdAUC_value_time_point_1, time_point_1))
            plt.title(figure_label1)
            plt.xlabel("1 - spec")
            plt.ylabel("sens")
            plt.legend(loc = "lower right")
            plt.savefig(tdROC_figure1, dpi=500)
            plt.show()
            # The situation on the test set
            test_tdROC_path_time_point_1, test_tdAUC_path_time_point_1 = tdROC_from_R_survival(test_data_path1, test_data_path2, time_point_1 = time_point_1, time_point_2 = time_point_2)
            test_tdROC_time_point_1 = pd.read_csv(test_tdROC_path_time_point_1)
            test_tdAUC_time_point_1 = pd.read_csv(test_tdAUC_path_time_point_1)
            test_tdAUC_value_time_point_1 = test_tdAUC_time_point_1.values[0, 1]
            test_sens_time_point_1 = test_tdROC_time_point_1.values[:, 2]
            test_spec_time_point_1 = test_tdROC_time_point_1.values[:, 3]
            x_standard = [0, 1]
            y_standard = [0, 1]
            plt.figure()
            plt.plot(x_standard, y_standard, linestyle = "--", color = "k", alpha = 0.5)
            plt.plot(1-test_spec_time_point_1, test_sens_time_point_1, label='AUC = %0.3f (time: %s)' %(test_tdAUC_value_time_point_1, time_point_1))
            plt.title(figure_label2)
            plt.xlabel("1 - spec")
            plt.ylabel("sens")
            plt.legend(loc = "lower right")
            plt.savefig(tdROC_figure2, dpi=500)
            plt.show()
    else: # time_pint_2 != False
        if test_data_path1 == False:
            train_tdROC_path_time_point_1, train_tdAUC_path_time_point_1, train_tdROC_path_time_point_2, train_tdAUC_path_time_point_2 = tdROC_from_R_survival(train_data_path1, train_data_path2, time_point_1 = time_point_1, time_point_2 = time_point_2)
            train_tdROC_time_point_1 = pd.read_csv(train_tdROC_path_time_point_1)
            train_tdAUC_time_point_1 = pd.read_csv(train_tdAUC_path_time_point_1)
            train_tdAUC_value_time_point_1 = train_tdAUC_time_point_1.values[0, 1]
            train_sens_time_point_1 = train_tdROC_time_point_1.values[:, 2]
            train_spec_time_point_1 = train_tdROC_time_point_1.values[:, 3]
            train_tdROC_time_point_2 = pd.read_csv(train_tdROC_path_time_point_2)
            train_tdAUC_time_point_2 = pd.read_csv(train_tdAUC_path_time_point_2)
            train_tdAUC_value_time_point_2 = train_tdAUC_time_point_2.values[0, 1]
            train_sens_time_point_2 = train_tdROC_time_point_2.values[:, 2]
            train_spec_time_point_2 = train_tdROC_time_point_2.values[:, 3]
            x_standard = [0, 1]
            y_standard = [0, 1]
            plt.figure()
            plt.plot(x_standard, y_standard, linestyle = "--", color = "k", alpha = 0.5)
            plt.plot(1-train_spec_time_point_1, train_sens_time_point_1, label='AUC = %0.3f (time: %s)' %(train_tdAUC_value_time_point_1, time_point_1))
            plt.plot(1-train_spec_time_point_2, train_sens_time_point_2, label='AUC = %0.3f (time: %s)' %(train_tdAUC_value_time_point_2, time_point_2))
            plt.title(figure_label1)
            plt.xlabel("1 - spec")
            plt.ylabel("sens")
            plt.legend(loc = "lower right")
            plt.savefig(tdROC_figure1, dpi=500)
            plt.show()
        else:
            # The situation on the training set
            train_tdROC_path_time_point_1, train_tdAUC_path_time_point_1, train_tdROC_path_time_point_2, train_tdAUC_path_time_point_2 = tdROC_from_R_survival(train_data_path1, train_data_path2, time_point_1 = time_point_1, time_point_2 = time_point_2)
            train_tdROC_time_point_1 = pd.read_csv(train_tdROC_path_time_point_1)
            train_tdAUC_time_point_1 = pd.read_csv(train_tdAUC_path_time_point_1)
            train_tdAUC_value_time_point_1 = train_tdAUC_time_point_1.values[0, 1]
            train_sens_time_point_1 = train_tdROC_time_point_1.values[:, 2]
            train_spec_time_point_1 = train_tdROC_time_point_1.values[:, 3]
            train_tdROC_time_point_2 = pd.read_csv(train_tdROC_path_time_point_2)
            train_tdAUC_time_point_2 = pd.read_csv(train_tdAUC_path_time_point_2)
            train_tdAUC_value_time_point_2 = train_tdAUC_time_point_2.values[0, 1]
            train_sens_time_point_2 = train_tdROC_time_point_2.values[:, 2]
            train_spec_time_point_2 = train_tdROC_time_point_2.values[:, 3]
            x_standard = [0, 1]
            y_standard = [0, 1]
            plt.figure()
            plt.plot(x_standard, y_standard, linestyle = "--", color = "k", alpha = 0.5)
            plt.plot(1-train_spec_time_point_1, train_sens_time_point_1, label='AUC = %0.3f (time: %s)' %(train_tdAUC_value_time_point_1, time_point_1))
            plt.plot(1-train_spec_time_point_2, train_sens_time_point_2, label='AUC = %0.3f (time: %s)' %(train_tdAUC_value_time_point_2, time_point_2))
            plt.title(figure_label1)
            plt.xlabel("1 - spec")
            plt.ylabel("sens")
            plt.legend(loc = "lower right")
            plt.savefig(tdROC_figure1, dpi=500)
            plt.show()
            # The situation on the test set
            test_tdROC_path_time_point_1, test_tdAUC_path_time_point_1, test_tdROC_path_time_point_2, test_tdAUC_path_time_point_2 = tdROC_from_R_survival(test_data_path1, test_data_path2, time_point_1 = time_point_1, time_point_2 = time_point_2)
            test_tdROC_time_point_1 = pd.read_csv(test_tdROC_path_time_point_1)
            test_tdAUC_time_point_1 = pd.read_csv(test_tdAUC_path_time_point_1)
            test_tdAUC_value_time_point_1 = test_tdAUC_time_point_1.values[0, 1]
            test_sens_time_point_1 = test_tdROC_time_point_1.values[:, 2]
            test_spec_time_point_1 = test_tdROC_time_point_1.values[:, 3]
            test_tdROC_time_point_2 = pd.read_csv(test_tdROC_path_time_point_2)
            test_tdAUC_time_point_2 = pd.read_csv(test_tdAUC_path_time_point_2)
            test_tdAUC_value_time_point_2 = test_tdAUC_time_point_2.values[0, 1]
            test_sens_time_point_2 = test_tdROC_time_point_2.values[:, 2]
            test_spec_time_point_2 = test_tdROC_time_point_2.values[:, 3]
            x_standard = [0, 1]
            y_standard = [0, 1]
            plt.figure()
            plt.plot(x_standard, y_standard, linestyle = "--", color = "k", alpha = 0.5)
            plt.plot(1-test_spec_time_point_1, test_sens_time_point_1, label='AUC = %0.3f (time: %s)' %(test_tdAUC_value_time_point_1, time_point_1))
            plt.plot(1-test_spec_time_point_2, test_sens_time_point_2, label='AUC = %0.3f (time: %s)' %(test_tdAUC_value_time_point_2, time_point_2))
            plt.title(figure_label2)
            plt.xlabel("1 - spec")
            plt.ylabel("sens")
            plt.legend(loc = "lower right")
            plt.savefig(tdROC_figure2, dpi=500)
            plt.show()
    return(tdROC_figure1, tdROC_figure2)
def get_multivariate_result_from_csv_survival(data_path):
    result = pd.read_csv(data_path)
    result.columns = ['variable', 'coef', 'HR', 'coef se', 'z', 'P']
    return(result)
def get_c_index_from_csv_survival(data_path):
    result = pd.read_csv(data_path)
    c_index = result.values[0, 1]
    c_index_se = result.values[0, 2]
    return({"c-index": c_index, "95% CI of c-index": (c_index-(1.96*c_index_se), c_index+(1.96*c_index_se))})
class Data_analysis_survival(object):
    def __init__(self, train_feature, train_time_status, test_feature, test_time_status, data_variable_names, whether_test, seed, cross):
        self.train_feature = train_feature
        self.train_time_status = train_time_status
        self.test_feature = test_feature
        self.test_time_status = test_time_status
        self.data_variable_names = data_variable_names
        self.whether_test = whether_test
        self.seed = seed
        self.cross = cross
    def multivariate_analysis(self, Nomo = False, time_point1 = False, time_point2 = False, figure_label1 = None, figure_label2 = None):
        print("starting...")
        time.sleep(3)
        train_data = np.concatenate((self.train_time_status, self.train_feature), axis = 1)
        train_data = pd.DataFrame(train_data, columns = ["time", "status"] + list(self.data_variable_names))
        train_data_path = "\\".join([dirname.name, "".join([str(time.time()), "train_data_path.csv"])])
        train_data.to_csv(train_data_path, index = False)
        if self.whether_test == True:
            test_data = np.concatenate((self.test_time_status, self.test_feature), axis = 1)
            test_data = pd.DataFrame(test_data, columns = ["time", "status"] + list(self.data_variable_names))
            test_data_path = "\\".join([dirname.name, "".join([str(time.time()), "test_data_path.csv"])])
            test_data.to_csv(test_data_path, index = False)
        # cox result
        if self.whether_test == False:
            multivariate_result_path, train_c_index_path, train_linear_predictor_path, cross_validation_path = multivariate_cox_analysis_survival(data_path = train_data_path, data_path_test = None, whether_test = self.whether_test, seed = self.seed)
            self.train_multivariate_result = get_multivariate_result_from_csv_survival(multivariate_result_path)
            self.train_c_index = get_c_index_from_csv_survival(train_c_index_path)
            print("Drawing figures...")
            time.sleep(5)
            # calibrate figure
            self.calibrate_figure1, self.calibrate_figure2 = calibrate_figure_survival(train_data_path = train_data_path, test_data_path = False, time_point1 = time_point1, time_point2 = time_point2, label1 = figure_label1, label2 = figure_label2)
            # tdROC
            self.tdROC_figure1, self.tdROC_figure2 = tdROC_survival(train_data_path1 = train_linear_predictor_path, train_data_path2 = train_data_path, test_data_path1 = False, test_data_path2 = False, time_point_1 = time_point1, time_point_2 = time_point2, figure_label1 = figure_label1, figure_label2 = figure_label2)
            self.cross_validation_value, self.cross_validation_mean = Get_cross_validation(cross_validation_path)
        else:
            multivariate_result_path, train_c_index_path, train_linear_predictor_path, test_c_index_path, test_linear_predictor_path, cross_validation_path = multivariate_cox_analysis_survival(data_path = train_data_path, data_path_test = test_data_path, whether_test = self.whether_test, seed = self.seed)
            self.train_multivariate_result = get_multivariate_result_from_csv_survival(multivariate_result_path)
            self.train_c_index = get_c_index_from_csv_survival(train_c_index_path)
            self.test_c_index = get_c_index_from_csv_survival(test_c_index_path)
            print("Drawing figures...")
            time.sleep(5)
            # calibrate figure
            self.calibrate_figure1, self.calibrate_figure2 = calibrate_figure_survival(train_data_path = train_data_path, test_data_path = test_data_path, time_point1 = time_point1, time_point2 = time_point2, label1 = figure_label1, label2 = figure_label2)
            # tdROC
            self.tdROC_figure1, self.tdROC_figure2 = tdROC_survival(train_data_path1 = train_linear_predictor_path, train_data_path2 = train_data_path, test_data_path1 = test_linear_predictor_path, test_data_path2 = test_data_path, time_point_1 = time_point1, time_point_2 = time_point2, figure_label1 = figure_label1, figure_label2 = figure_label2)
            self.cross_validation_value, self.cross_validation_mean = Get_cross_validation(cross_validation_path)
        # Nomogram
        if Nomo == True:
            self.Nomogram_figure = Nomogram_figure_survival(train_data_path, time_point1, time_point2)
            print("【Note】The nomogram is exported to the desktop.")
        else:
            self.Nomogram_figure = None
        print("【Note】The model information:")
        if self.cross:
            print("【Note】 The cross validation results:")
            print("each-cross c-index: %s" %list(self.cross_validation_value.T[1]))
            print("mean-cross c-index: %s" %list(self.cross_validation_mean)[1])
        print("Multivariate result:")
        print(self.train_multivariate_result)
        print("Training data c_index:")
        print(self.train_c_index)
        if self.whether_test == True:
            print("Testing data c_index:")
            print(self.test_c_index)
if __name__ == "__main__":
    model = Data_analysis_survival(myfeature.train_feature, myfeature.train_time_status, myfeature.test_feature, myfeature.test_time_status, myfeature.data_variable_names, True)
    model.multivariate_analysis(Nomo = False, time_point1 = 6, time_point2 = False, figure_label1 = "train_data", figure_label2 = "test_data")
    model.train_multivariate_result
    model.train_c_index
    model.test_c_index



    
    
