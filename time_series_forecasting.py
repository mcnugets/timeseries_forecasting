import pandas as pd
from matplotlib import pyplot
from sklearn.linear_model import LinearRegression
import numpy as np




def make_prediction():
    np.random.seed(42)
    date = pd.date_range(start='01/09/2025', periods=30)
    date = np.arange(len(date)).reshape(-1,1)
    test_date_nums = np.arange(30, 35).reshape(-1, 1)

    objects_per_day = np.random.poisson(lam=50, size=30) 
    
    
    # linear regression
    lr = LinearRegression()
    reg = lr.fit(X=date, y=objects_per_day) 

    # score = reg.score()
    result = reg.predict(test_date_nums)
    # LR visualisation

    # history
    pyplot.scatter(date, objects_per_day, color='black', label='history') 
  
    # prediction
 
    pyplot.plot(test_date_nums, result, color='red', linewidth=3, label='prediction')
    pyplot.xlabel('Date')
    pyplot.ylabel('Number of Objects')
    pyplot.legend()
    pyplot.savefig('time_series_forecast.png')  
    print("Plot saved as 'time_series_forecast.png'")

    pyplot.close()




