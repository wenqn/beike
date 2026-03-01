import turtle

# 初始化海龟（绘图+写数字）
draw_t = turtle.Turtle()
write_t = turtle.Turtle()
draw_t.speed(2)
write_t.speed(0)
write_t.penup()

# 绘制3×3方格（复用第1课函数）
def draw_grid(size=100, n=3):
    for i in range(n+1):
        # 横线
        draw_t.penup()
        draw_t.goto(0, i*size)
        draw_t.pendown()
        draw_t.forward(n*size)
        # 竖线
        draw_t.penup()
        draw_t.goto(i*size, 0)
        draw_t.pendown()
        draw_t.goto(i*size, n*size)

# 计算动态规划表
def calculate_dp(n=3):
    dp = [[0]*n for _ in range(n)]
    # 边界条件
    for i in range(n):
        dp[i][0] = 1
        dp[0][i] = 1
    # 填充表格
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp

# 用turtle在方格中写路径数
def write_dp(dp, size=100):
    n = len(dp)
    for i in range(n):
        for j in range(n):
            # 移动到方格中心
            x = j*size + size/2
            y = i*size + size/2
            write_t.goto(x, y)
            write_t.write(dp[i][j], align='center', font=('Arial', 20, 'bold'))

# 主流程
dp_table = calculate_dp()
draw_grid()
write_dp(dp_table)

# 计算相遇总路径数
total = 0
for i in range(3):
    for j in range(3):
        male_paths = dp_table[i][j]
        female_paths = dp_table[2-i][2-j]
        total += male_paths * female_paths
        # 标注相遇路径数
        x = j*100 + 100/2
        y = i*100 - 20  # 写在方格下方
        write_t.goto(x, y)
        write_t.write(f'相遇：{male_paths}×{female_paths}', align='center', font=('Arial', 12, 'normal'))

write_t.goto(150, 350)
write_t.write(f'总相遇路径数：{total}', align='center', font=('Arial', 20, 'bold'))
turtle.done()