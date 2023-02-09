from Gujarat_Results_Comparison import BJP, INC, AAAP
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def test_BJP():
    x_BJP, y_BJP, statsmodels_results_BJP, y_hat_all_BJP, r_BJP, p_value_BJP = BJP()
    assert isinstance(x_BJP, pd.Series)
    assert isinstance(y_BJP, pd.Series)
    assert isinstance(statsmodels_results_BJP,
                      sm.regression.linear_model.RegressionResultsWrapper)
    assert isinstance(y_hat_all_BJP, np.ndarray)
    assert isinstance(r_BJP, float)
    assert isinstance(p_value_BJP, float)


def test_INC():
    x_INC, y_INC, statsmodels_results_INC, y_hat_all_INC, r_INC, p_value_INC = INC()
    assert isinstance(x_INC, pd.Series)
    assert isinstance(y_INC, pd.Series)
    assert isinstance(statsmodels_results_INC,
                      sm.regression.linear_model.RegressionResultsWrapper)
    assert isinstance(y_hat_all_INC, np.ndarray)
    assert isinstance(r_INC, float)
    assert isinstance(p_value_INC, float)


def test_AAAP():
    x_AAAP, y_AAAP, statsmodels_results_AAAP, y_hat_all_AAAP, r_AAP, p_value_AAP = AAAP()
    assert isinstance(x_AAAP, pd.Series)
    assert isinstance(y_AAAP, pd.Series)
    assert isinstance(statsmodels_results_AAAP,
                      sm.regression.linear_model.RegressionResultsWrapper)
    assert isinstance(y_hat_all_AAAP, np.ndarray)
    assert isinstance(r_AAP, float)
    assert isinstance(p_value_AAP, float)
