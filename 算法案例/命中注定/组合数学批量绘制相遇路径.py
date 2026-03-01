import turtle
from itertools import combinations

# 生成从(0,0)到(m,n)的所有路径（仅右R、上U移动，最短路径）
def generate_paths(m, n):
    paths = []
    # 总步数：m次右移 + n次上移 = m+n步
    total_steps = m + n
    # 选择m步作为右移（其余为上移）
    for right_steps in combinations(range(total_steps), m):
        path = []
        for i in range(total_steps):
            if i in right_steps:
                path.append('R')
            else:
                path.append('U')
        paths.append(path)
    return paths

# 批量绘制路径
def draw_all_paths(paths, size=100):
    # 绘制方格
    t = turtle.Turtle()
    t.speed(2)
    for i in range(3):
        t.penup()
        t.goto(0, i*size)
        t.pendown()
        t.forward(2*size)
        t.penup()
        t.goto(i*size, 0)
        t.pendown()
        t.goto(i*size, 2*size)

    # 定义颜色列表（区分不同路径）
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown']
    for idx, path in enumerate(paths):
        # 每个路径创建一只新海龟
        path_t = turtle.Turtle()
        path_t.color(colors[idx % len(colors)])
        path_t.speed(3)
        path_t.penup()
        path_t.goto(0, 0)
        path_t.pendown()
        # 移动海龟
        for direction in path:
            if direction == 'R':
                path_t.forward(size)
            elif direction == 'U':
                path_t.left(90)
                path_t.forward(size)
                path_t.right(90)
        # 标注路径序号
        path_t.penup()
        path_t.goto(100, 300 + idx*30)
        path_t.write(f'路径{idx+1}：{path}', font=('Arial', 12, 'normal'))

# 生成从(0,0)到(2,2)的所有最短路径
all_paths = generate_paths(2, 2)
print(f'总路径数：{len(all_paths)}')
print(f'所有路径：{all_paths}')

# 批量绘制
draw_all_paths(all_paths)
turtle.done()