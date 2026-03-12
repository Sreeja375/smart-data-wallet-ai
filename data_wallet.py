class DataWallet:
    def __init__(self):
        self.daily_usage = []

    def add_usage(self, data_mb):
        self.daily_usage.append(data_mb)

    def total_usage(self):
        return sum(self.daily_usage)

    def remaining_data(self, limit):
        return limit - self.total_usage()


# test example
if __name__ == "__main__":
    wallet = DataWallet()
    wallet.add_usage(500)
    wallet.add_usage(300)

    print("Total usage:", wallet.total_usage(), "MB")
    print("Remaining:", wallet.remaining_data(2000), "MB")