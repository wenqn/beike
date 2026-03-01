import turtle
import math

# 初始化海龟
t = turtle.Turtle()
t.speed(10)  # 慢速，方便观察
screen = turtle.Screen()
screen.title("约瑟夫环暴力解法可视化")

# 绘制环形人物（n人围圈，半径150像素）
def draw_people(n, radius=150):
    """绘制n个圆形代表人物，标注编号"""
    people_pos = []  # 存储每个人的坐标，用于后续标注淘汰
    angle_step = 360 / n  # 每人之间的角度
    for i in range(n):
        # 计算坐标（极坐标转直角坐标）
        angle = i * angle_step
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        # 绘制圆形
        t.penup()
        t.goto(x, y - 20)  # 圆心下移20，让编号在圆上方
        t.pendown()
        t.circle(20)  # 人物圆形大小
        # 标注编号（日常计数：i+1）
        t.penup()
        t.goto(x, y + 10)
        t.write(i+1, align="center", font=("Arial", 12, "bold"))
        people_pos.append((x, y))
    return people_pos

# 模拟淘汰过程并可视化
def josephus_violent(n, m):
    people = list(range(n))  # 0~n-1表示n个人
    pos_list = draw_people(n)  # 绘制人物并获取坐标
    t.color("red")  # 淘汰标记为红色
    t.pensize(3)
    
    while len(people) > 1:
        # 计算淘汰索引
        index = (index + m - 1) % len(people) if len(people)!=n else (m-1)%n
        # 可视化淘汰：在对应位置画叉
        x, y = pos_list[people[index]]
        t.penup()
        t.goto(x - 15, y - 15)
        t.pendown()
        t.goto(x + 15, y + 15)
        t.goto(x - 15, y + 15)
        t.goto(x + 15, y - 15)
        # 删除淘汰的人
        del people[index]
        screen.update()
        turtle.delay(1000)  # 延迟1秒，观察过程
    
    # 标注幸存者
    survivor = people[0]
    x, y = pos_list[survivor]
    t.color("green")
    t.penup()
    t.goto(x, y - 30)
    t.write("幸存者", align="center", font=("Arial", 14, "bold"))
    return survivor + 1  # 转换为日常计数

# 主程序
n = 5  # 人数
m = 2  # 报数步长
index = 0  # 初始索引
survivor = josephus_violent(n, m)
print(f"{n}人围圈，报数到{m}淘汰，幸存者位置：{survivor}")
turtle.done()
