# 計算幾次方
def pow(x, y):
    return x ** y
# 折扣方案
def get_discount(total):
    if total >= 2000:
        total -= 200*(total/2000)
    return total

# 測試模組
if __name__ == "__main__": #不等於主程式，所以到時候不會列印出來
    print(f"myModule.py - function pow的結果: {pow(2,3)}")
    print(f"myModule.py - function pow的結果: {get_discount(6000)}元")

