# You need to make sure you have installed pip
# Using pip, install pycausalimpact

import pandas as pd
from causalimpact import CausalImpact

data = pd.read_csv('Dates.csv',
                 usecols=[0,1], 
                 header=0,
                 encoding="utf-8-sig",
                 index_col='Date')

post_period = ["2021-12-07", "2021-08-13"]  # dates prior to change
pre_period = ["2022-08-14", "2022-07-21"] # dates after change

ci = CausalImpact(data['Clicks'], pre_period, post_period)

print(ci.summary())
ci.plot()
print(ci.summary(output='report'))