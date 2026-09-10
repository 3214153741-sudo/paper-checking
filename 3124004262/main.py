import re
from collections import Counter

def preprocess(text):
    """此处是文本预处理：去除标点、转为小写、分词"""
    # 只保留中文、英文、数字
    text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9]', '', text)
    return list(text)

def get_ngram(chars, n=3):
    """生成n-gram，默认3-gram"""
    ngram_list = []
    for i in range(len(chars) - n + 1):
        gram = ''.join(chars[i:i+n])
        ngram_list.append(gram)
    return ngram_list

def calc_similarity(text1, text2):
    """计算两段文本的Jaccard相似度"""
    c1 = preprocess(text1)
    c2 = preprocess(text2)
    g1 = get_ngram(c1, 3)
    g2 = get_ngram(c2, 3)
    set1 = set(g1)
    set2 = set(g2)
    inter = set1 & set2
    union = set1 | set2
    if len(union) == 0:
        return 0.0
    sim = len(inter) / len(union)
    return sim

if __name__ == "__main__":
    # 测试例子1
    doc1 = "人工智能是一门研究如何使机器模拟人类智能的学科"
    doc2 = "人工智能是研究让机器模拟人的智能的一门学科"

    sim_score = calc_similarity(doc1, doc2)
    print(f"文本相似度：{sim_score:.4f}")
    print(f"重复率百分比：{sim_score*100:.2f}%")