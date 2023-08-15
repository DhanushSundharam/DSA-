from sklearn.linear_model import LinearRegression
import numpy as np


features = np.array([[1000], [2000], [3000], [4000], [8000]])


prices = np.array([6200000, 6430000, 6745000, 7100000, 8200000])


model = LinearRegression()


model.fit(features, prices)


new_feature = np.array([[6000]])

predicted_price = model.predict(new_feature)

print("Predicted price for a house with 6000 square feet: %.f" % predicted_price)
