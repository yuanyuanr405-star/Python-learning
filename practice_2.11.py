first_name="ren"
#用变量表示姓
last_name="yuanyuan"
#用变量表示名
full_name=f"{first_name} {last_name}"
#使用f方法，并使用变量表示全名
print(full_name)
#打印全名
print(full_name.title())
#打印首字母大写的全名
print(full_name.upper())
#打印大写的全名
print(full_name.lower())
#打印小写的全名
print(f"Hello,{full_name.title()}!")
#打印出：你好，Ren Yuanyuan!(首字母大写)
message=f"Hello,{full_name.title()}!"
#将这句话赋予一个变量
print(message)
#打印这个变量所代表的话