import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import statistics
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

"D:\Ajay Maken Dropbox\Dropbox"

# Read CSV Files
guj_demog = pd.read_csv(
    r"D:\Dropbox\CS50 VS Code\src10 Project\AC wise Gujarat Demography.csv")
guj_AE_raw = pd.read_csv(
    r"D:\Dropbox\CS50 VS Code\src10 Project\TCPD_AE_Gujarat_2022-12-19.csv")
guj_AE_raw = guj_AE_raw[["Election_Type", "Assembly_No", "Constituency_No", "Year", "Position", "Candidate",
                         "Sex", "Party", "Votes", "Vote_Share_Percentage", "Candidate_Type", "Valid_Votes", "Electors", "Constituency_Name",
                         "Constituency_Type", "Sub_Region", "District_Name", "PC_Name", "PC_No"]]
guj_raw = pd.merge(guj_demog, guj_AE_raw, how='inner', on='Constituency_No')
print(guj_raw.shape)

year = int(input("For which year you want to compare?: "))
basis = input(
    "Amongst SC, ST, RURAL, URBAN; for which feauture you want regression analysis?: ")


def main():
    x_BJP, y_BJP, statsmodels_results_BJP, y_hat_all_BJP = BJP()
    x_INC, y_INC, statsmodels_results_INC, y_hat_all_INC = INC()
    x_AAAP, y_AAAP, statsmodels_results_AAAP, y_hat_all_AAAP = AAAP()
    print(statsmodels_results_BJP.summary())
    print(statsmodels_results_INC.summary())
    print(statsmodels_results_AAAP.summary())

    plt.scatter(x_INC, y_INC, color="red")
    plt.plot(x_INC, y_hat_all_INC, color="red")

    plt.scatter(x_BJP, y_BJP, color="blue")
    plt.plot(x_BJP, y_hat_all_BJP, color="blue")

    plt.scatter(x_AAAP, y_AAAP, color="green")
    plt.plot(x_AAAP, y_hat_all_AAAP, color="green")
    plt.show()

    print(
        f"rvalue for INC in RURAL = {math.sqrt(statsmodels_results_INC.rsquared):0.3}")
    print(
        f"rvalue for BJP in RURAL = {math.sqrt(statsmodels_results_BJP.rsquared):0.3}")
    print(
        f"rvalue for AAP in RURAL = {math.sqrt(statsmodels_results_AAAP.rsquared):0.3}")


def BJP():
    PARTY_BASIS_YEAR = year_party_basis(guj_raw, year, basis)
    # Filter the rows in column 'Party' only for 'BJP'
    PARTY_BASIS_YEAR = PARTY_BASIS_YEAR[(PARTY_BASIS_YEAR['Party'] == "BJP")]
    x_BJP = PARTY_BASIS_YEAR[basis]  # To return
    y_BJP = PARTY_BASIS_YEAR["Vote_Share_Percentage"]  # To return
    X_BJP = sm.add_constant(x_BJP)
    model_BJP = sm.OLS(y_BJP, X_BJP)
    statsmodels_results_BJP = model_BJP.fit()  # To return

    X_reshape_BJP = PARTY_BASIS_YEAR[basis].values
    y_reshape_BJP = PARTY_BASIS_YEAR["Vote_Share_Percentage"].values
    X_reshape_BJP = X_reshape_BJP.reshape(-1, 1)
    X_train_BJP, X_test_BJP, y_train_BJP, y_test_BJP = train_test_split(
        X_reshape_BJP, y_reshape_BJP, test_size=.2)
    reg_BJP = LinearRegression()
    reg_BJP.fit(X_train_BJP, y_train_BJP)
    y_hat_all_BJP = reg_BJP.predict(X_reshape_BJP)  # To return

    return x_BJP, y_BJP, statsmodels_results_BJP, y_hat_all_BJP


def INC():
    PARTY_BASIS_YEAR = year_party_basis(guj_raw, year, basis)
    # Filter the rows in column Party only for INC
    PARTY_BASIS_YEAR = PARTY_BASIS_YEAR[(PARTY_BASIS_YEAR['Party'] == "INC")]
    x_INC = PARTY_BASIS_YEAR[basis]  # To return
    y_INC = PARTY_BASIS_YEAR["Vote_Share_Percentage"]  # To return
    X_INC = sm.add_constant(x_INC)
    model_INC = sm.OLS(y_INC, X_INC)
    statsmodels_results_INC = model_INC.fit()  # To return

    X_reshape_INC = PARTY_BASIS_YEAR[basis].values
    y_reshape_INC = PARTY_BASIS_YEAR["Vote_Share_Percentage"].values
    X_reshape_INC = X_reshape_INC.reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(
        X_reshape_INC, y_reshape_INC, test_size=.2)
    reg_INC = LinearRegression()
    reg_INC.fit(X_train, y_train)
    y_hat_all_INC = reg_INC.predict(X_reshape_INC)  # To return

    return x_INC, y_INC, statsmodels_results_INC, y_hat_all_INC


def AAAP():
    PARTY_BASIS_YEAR = year_party_basis(guj_raw, year, basis)
    # Filter the rows in column 'Party' only for 'AAP'
    PARTY_BASIS_YEAR = PARTY_BASIS_YEAR[(PARTY_BASIS_YEAR['Party'] == "AAAP")]
    x_AAAP = PARTY_BASIS_YEAR[basis]  # To return
    y_AAAP = PARTY_BASIS_YEAR["Vote_Share_Percentage"]  # To return
    X_AAAP = sm.add_constant(x_AAAP)
    model_AAAP = sm.OLS(y_AAAP, X_AAAP)
    statsmodels_results_AAAP = model_AAAP.fit()  # To return

    X_reshape_AAAP = PARTY_BASIS_YEAR[basis].values
    y_reshape_AAAP = PARTY_BASIS_YEAR["Vote_Share_Percentage"].values
    X_reshape_AAAP = X_reshape_AAAP.reshape(-1, 1)
    X_train_AAAP, X_test_AAAP, y_train_AAAP, y_test_AAAP = train_test_split(
        X_reshape_AAAP, y_reshape_AAAP, test_size=.2)
    reg_AAAP = LinearRegression()
    reg_AAAP.fit(X_train_AAAP, y_train_AAAP)
    y_hat_all_AAAP = reg_AAAP.predict(X_reshape_AAAP)  # To return

    return x_AAAP, y_AAAP, statsmodels_results_AAAP, y_hat_all_AAAP


def year_party_basis(guj_raw, year, basis):
    # Filter the rows
    PARTY_BASIS_YEAR = guj_raw[(guj_raw['Year'] == year)]
    # Select the columns
    PARTY_BASIS_YEAR = PARTY_BASIS_YEAR[[
        "Party", "Vote_Share_Percentage", basis]]
    return PARTY_BASIS_YEAR


main()
