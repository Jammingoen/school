import pandas as pd

전_values =input("전 측정값: ")
전_list = [int(value) for value in 전_values.split()]

후_values = input("후 측정값: ")
후_list = [int(value) for value in 후_values.split()]

data = {
    
    "전": 전_list,
    "후": 후_list,
}

df = pd.DataFrame(data)

df["전후 변화량"] = df["후"] - df["전"]

average_change = df["전후 변화량"].mean()

print("입력된 '전' 값", 전_list)
print("입력된 '후' 값", 후_list)
print(f"전후 변화량의 평균: {average_change}")
