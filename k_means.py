# Determine K according to the value of silhouette (when the mutual information has real labels) or silhouette (disordered real labels), and obtain the predicted category yhat and the scores obtained when different K is obtained by the KMeans method
import numpy as np
import pandas as pd
import warnings
from sklearn.metrics import adjusted_mutual_info_score
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
import lifelines
from lifelines import CoxPHFitter
from lifelines import KaplanMeierFitter
from lifelines.plotting import add_at_risk_counts
from lifelines import utils
import matplotlib.pyplot as plt
import winreg
def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return (winreg.QueryValueEx(key, "Desktop")[0])


the_user_desktop = get_desktop()

def multivariate_logrank_test(yhat_final, time_cluster_label, duration_column="time", observed_column="status"):
    data_index = list(set(yhat_final.index) & set(time_cluster_label.index))
    log_rank_model = lifelines.statistics.multivariate_logrank_test(
        time_cluster_label.loc[data_index][duration_column],
        yhat_final.loc[data_index],
        time_cluster_label.loc[data_index][observed_column],
    )
    return round(log_rank_model.test_statistic, 3), round(log_rank_model.p_value, 3)



class K_Means_Class(object):
    def __init__(self, select_features_data):
        self.select_features_data = select_features_data   
        self.yhat_final = None  
        self.time_cluster_label = None   
        self.kmeans_scores = None  # Record the score of the sillute method
        self.test_statistic = 0.0
        self.p_value = 0.0
        self.median_survival_time = {}  # Store the median survival time in the form of a dictionary
        self.survival_rate_result = None
    
    def cluster(self,
                seed=1234,
                k=None,
                optimal_k_method="silhouette",
                ami_y=None,
                kmeans_kwargs=None):
        # Output data containing only filtered features
        z = self.select_features_data.drop(['times', 'status'], axis=1)
        # z = self.select_features_data[2:]
        if kmeans_kwargs is None:
            kmeans_kwargs = {"n_init": 1000, "n_jobs": 2}
        if k is not None:
            self.yhat_final1 = pd.Series(KMeans(k, **kmeans_kwargs, random_state=seed).fit_predict(z), index=z.index) 
            self.yhat_final1 = pd.DataFrame(self.yhat_final1)
            self.yhat_final1.columns = ['label']
            self.time_cluster_label = pd.DataFrame(
                pd.concat([self.select_features_data['times'], self.select_features_data['status'], self.yhat_final1],
                          axis=1))
            path = the_user_desktop + '\\user_set_time_label.csv'
            self.time_cluster_label.to_csv(path)
#             return self.yhat_final
        else:
            if optimal_k_method == "ami":
                ami_y = self.select_features_data['ami_label']
                z_to_use = z.loc[pd.DataFrame(ami_y).index]
                scorer = lambda yhat: adjusted_mutual_info_score(ami_y, yhat)

            elif optimal_k_method == "silhouette":
                z_to_use = z
                scorer = lambda yhat: silhouette_score(z_to_use, yhat)
            # Output the yhat results obtained by kmeans clustering when k is different
            yhats = {
                k: pd.Series(
                    KMeans(k, **kmeans_kwargs, random_state=seed).fit_predict(z_to_use),
                    index=z_to_use.index,
                )
                for k in range(3, 10)
            }

            # Output kmeans_scores scores when k is different (the higher the score, the better), the index is the value of k
            self.kmeans_scores = pd.Series(
                [scorer(yhats[k]) for k in range(3, 10)],
                index=range(3, 10),
                name=optimal_k_method,

            )
            self.kmeans_scores.index.name = "K"  
            optimal_k = np.argmax(self.kmeans_scores)  
            self.yhat_final2 = yhats[optimal_k]
            # Plot kmeans_scores (according to AMI mutual information)
            plt.plot(self.kmeans_scores)
            plt.ylabel("silhouette")
            plt.title("silhouette find K")
            plt.show()
            # return self.yhat_final, self.kmeans_scores
            # Survival analysis of the obtained tags
            self.yhat_final2 = pd.DataFrame(self.yhat_final2)
            self.yhat_final2.columns = ['label']
            self.time_cluster_label = pd.DataFrame(
                pd.concat([self.select_features_data['times'], self.select_features_data['status'], self.yhat_final2],
                          axis=1))
            path = the_user_desktop + '\\system_set_time_label.csv'
            self.time_cluster_label.to_csv(path)
        # return self.time_cluster_label

