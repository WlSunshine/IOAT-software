from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import lifelines
from lifelines import CoxPHFitter  
from lifelines import KaplanMeierFitter
from lifelines.plotting import add_at_risk_counts
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Calculate the multivariate log-rank test-whether the survival analysis is different
def multivariate_logrank_test(data_df, labels):
    log_rank_model = lifelines.statistics.multivariate_logrank_test(
        data_df['times'],
        labels,
        data_df['status']
    )
    return round(log_rank_model.test_statistic, 3), round(log_rank_model.p_value, 3)


class Survival_Curve_class():
    def __init__(self, duration_column='times', observed_column='status'):
        # self.path = None
        self.duration_column = duration_column
        self.observed_column = observed_column

        self.data_df = None
        self.survival_label = None

        self.test_statistic = 0.0  # Survival difference stat value of each group (value in survival curve)
        self.p_value = 0.0  # Survival difference p value of each group (value in survival curve)
        self.median_survival_time = {}  # Store the median survival time in the form of a dictionary
        self.survival_rate_result = None  # Store survival rate results between different groups (different months)

        self.cox_report_for_HR = None  # Output the HR value of Cox-PH pair after grouping
        self.HR = 0.0  # Get HR risk rate
        self.CI = []  # Get confidence interval

    def read_data_cox(self, path):
        self.data_df = pd.DataFrame(pd.read_csv(path))
        self.survival_label = pd.DataFrame(pd.concat(
            [self.data_df[self.duration_column], self.data_df[self.observed_column], self.data_df['label']],
            axis=1))

    # Survival curve
    def estimate_kaplan_meier(self):
        labels = self.survival_label['label']  # Convert the DataFrame format of data_label to Series format
        sfs = {}
        # Draw a survival curve
        # plt.figure(1)
        ax = plt.subplot()
        fitter = []

        for label in sorted(labels.unique()):
            data_label_index = list(set(labels[labels == label].index) & set(self.survival_label.index))
            kmf = KaplanMeierFitter()
            kmf.fit(
                self.survival_label.loc[data_label_index][self.duration_column],
                self.survival_label.loc[data_label_index][self.observed_column],
                label=label
            )
            # Put each trained kmf into the fitter and store it to draw the number of survivors corresponding to the time for each label
            fitter.append(kmf)

            sfs[label] = kmf.survival_function_  # Get the survival rate of each label
            self.median_survival_time[label] = kmf.median_

            ax = kmf.plot(ax=ax)  # Draw a survival curve

        # Draw the number of survivors corresponding to the time
        add_at_risk_counts(*fitter)
        # Calculate the log_rank value to see if the survival difference of the group is significant
        self.test_statistic, self.p_value = multivariate_logrank_test(self.survival_label, labels)
        if self.p_value == 0:
            self.p_value = '< 0.0001'
            p_transform = True
        else:
            self.p_value = str(self.p_value)
            p_transform = False
        # Output the survival rate of all groups
        self.survival_rate_result = pd.concat([sfs[k] for k in list(sorted(labels.unique()))], axis=1).interpolate()
        if len(self.CI) > 0:
            # Show the p value in log_rank in the figure
            if p_transform == False:
                ax.text(0.35, 0.8, 'log_rank p=%s' % self.p_value, transform=ax.transAxes, va='top', fontsize=12)
                ax.text(0.35, 0.9, "HR=%.3f(95%% CI:%.3f-%.3f)" % (self.HR, self.CI[0], self.CI[1]), transform=ax.transAxes,
                        va='top', fontsize=12)
            else:
                ax.text(0.35, 0.8, 'log_rank p %s' % self.p_value, transform=ax.transAxes, va='top', fontsize=12)
                ax.text(0.35, 0.9, "HR=%.3f(95%% CI:%.3f-%.3f)" % (self.HR, self.CI[0], self.CI[1]), transform=ax.transAxes,
                        va='top', fontsize=12)
        else:
            # Show the p value in log_rank in the figure
            ax.text(0.35, 0.8, 'log_rank p=%s' % self.p_value, transform=ax.transAxes, va='top', fontsize=12)
        plt.title('Full Data')
        print("Median survival time of data: %s" %self.median_survival_time)
        plt.show()

    #         return test_statistic, p_value, median_survival_time, survival_rate_result

    # The Cox-PH model calculates HR values and confidence intervals based on known groups as features (total data with labels)
    def Cox_Label_HR(self):
        cph = CoxPHFitter()
        try:
            cph.fit(self.survival_label, self.duration_column, event_col=self.observed_column)
            self.cox_report_for_HR = cph.print_summary()
            self.HR = cph.hazard_ratios_[0]
            self.CI = cph.confidence_intervals_.values[0]
        #         return cph.print_summary()
        except:
            print("The truncation has problem. ")
