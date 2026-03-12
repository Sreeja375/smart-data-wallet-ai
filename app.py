from data_wallet import DataWallet
from AI_prediction import DataPredictor

wallet = DataWallet()

wallet.add_usage(500)
wallet.add_usage(300)
wallet.add_usage(700)

print("Total Data Used:", wallet.total_usage())

predictor = DataPredictor()
predictor.train(wallet.daily_usage)

prediction = predictor.predict(4)

print("Predicted usage for next day:", prediction, "MB")