import turtle
import math

# 初始化海龟
t = turtle.Turtle()
screen = turtle.Screen()
screen.title("约瑟夫环递推解法可视化")
t.speed(0)

# 绘制递推过程表格
def draw_table(n, m):
    """绘制递推表格，标注每轮f(k,m)的值"""
    # 绘制表格边框
    t.penup()
    t.goto(-300, 200)
    t.pendown()
    t.goto(200, 200)
    t.goto(200, -200)
    t.goto(-300, -200)
    t.goto(-300, 200)
    
    # 绘制列标题（人数k、f(k,m)、实际位置）
    col_titles = ["人数k", "f(k,m)", "实际位置"]
    for i, title in enumerate(col_titles):
        t.penup()
        t.goto(-300 + i*160, 180)
        t.write(title, align="center", font=("Arial", 12, "bold"))
        # 绘制竖线
        t.pendown()
        t.goto(-300 + i*160, -200)
    
    # 计算递推值并绘制每行
    f_prev = 0  # f(1,m)=0
    row_y = 150
    for k in range(1, n+1):
        if k == 1:
            f_k = 0
        else:
            f_k = (f_prev + m) % k
        # 填写每行内容
        t.penup()
        t.goto(-300 + 0*160, row_y)
        t.write(k, align="center", font=("Arial", 12, "normal"))
        t.goto(-300 + 1*160, row_y)
        t.write(f_k, align="center", font=("Arial", 12, "normal"))
        t.goto(-300 + 2*160, row_y)
        t.write(f_k + 1, align="center", font=("Arial", 12, "normal"))
        # 标注递推关系（k≥2时）
        if k >= 2:
            t.color("red")
            t.penup()
            t.goto(-300 + 1*160, row_y + 10)
            t.write(f"=({f_prev}+{m})%{k}", font=("Arial", 10, "normal"))
            t.color("black")
        # 更新上一轮值
        f_prev = f_k
        row_y -= 30
        # 绘制横线
        t.pendown()
        t.goto(-300, row_y)
        t.goto(200, row_y)
    
    # 标注最终结果
    t.color("green")
    t.penup()
    t.goto(0, -220)
    t.write(f"{n}人围圈，报数到{m}淘汰，幸存者位置：{f_prev + 1}", 
            align="center", font=("Arial", 14, "bold"))
    return f_prev + 1

# 递推解法函数
def josephus_recursive(n, m):
    if n == 1:
        return 0
    return (josephus_recursive(n-1, m) + m) % n

# 主程序
n = 5
m = 2
# 绘制递推表格
survivor = draw_table(n, m)
# 验证递归解法
recur_survivor = josephus_recursive(n, m) + 1
print(f"递推解法结果：{survivor}，递归解法结果：{recur_survivor}")
turtle.done()