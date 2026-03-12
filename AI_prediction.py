import numpy as np
from sklearn.linear_model import LinearRegression


class DataPredictor:

    def __init__(self):
        self.model = LinearRegression()

    def train(self, usage_data):
        days = np.array(range(len(usage_data))).reshape(-1, 1)
        usage = np.array(usage_data)

        self.model.fit(days, usage)

    def predict(self, next_day):
        return self.model.predict([[next_day]])[0]