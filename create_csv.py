import csv

# 准备数据，数据以列表的列表形式呈现，每个子列表代表一行数据
data = [
    ["姓名", "成绩"],
    ["张三", 85],
    ["李四", 90],
    ["王五", 78]
]

# 打开文件，以写入模式，newline=''是为了避免在Windows系统中出现额外的空行
with open('example.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # 逐行写入数据
    for row in data:
        writer.writerow(row)

print("CSV文件已成功创建！")