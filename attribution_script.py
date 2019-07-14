########
# script to run attribution example
########


import numpy as np
import pandas as pd

from factorAttribution.factor_attribution_class import factorAttribution

V = np.array([[0.0232, 0.0163, 0.0095],[0.0163, 0.2601, 0.0122],[0.0095, 0.0122, 0.0174]])

F = V

h = np.array([-0.3, 0.5, 0.8])

S = np.identity(3)

R = np.array([0.0604, 0.1795, 0.0419])

# what if we used col and row names?
########################
V = pd.DataFrame(V)

V.columns = ['X','Y','Z']
V.index = ['X','Y','Z']

h = pd.DataFrame(h)
h.index = ['X','Y','Z']

S = pd.DataFrame(np.identity(3))
S = pd.DataFrame(S)
S.index = ['X','Y','Z']
S.columns = ['S1','S2','S3']

R = pd.DataFrame(R)
R.index = ['X','Y','Z']

F = pd.DataFrame(F)
F.index = ['S1','S2','S3']
F.columns= ['S1','S2','S3']

factor_attrib = factorAttribution(V=np.array(V),
                         h=np.array(h),
                        F = np.array(F),
                         S=np.array(S),
                         R=np.array(R),
                                  list_factors=['S1', 'S2', 'S3'])
factor_attrib

###############
# importing risk model package

import pandas as pd

from riskModel.factor_risk_model import factor_risk_model

list_factors=['sector', 'momentum','quality','growth','vol','value','size']

df_new = pd.read_csv('stock_data_actual_dates.csv').iloc[:,1:]

#df_new = df_new.set_index('stock')
#dt_list = list(df_new.date.unique()[48:])

##########


model = factor_risk_model(df_new,
                          factor_portfolios = _factor_portfolios,
                          factor_returns = _factor_portfolio_returns,
                          specific_returns = _specific_returns,
                          all_factor_exposures = _all_factor_exposures)

model = factor_risk_model(df_new)
# this takes a few min
model.calc_factor_ports_and_returns(list_dates= None,
    list_factors=['sector', 'momentum','quality','growth','vol','value','size'])

model.calculate_factor_cov_matrix(window = 60)
model.calculate_stock_covariance_matrix()
model.calculate_FMPs()

dt = '2015-12-31'
model.all_FMPs[dt]
model.all_FMPs_using_V[dt]

model.all_FMPs[dt].sum(axis=0)

model.specific_returns

