
# 软件工程-文本查重系统
基于3-gram字符分片与Jaccard相似度计算，检测两段文本的重复率。

## 环境
Python3，依赖 pytest、coverage
```bash
pip install pytest coverage
```

## 运行方式
```bash
python main.py [原文文件路径] [待检测文本路径] [输出结果文件]
```
示例：
```bash
python main.py test1.txt copy1.txt ans1.txt
```

## 单元测试
执行单元测试并统计覆盖率：
```bash
coverage run -m pytest test_main.py -v
coverage html
```
运行完成后打开 htmlcov/index.html 查看可视化覆盖率报告。

## 项目文件说明
- main.py：主程序，包含文本预处理、3-gram生成、Jaccard相似度计算、文件读写与异常处理
- test_main.py：单元测试脚本，使用pytest编写
- testX.txt / copyX.txt：10组功能测试输入用例
- ansX.txt：程序输出的重复率结果文件
- .gitignore：git忽略配置，不提交缓存、输出文件
- README.md：项目说明文档
