
class Hero():
    name = "雷神"
    age = 200
    skill = "神罗天征"

    def talk(self):
        print("爆炸就是艺术！")

    def game(self,words):
        print("陷阵杀{}".format(words))
        return "一马当先"


p = Hero()
# print(p.name)
# print(p.age)
# print(p.skill)

# p.talk()
a = p.game("敌")
print(a)