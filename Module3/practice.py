# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」

password = 34

while True:
    data = input("請輸入1-100的數字")
    data = int(data) 
    if data > 100 or data < 1:
        print("超出範圍請重新輸入")
    elif data > password:
        print("請輸入更小的數字")
    elif data < password:
        print("請輸入更大的數字")
    else: 
        print("恭喜中獎")
        break
        












