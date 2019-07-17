
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


```python

```

### Now translate this into Python code:


```python

import numpy as np
import pandas as pd
from factor_attribution_class import factorAttribution

V = np.array([[0.0232, 0.0163, 0.0095],[0.0163, 0.2601, 0.0122],[0.0095, 0.0122, 0.0174]])

F = V

h = np.array([-0.3, 0.5, 0.8])

S = np.identity(3)

R = np.array([0.0604, 0.1795, 0.0419])

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
```


```python
S
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>S1</th>
      <th>S2</th>
      <th>S3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>X</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>Y</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>Z</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
V
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>X</th>
      <td>0.0232</td>
      <td>0.0163</td>
      <td>0.0095</td>
    </tr>
    <tr>
      <th>Y</th>
      <td>0.0163</td>
      <td>0.2601</td>
      <td>0.0122</td>
    </tr>
    <tr>
      <th>Z</th>
      <td>0.0095</td>
      <td>0.0122</td>
      <td>0.0174</td>
    </tr>
  </tbody>
</table>
</div>




```python
h
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>X</th>
      <td>-0.3</td>
    </tr>
    <tr>
      <th>Y</th>
      <td>0.5</td>
    </tr>
    <tr>
      <th>Z</th>
      <td>0.8</td>
    </tr>
  </tbody>
</table>
</div>




```python
S
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>S1</th>
      <th>S2</th>
      <th>S3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>X</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>Y</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>Z</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
R
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>X</th>
      <td>0.0604</td>
    </tr>
    <tr>
      <th>Y</th>
      <td>0.1795</td>
    </tr>
    <tr>
      <th>Z</th>
      <td>0.0419</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

### Custom Factor Attribution class


```python

factor_attrib = factorAttribution(V=np.array(V),
                         h=np.array(h),
                        F = np.array(F),
                         S=np.array(S),
                         R=np.array(R),
                                  list_factors=['S1', 'S2', 'S3'])
factor_attrib
```

     n = 3 stocks, k = 3 factors





    
            factorAttribution class
            =======================
            Portfolio Variance = [[0.078559]]
    
            Exposures / Risk Contributions
            ==============================
                port_factor_exposure  vol_adj_factor_exposure  risk_contrib_from_factors  \
    S1                  -0.3                -0.045695                  -0.009408   
    S2                   0.5                 0.255000                   0.240685   
    S3                   0.8                 0.105527                   0.049007   
    
        risk_contrib_from_factors_pct  return_contrib_from_factors  
    S1                      -0.033567                     -0.01812  
    S2                       0.858718                      0.08975  
    S3                       0.174849                      0.03352  
            
            Risk Contributions
            ==================
            Portfolio Vol             = [[0.28028378]]
            Risk Contrib from Factors = 0.2802837847610882
            Risk Contrib from Resid   = [[-3.31937467e-18]]
            
            Return Contributions
            ==================
            Portfolio Returns           = [0.10515]
            Return Contrib from Factors = 0.10515
            Return Contrib from Resid   = [2.0539126e-18]
            




```python

```


```python
B = np.linalg.inv(S.T.dot(V).dot(S)).dot(S.T.dot(V).dot(h))
print(B)
```

    [[-0.3]
     [ 0.5]
     [ 0.8]]



```python

```


```python

```


```python

```


```python

```
