########
# script to run attribution example
########


import numpy as np
import pandas as pd
from factor_attribution_class import factorAttribution

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

