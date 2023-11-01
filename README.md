<img src="docs/_static/logo.png" align="right" />

# paramcheckup

<img srd="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"> <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white"> <img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white"> <img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black"> <img src="https://img.shields.io/badge/License-BSD%203--Clause-blue.svg">

This package has a collection of functions that check whether the parameter received by a function is of a certain type, returning ``True`` if the input is as expected or ``raising an error`` that indicates what the problem is.


<!-- 
## Install

> pip install paramcheckup



## Example


```python
import numpy as np
from scipy import stats
```

Assume a function ``t_test()`` that applies one sample Student's t test to compare means (two sided). This function receives three parameters, which are ``x_data``, ``mu`` and ``alpha``.

```python
def t_test(x_data, mu, alpha):
    
    tcalc = (x_data.mean() - mu)*np.sqrt(x_data)/(x_data.std(ddof=1))
    t_critical = stats.t.ppf(1-alpha/2, x_data.size - 1)
    p_value = (1 - stats.t.cdf(np.abs(tcalc), x_data.size - 1))*2
    if p_value < alpha:
        conclusion = "Reject H0"
    else:
        conclusion = "Fail to reject H0"
    return tcalc, t_critical, p_value, conclusion
```

The ``t_test`` function strongly depends on the ``x_data`` parameter being a one-dimensional numpy array. The ``types.is_numpy(value, param_name, func_name)`` function checks this is True:



```python
from paramcheckup import types
def t_test(x_data, mu, alpha):
    types.is_numpy(x_data, "x_data", "t_test")
    
    tcalc = (x_data.mean() - mu)*np.sqrt(x_data)/(x_data.std(ddof=1))
    t_critical = stats.t.ppf(1-alpha/2, x_data.size - 1)
    p_value = (1 - stats.t.cdf(np.abs(tcalc), x_data.size - 1))*2
    if p_value < alpha:
        conclusion = "Reject H0"
    else:
        conclusion = "Fail to reject H0"
    return tcalc, t_critical, p_value, conclusion
```

If we use the function passing a ``list`` instead of a ``NumpyArray``, an ``TypeError`` error will be raised informing the user what the error is:
 -->



## License

- [BSD 3-Clause License]("https://github.com/puzzle-in-a-mug/paramcheckup/blob/main/LICENSE")




