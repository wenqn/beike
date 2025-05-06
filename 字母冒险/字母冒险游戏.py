# 密室逃脱小游戏
# 包含：字符串、列表、字典、函数、循环、条件判断等基础语法

def show_scene(scene):
    """显示场景描述（函数定义与字符串操作）"""
    print("\n" + "="*30)
    print(f"当前场景：{scene['name']}")
    print(scene['description'])
    print("你可以进行的操作：")
    for i, option in enumerate(scene['options'], 1):  # 遍历列表
        print(f"{i}. {option}")

def handle_choice(options):
    """处理玩家选择（输入验证与循环）"""
    while True:  # while循环
        try:
            choice = int(input("请输入选项数字："))
            if 1 <= choice <= len(options):  # 比较运算符
                return choice - 1  # 列表索引从0开始
            print("请输入有效数字！")
        except ValueError:  # 异常处理
            print("请输入数字！")

# 使用字典定义游戏场景（字典嵌套结构）
scenes = {
    "start": {
        "name": "密室入口",
        "description": "你醒来发现自己在一个石室中，墙上有个数字键盘，东北角有扇木门",
        "options": ["检查数字键盘", "尝试打开木门", "查看地面"],
        "next": ["keypad", "door", "floor"]
    },
    "keypad": {
        "name": "数字键盘",
        "description": "键盘上有四位数字输入框，旁边刻着：3的倍数，大于1000",
        "options": ["输入1359", "输入1002", "返回入口"],
        "next": ["success", "fail", "start"]
    },
    "door": {
        "name": "木门",
        "description": "门被铁链锁着，需要钥匙才能打开",
        "options": ["用力撞门", "返回入口"],
        "next": ["fail", "start"]
    },
    # 更多场景定义...
}

def main_game():
    """主游戏逻辑（流程控制）"""
    current = "start"
    while True:  # 游戏主循环
        scene = scenes[current]
        show_scene(scene)
        
        choice_index = handle_choice(scene['options'])
        next_scene = scene['next'][choice_index]
        
        # 条件判断语句
        if next_scene == "success":
            print("\n恭喜！门开了！")
            print(r'''
            ╔═══╗
            ║   ║
            ║ ^ ║
            ╚═══╝
            ''')
            break
        elif next_scene == "fail":
            print("\n失败！触发机关！游戏结束")
            break
        else:
            current = next_scene

if __name__ == "__main__":
    print("=== 密室逃脱 v1.0 ===")
    while True:
        main_game()
        print("感谢游玩！")
