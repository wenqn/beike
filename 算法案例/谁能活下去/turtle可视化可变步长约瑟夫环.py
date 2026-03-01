import turtle
import time
import math

# 可变步长的暴力解法（拓展版）
def josephus_variable_step(n, steps):
    """
    n: 人数
    steps: 步长列表，steps[i]表示第i+1轮的报数步长
    """
    people = list(range(n))
    index = 0
    # 初始化turtle
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.title("可变步长约瑟夫环可视化")
    t.speed(1)
    pos_list = draw_people(n)  # 复用第1课的draw_people函数
    
    while len(people) > 1:
        # 取当前轮次的步长（超出列表则用最后一个步长）
        round_num = n - len(people) + 1
        m = steps[round_num-1] if round_num-1 < len(steps) else steps[-1]
        # 计算淘汰索引
        index = (index + m - 1) % len(people)
        # 可视化淘汰（标注轮次和步长）
        x, y = pos_list[people[index]]
        t.color("red")
        t.penup()
        t.goto(x, y - 30)
        t.write(f"第{round_num}轮，步长{m}", align="center", font=("Arial", 10, "normal"))
        # 画叉标记淘汰
        t.goto(x - 15, y - 15)
        t.pendown()
        t.goto(x + 15, y + 15)
        t.goto(x - 15, y + 15)
        t.goto(x + 15, y - 15)
        t.penup()
        # 删除淘汰的人
        del people[index]
        screen.update()
        turtle.delay(1000)
    
    # 标注幸存者
    survivor = people[0]
    x, y = pos_list[survivor]
    t.color("green")
    t.goto(x, y - 40)
    t.write("幸存者", align="center", font=("Arial", 14, "bold"))
    return survivor + 1

# 复用第1课的draw_people函数
def draw_people(n, radius=150):
    people_pos = []
    angle_step = 360 / n
    t = turtle.Turtle()
    for i in range(n):
        angle = i * angle_step
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        t.penup()
        t.goto(x, y - 20)
        t.pendown()
        t.circle(20)
        t.penup()
        t.goto(x, y + 10)
        t.write(i+1, align="center", font=("Arial", 12, "bold"))
        people_pos.append((x, y))
    return people_pos

# 主程序
n = 8
steps = [3,5,2]  # 第一轮步长3，第二轮5，后续2
start_time = time.time()
survivor = josephus_variable_step(n, steps)
end_time = time.time()
print(f"幸存者位置：{survivor}，运行时间：{end_time - start_time:.4f}秒")
turtle.done()