# AI辅助错题整理与重难点突破
## 目标
- 学会使用AI提示词进行错题整理和重难点突破
## 资源
- [AI课堂笔记指南](https://github.com/wenqn/beike/blob/main/AI%E8%BE%85%E5%8A%A9%E5%AD%A6%E4%B9%A0/AI%E8%AF%BE%E5%A0%82%E7%AC%94%E8%AE%B0%E6%8C%87%E5%8D%97.md)（Github）
- [AI课堂笔记指南](https://gitlab.com/zhangwenqn/beike/-/blob/main/%E5%AD%A6%E8%80%83%E5%A4%8D%E4%B9%A0/AI%E8%AF%BE%E5%A0%82%E7%AC%94%E8%AE%B0%E6%8C%87%E5%8D%97.md)（GitLab）
- [Mermaid 在线思维导图](https://mermaid.live/edit#示例代码)
- [百度DeepSeek R1满血版](http://chat.baidu.com)
- [豆包网页版](https://www.doubao.com/chat/)
- [Markdown在线编辑器1](https://www.jyshare.com/front-end/712/)
- [Markdown在线编辑器2](https://tool.lu/markdown/)

## 操作
### 错题整理
> 以下是一个示例题目：正确答案是A，我的错误答案是D
 ```python 
sum = 0  
for i in range(1, 6):  
    sum += i  
print(sum)  
```
> A. 计算1到5的累加和  
> B. 计算1到5的乘积  
> C. 输出1到5的每个数  
> D. 计算1到6的累加和

#### 整理步骤
1. 打开AI，开启深度思考模式
2. 复制以下提示词到AI（需要将替换{{}}中的内容为实际内容，并去掉{{}}）
```
你是一个错题整理助手，你会根据以下内容，整理出一份Markdown格式的错题总结文档。
请根据以下错题：{{错题1}}，{{错题2}}，{{错题3}}，{{错题4}}
我的错误答案：{{具体错误步骤}}  
正确答案：{{标准答案}}  
请执行以下操作：  
1. 分析错误原因（知识漏洞/思维误区）；  
2. 归纳此题对应的知识点（关联到知识框架中的{{章节}}）；  
3. 生成3道同类题型变式练习（题干相似但参数/条件变化）；  
4. 提供延伸训练建议（如针对{{薄弱点}}的专题资源链接）。  
注：完成练习后可再次提交答案进行验证。
```
3. 等待AI整理完成
4. 整理完成后，复制AI输出内容，粘贴到Markdown编辑器中，进一步完善笔记内容与格式。
5. 可以分次处理，每次处理1-3道错题，直到完成所有错题整理。然后再合并整理输出完整文档。
6. 保存笔记, 上传至自己的云空间或云笔记软件中。

### 重难点突破
> 以下是一个示例题目：
```python
def func(n):  
    if n == 0:  
        return 1  
    else:  
        return n * func(n-1)  
```
>    A. 计算n的阶乘  
>    B. 计算n的累加和  
>    C. 判断n是否为素数  
>    D. 生成斐波那契数列

#### 整理步骤
1. 打开AI，开启深度思考模式
2. 复制以下提示词到AI（需要将替换{{}}中的内容为实际内容，并去掉{{}}）
```
你是一个{{重难点}}方面的专家，你会根据以下内容，整理出一份Markdown格式的重难点总结文档。
当前学习难点：{{具体问题描述}}  
请通过以下方式辅助突破：  
1. 多模态解释：用生活类比（如将{{抽象概念}}类比为{{常见事物}}）；  
2. 正反案例对比：展示正确应用 vs 典型错误场景；  
3. 变式训练：提供改变问题维度（如逆向提问、参数极端化）的3道习题；  
4. 推荐学习资源：匹配此难点的优质视频/交互式模拟器链接。  
要求：解释需控制在高中生可理解范围内。
完成后，请检查输出内容是否符合要求，并提供修改建议。
```
3. 等待AI整理完成
4. 整理完成后，复制AI输出内容，粘贴到Markdown编辑器中，进一步完善笔记内容与格式。
5. 可以分次处理，每次处理1-3道重难点，直到完成所有重难点整理。然后再合并整理输出完整文档。
6. 保存笔记, 上传至自己的云空间或云笔记软件中。

## [问题](./AI辅助知识总结.md#问题)