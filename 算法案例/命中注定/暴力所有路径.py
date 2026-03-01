'''
暴力破解3*3方格相遇问题
'''
import turtle
import random
# 初始化画棋盘海龟
t = turtle.Turtle()
t.speed(2)  # 绘图速度

# 定义两只海龟，男生和女生
male = turtle.Turtle()
female = turtle.Turtle()

# 绘制3×3方格（4条横线+4条竖线）
def draw_grid(size=100, n=3):
    """绘制n×n方格，每格边长size像素"""
    for i in range(n+1):
        # 横线
        t.penup()
        t.goto(0, i*size)
        t.pendown()
        t.forward(n*size)
        # 竖线
        t.penup()
        t.goto(i*size, 0)
        t.pendown()
        t.goto(i*size, n*size)

def move_turtle(t, direction, size=100):
            """根据方向移动海龟，size为每格边长"""
            if direction == 'R':
                t.forward(size)
            elif direction == 'L':
                t.backward(size)
            elif direction == 'U':
                t.left(90)
                t.forward(size)
                t.right(90)  # 保持方向一致
            elif direction == 'D':
                t.right(90)
                t.forward(size)
                t.left(90)
def init():
    # 初始化两只海龟（男生：蓝色，女生：红色）
    male.color('blue')
    female.color('red')
    male.speed(3)
    female.speed(3)
    # 女生到右上角（300，300）处
    female.penup()
    female.goto(300,300)
    female.pendown()
    # 男生回到原点（0，0）处
    male.penup()
    male.goto(0,0)
    male.pendown()

    
def meeting():
    # 模拟移动并检查相遇
    meeting_point = None
    for i in range(min(len(male_path), len(female_path))):
        move_turtle(male, male_path[i])
        move_turtle(female, female_path[i])
        # 检查是否相遇（坐标是否相同，允许1像素误差）
        if abs(male.xcor() - female.xcor()) < 1 and abs(male.ycor() - female.ycor()) < 1:
            meeting_point = (male.xcor()/100, male.ycor()/100)  # 转换为方格坐标
            print(f"相遇啦！位置：{meeting_point}，步数：{i+1}")
            # 标记相遇点（画个圆圈）
            t = turtle.Turtle()
            t.color('green')
            t.penup()
            t.goto(male.xcor(), male.ycor())
            t.pendown()
            t.circle(10)
            break


# 男生路径：(0,0)→(0,1)→(0,2)→(1,2)→(2,2)
# male_path = ['U', 'R', 'R', 'R']
# 女生路径：(2,2)→(2,1)→(2,0)→(1,0)→(0,0)
# female_path = ['D', 'D', 'L', 'L']

# 绘制方格
draw_grid()

# 主循环
while True:
    init()
    male_path = []
    female_path = []
    male_all = []    #男生走过的所有路径
    female_all = []  #女生走过的所有路径
    
    for i in range(4):
        random.seed()
        male_path.append(random.choice(['U','R']))
        random.seed()
        female_path.append(random.choice(['D','L']))
    print('男生路径：',male_path)
    print('女生路径：',female_path)
    male_all.append(male_path)
    female_all.append(female_path)
    if male_path in male_all and female in female_all:
        continue
    meeting()
turtle.done()