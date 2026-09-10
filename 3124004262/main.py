import re
import sys

def preprocess(text):
    """文本预处理：过滤无关符号，保留中文、英文、数字"""
    text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9]', '', text)
    return list(text)

def get_ngram(chars, n=3):
    """生成3-gram字符片段"""
    ngram_list = []
    if len(chars) < n:
        return ngram_list
    for i in range(len(chars) - n + 1):
        gram = ''.join(chars[i:i+n])
        ngram_list.append(gram)
    return ngram_list

def calc_similarity(text1, text2):
    """Jaccard相似度计算，返回0~1之间的浮点数"""
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

def read_text(file_path):
    """读取txt文件，捕获文件异常"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"文件不存在：{file_path}")
    except Exception as e:
        raise RuntimeError(f"读取文件失败：{str(e)}")

def write_result(file_path, score):
    """将重复率写入输出文件，保留两位百分比"""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"{score*100:.2f}")
    except Exception as e:
        raise RuntimeError(f"写入文件失败：{str(e)}")

if __name__ == "__main__":
    # 判断命令行参数数量
    if len(sys.argv) != 4:
        print("参数错误，使用方式：python main.py [原文路径] [抄袭文本路径] [输出答案路径]")
        sys.exit(1)
    try:
        org_path = sys.argv[1]
        copy_path = sys.argv[2]
        ans_path = sys.argv[3]
        text_org = read_text(org_path)
        text_copy = read_text(copy_path)
        sim = calc_similarity(text_org, text_copy)
        write_result(ans_path, sim)
    except Exception as err:
        print(f"程序异常：{err}")
        sys.exit(1)