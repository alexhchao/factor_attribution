
# Custom Factor Risk and Return Attribution

## by Alex Chao

Package used to analyze a portfolio and run custom holdings-based factor attributions that calculates risk and return contributions. 

### Resources
- Active Portfolio Management, Grinold and Kahn, 2000
- Attribution, Grinold, 2006
- Made to Measure: Attribution, Deutsche Bank Quant Strategy, 2014

Lets start with the formula for our holdings (portfolio) decomposed into a factor component and residual portfolio

n = number of stocks
k = number of factors

h = portfolio holdings [n x 1]  
S = factor portfolios (FMPs) [n x k]     
B = portfolio factor exposures [k x 1]  
u = residual portfolio [n x 1]  
R = stock returns [n x 1]  

  
![first equation](https://latex.codecogs.com/gif.latex?h%20%3D%20S%20*%20B%20&plus;%20u)

assuming: 

![first equation](https://latex.codecogs.com/gif.latex?S%27%20V%20u%20%3D%200)  

hit equation with S' V

![first equation](https://latex.codecogs.com/gif.latex?S%27%20V%20h%20%3D%20S%20%27%20V%20S%20B%20&plus;%20S%27%20V%20u)  

![first equation](https://latex.codecogs.com/gif.latex?S%27%20V%20h%20%3D%20S%20%27%20V%20S%20B)  

#### Portfolio factor exposures (B) = 

![first equation](https://latex.codecogs.com/gif.latex?%28S%27%20V%20S%29%5E%7B-1%7DS%27%20V%20h)  

```python

```

### Risk Decomposition

Variance of the portfolio can be decomposed into variance from factors and from residuals

![first equation](https://latex.codecogs.com/gif.latex?h%27%20V%20h%20%3D%20h%27%20V%20S%20B%20&plus;%20h%27%20V%20u)    

Divide both sides by 
![first equation](https://latex.codecogs.com/gif.latex?%5Csqrt%7Bh%27Vh%7D)   

![first equation](https://latex.codecogs.com/gif.latex?%5Csqrt%7Bh%27Vh%7D%20%3D%20%5Cfrac%7Bh%27%20V%20S%20B%7D%7B%5Csqrt%7Bh%27Vh%7D%7D%20&plus;%20%5Cfrac%7Bh%27%20V%20u%7D%7B%5Csqrt%7Bh%27Vh%7D%7D)   

where portfolio risk = 
![first equation](https://latex.codecogs.com/gif.latex?%5Csqrt%7Bh%27Vh%7D)   

risk contribution from factors = 
![first equation](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bh%27%20V%20S%20B%7D%7B%5Csqrt%7Bh%27Vh%7D%7D)   

risk contribution from residuals = 
![first equation](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bh%27%20V%20u%7D%7B%5Csqrt%7Bh%27Vh%7D%7D)   

<!--- 
\frac{h' V S B}{\sqrt{h'Vh}} + \frac{h' V u}{\sqrt{h'Vh}} --->

```python

```

### Return contribution

return of the portfolio can be decomposed to return contribution from factors and residuals

![first equation](https://latex.codecogs.com/gif.latex?h%20%3D%20S%20*%20B%20&plus;%20u)  

hit with return (R)   

![first equation](https://latex.codecogs.com/gif.latex?h%27%20R%20%3D%20B%27%20S%27%20R%20&plus;%20u%27%20R)  

return contribution from factors =     
![first equation](https://latex.codecogs.com/gif.latex?B%27%20S%27%20R)  

return contribution from residuals =    
![first equation](https://latex.codecogs.com/gif.latex?u%27%20R)  


Import the factorAttribution class


```python

import os
import mpu

import numpy as np
import pandas as pd

from factorAttribution.factor_attribution_class import factorAttribution



```

Now lets test that the package is working as expected. Lets pretend our portfolio is the momentum factor mimicking portfolio. If our attribution is correct, it should have 100% risk / return contribution to momentum factor and 0 to all other factors.


```python
factor_model = mpu.io.read("data/factor_model_object.pickle")

factor_to_test = 'momentum'
dt = '2015-12-31'
V = factor_model.all_stock_covariance_mat[dt].copy()
F = factor_model.all_factor_covariance_mat[dt].copy()
S = factor_model.all_FMPs[dt].copy()
h = factor_model.all_FMPs[dt].loc[:,[factor_to_test]]
R = factor_model.df.reset_index().query(
    "date == @dt").set_index('stock').fwd_returns.loc[h.index].copy()*.01
F = S.T.dot(V).dot(S)

```


```python
factor_attrib = factorAttribution(V=np.array(V),
                         h=np.array(h),
                        F = np.array(F),
                         S=np.array(S),
                         R=R.reshape(575,1),
                                  list_factors=list(F.index))
factor_attrib


```

     n = 575 stocks, k = 16 factors


    /anaconda/lib/python3.6/site-packages/ipykernel/__main__.py:5: FutureWarning: reshape is deprecated and will raise in a subsequent release. Please use .values.reshape(...) instead





    
            factorAttribution class
            =======================
            Portfolio Variance = [[9.50254962e-05]]
    
            Exposures / Risk Contributions
            ==============================
                        port_factor_exposure  vol_adj_factor_exposure  \
    momentum            1.000000e+00             9.748102e-03   
    quality             5.551115e-16             3.341803e-18   
    growth             -1.332268e-15            -5.755048e-18   
    vol                -4.440892e-16            -6.996256e-18   
    value               1.110223e-15             7.968550e-18   
    ...                          ...                      ...   
    sector_5.0         -3.885781e-16            -1.692986e-17   
    sector_6.0          2.220446e-16             9.117568e-18   
    sector_7.0         -4.163336e-16            -1.599381e-17   
    sector_8.0         -1.387779e-17            -6.099662e-19   
    sector_9.0          2.220446e-16             8.494458e-18   
    
                risk_contrib_from_factors  risk_contrib_from_factors_pct  \
    momentum                 9.748102e-03                   1.000000e+00   
    quality                  9.951033e-20                   1.020817e-17   
    growth                  -4.480809e-19                  -4.596596e-17   
    vol                      3.335628e-18                   3.421823e-16   
    value                   -1.205426e-18                  -1.236575e-16   
    ...                               ...                            ...   
    sector_5.0               5.947306e-18                   6.100988e-16   
    sector_6.0              -2.709984e-18                  -2.780012e-16   
    sector_7.0               4.191410e-18                   4.299719e-16   
    sector_8.0               2.070302e-19                   2.123800e-17   
    sector_9.0              -1.602553e-18                  -1.643964e-16   
    
                return_contrib_from_factors  
    momentum                   1.004050e-02  
    quality                    6.085842e-19  
    growth                    -1.874248e-18  
    vol                        1.810498e-18  
    value                     -4.255040e-18  
    ...                                 ...  
    sector_5.0                 1.365673e-17  
    sector_6.0                 1.181791e-18  
    sector_7.0                -3.141411e-19  
    sector_8.0                 1.291511e-19  
    sector_9.0                 4.028263e-18  
    
    [16 rows x 5 columns]
            
            Risk Contributions
            ==================
            Portfolio Vol             = [[0.0097481]]
            Risk Contrib from Factors = 0.009748102182194641
            Risk Contrib from Resid   = [[1.52195232e-17]]
            
            Return Contributions
            ==================
            Portfolio Returns           = [0.0100405]
            Return Contrib from Factors = 0.010040504538319272
            Return Contrib from Resid   = [-1.83448945e-17]
            




```python

```
