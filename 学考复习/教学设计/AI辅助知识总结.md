# 用AI辅助进行知识总结
## 目标
- 学会使用AI提示词进行知识总结
- 通过AI提示词整理已学python知识图谱
## 资源
- [AI课堂笔记指南](https://github.com/wenqn/beike/blob/main/%E5%AD%A6%E8%80%83%E5%A4%8D%E4%B9%A0/AI%E8%AF%BE%E5%A0%82%E7%AC%94%E8%AE%B0%E6%8C%87%E5%8D%97.md)（Github）
- [AI课堂笔记指南](https://gitlab.com/zhangwenqn/beike/-/blob/main/%E5%AD%A6%E8%80%83%E5%A4%8D%E4%B9%A0/AI%E8%AF%BE%E5%A0%82%E7%AC%94%E8%AE%B0%E6%8C%87%E5%8D%97.md)（GitLab）
- [Mermaid 在线思维导图](https://mermaid.live/edit#示例代码)
- [百度DeepSeek R1满血版](http://chat.baidu.com)
- [Markdown在线编辑器1](https://www.jyshare.com/front-end/712/)
- [Markdown在线编辑器2](https://tool.lu/markdown/)
## 操作
1. 打开AI，开启深度思考模式
2. 复制以下提示词到AI（需要将知识概念替换{{}}中的内容，去掉{{}}，因此你需要先回忆一下所学关于python的基本概念）
```
你是一个知识总结助手，你会根据以下内容，整理出一份Markdown格式的知识总结文档。
请根据以下关键词/概念：python基础语法, {{核心概念2}}  
1.输出层级化知识框架
2.知识点符合教育科学出版社出版高中信息技术教材，符合最新版山东省高中信息技术学业水平考试大纲要求
3. 标注高频考点和冷门考点
   - 通俗易懂的解释（避免专业术语堆砌）  
   - 至少2个现实案例或图表说明  
   - 3道难度递增的练习题（附答案关键步骤）   
4. 每个知识点提供解释+案例+练习题
5. 生成mermaid语法思维导图指令
5. 提供延伸训练建议（如针对{{薄弱点}}的专题资源链接）。
```
3. 等待AI生成知识总结文档
4. 整理输出为Markdown格式，方便后续学习。
   - 复制AI输出内容，粘贴到Markdown编辑器中，进一步完善笔记内容与格式。
   - 在Markdown编辑器中，将文档导出为md格式或pdf格式（资源链接中‘Markdown在线编辑器2’带有文档导出功能）
5. 整理输出为脑图格式，方便后续学习。
   - 在Markdown编辑器中，将文档导出为mermaid语法
   - 将mermaid语法复制到Mermaid在线编辑器中，生成脑图
   - 将脑图导出为png格式或pdf格式（Mermaid 在线思维导图）
6. 保存笔记, 上传至自己的云空间或云笔记软件中。