import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import statistics as st

year = int(input("2017 or 2022, for which Assembly Elections you want to analyse?: "))
basis = input(
    "Amongst SC, ST, RURAL, URBAN; for which feauture you want regression analysis?: ")


def main():
    x_BJP, y_BJP, statsmodels_results_BJP, y_hat_all_BJP, r_BJP, p_value_BJP = BJP()
    x_INC, y_INC, statsmodels_results_INC, y_hat_all_INC, r_INC, p_value_INC = INC()
    x_AAAP, y_AAAP, statsmodels_results_AAAP, y_hat_all_AAAP, r_AAP, p_value_AAP = AAAP()
    BJP_Avg = st.mean(y_BJP)
    INC_Avg = st.mean(y_INC)
    AAP_Avg = st.mean(y_AAAP)
    print(statsmodels_results_BJP.summary())
    print(statsmodels_results_INC.summary())
    print(statsmodels_results_AAAP.summary())

    print(
        f"BJP Avg Votes % = {BJP_Avg:0.4}; Pearson Coefficient r for BJP in {basis} = {r_BJP:0.3} BJP p-Value in {basis} = {p_value_BJP:0.5}")
    print(
        f"INC Avg Votes % = {INC_Avg:0.4}; Pearson Coefficient r for INC in {basis} = {r_INC:0.3} INC p-Value in {basis} = {p_value_INC:0.5}")
    print(
        f"AAP Avg Votes % = {AAP_Avg:0.4}; Pearson Coefficient r for AAP in {basis} = {r_AAP:0.3} AAP p-Value in {basis} = {p_value_AAP:0.5}")
   

    plt.scatter(x_INC, y_INC, color="blue", label = y_INC)
    plt.plot(x_INC, y_hat_all_INC, color="blue")

    plt.scatter(x_BJP, y_BJP, color="orange", label = y_BJP)
    plt.plot(x_BJP, y_hat_all_BJP, color="orange")

    plt.scatter(x_AAAP, y_AAAP, color="black", label = y_AAAP)
    plt.plot(x_AAAP, y_hat_all_AAAP, color="black")
    plt.title(f"Regression Analysis for {year} Legislative Assembly Elections\n of BJP, INC and APP \n on {basis}% of votes in each AC")
    plt.xlabel(f"{basis}% of Votes in each Assembly Constituency")
    plt.ylabel(f"Party % of Votes in each Assembly Constituency")
    plt.text(
        10, 80, f"BJP-Orange, INC-Blue, AAP-Black\nBJP Avg Vote % = {BJP_Avg:0.4}\nINC Avg Votes % = {INC_Avg:0.4}\nAAP Avg Votes % = {AAP_Avg:0.4}")
    plt.text(
        10,70,f"For BJP r={r_BJP:0.3} & p-Value={p_value_BJP:0.5}\nFor INC r={r_INC:0.3} & p-Value={p_value_INC:0.5}\nFor AAP r={r_AAP:0.3} & p-Value={p_value_AAP:0.5}")
    plt.show()

    

def BJP():
    PARTY_BASIS_YEAR = year_party_basis(year, basis)
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
    pearson_BJP = stats.pearsonr(PARTY_BASIS_YEAR[basis], PARTY_BASIS_YEAR["Vote_Share_Percentage"])
    r_BJP, p_value_BJP = pearson_BJP

    return x_BJP, y_BJP, statsmodels_results_BJP, y_hat_all_BJP, r_BJP, p_value_BJP


def INC():
    PARTY_BASIS_YEAR = year_party_basis(year, basis)
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
    pearson_INC = stats.pearsonr(
        PARTY_BASIS_YEAR[basis], PARTY_BASIS_YEAR["Vote_Share_Percentage"])
    r_INC, p_value_INC = pearson_INC

    return x_INC, y_INC, statsmodels_results_INC, y_hat_all_INC, r_INC, p_value_INC


def AAAP():
    PARTY_BASIS_YEAR = year_party_basis(year, basis)
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
    pearson_AAP = stats.pearsonr(
        PARTY_BASIS_YEAR[basis], PARTY_BASIS_YEAR["Vote_Share_Percentage"])
    r_AAP, p_value_AAP = pearson_AAP
    return x_AAAP, y_AAAP, statsmodels_results_AAAP, y_hat_all_AAAP, r_AAP, p_value_AAP


def year_party_basis(year, basis):
    """
    This function uses two publicly available data files. The first one is demographic mapping 
    of Gujarat AC and the second one is data of all Assembly Elections in Gujarat.
    """
    # Read CSV Files
    guj_demog = pd.read_csv(
        r"D:\Dropbox\CS50 VS Code\src10 Project\AC wise Gujarat Demography.csv")
    guj_AE_raw = pd.read_csv(
        r"D:\Dropbox\CS50 VS Code\src10 Project\TCPD_AE_Gujarat_2022-12-19.csv")
    guj_AE_raw = guj_AE_raw[["Constituency_No", "Year", "Party", "Vote_Share_Percentage" ]]
    guj_raw = pd.merge(guj_demog, guj_AE_raw, how='inner', on='Constituency_No')
    print(guj_raw.shape)
    # Filter the rows
    PARTY_BASIS_YEAR = guj_raw[(guj_raw['Year'] == year)]
    # Select the columns
    PARTY_BASIS_YEAR = PARTY_BASIS_YEAR[[
        "Party", "Vote_Share_Percentage", basis]]
    return PARTY_BASIS_YEAR

if __name__ == "__main__":
    main()
