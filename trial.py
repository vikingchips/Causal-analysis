# pip install pycausalimpact
# pip install searchconsole

import pandas as pd 
 
X = pd.read_csv('Dates.csv')
y = pd.read_csv('Dates.csv')
 
# define metric that you want to test
# impressions, clicks, ctr
metric = 'Clicks'
 
# define intervention data
intervention = '2021-08-01'

from causalimpact import CausalImpact
 
def get_pre_post(data):
    """Get pre-post periods based on the intervention date
 
    Args:
        data (dataframe): df comming from create_master_df()
 
    Returns:
        tuple: tuple of lists showing index edges of period before and after intervention
    """       
    pre_start = min(data.index)
    pre_end = int(data[data['Date'] == intervention].index.values)
    post_start = pre_end + 1
    post_end = max(data.index)
 
    pre_period = [pre_start, pre_end] 
    post_period = [post_start, post_end]
    return pre_period, post_period
 
 
def make_report(data, pre_period, post_period):
    """Creates the built-in CausalImpact report
 
    Args:
        data (dataframe): df comming from create_master_df()
        pre_period (list): list coming from get_pre_post()
        post_period (list): list coming from get_pre_post()
    """       
    ci = CausalImpact(data.drop(['Date'], axis=1), pre_period, post_period)
    print(ci.summary())
    print(ci.summary(output='report'))
    ci.plot()
 
 
if __name__ == '__main__':
    y = y[['Date', metric]].rename(columns={metric:'y'})
    X = X[['Date', metric]].rename(columns={metric:'X'})
    data = y.merge(X, on='Date', how='left')
    data.sort_values(by='Date').reset_index(drop=True)
    pre_period, post_period = get_pre_post(data)
    make_report(data, pre_period, post_period)