# a = input("请输入数字：")
# b = input("请输入数字：")
# c = a+b
# print("相加得到:" + c)



print("\n".join([''.join([('LangJins'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))