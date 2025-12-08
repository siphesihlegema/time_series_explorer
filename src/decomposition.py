from statsmodels.tsa.seasonal import seasonal_decompose
import pandas as pd

class ClassicalDecomposition:
    def __init__(self, series: pd.Series, model: str = 'multiplicative', freq: int = None):
        """
        Initialize the decomposition class.

        Args:
            series (pd.Series): Time series to decompose.
            model (str): 'additive' or 'multiplicative'.
            freq (int): Seasonal frequency. If None, statsmodels tries to infer it.
        """
        self.series = series
        self.model = model
        self.freq = freq
        self.decomposition = seasonal_decompose(self.series, model=self.model, period=self.freq)
    
    @property
    def trend(self):
        return self.decomposition.trend
    
    @property
    def seasonal(self):
        return self.decomposition.seasonal
    
    @property
    def residual(self):
        return self.decomposition.resid
