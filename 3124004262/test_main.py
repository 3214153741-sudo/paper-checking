# test_main.py
import os
import pytest
from main import preprocess, get_ngram, calc_similarity, read_text, write_result

def test_preprocess_normal():
    # 普通文本预处理，过滤符号，只保留中英数字
    s = "数据挖掘，是从海量、杂乱、不完整的数据里，挖掘潜在有用信息！"
    res = preprocess(s)
    # 标点会被删掉，返回字符列表
    assert "数" in res
    assert "，" not in res

def test_preprocess_empty():
    # 空文本预处理
    assert preprocess("") == []

def test_get_ngram_short():
    # 字符长度不足3，返回空列表
    chars = list("ab")
    assert get_ngram(chars,3) == []

def test_get_ngram_normal():
    # 正常生成3gram
    chars = list("abcd")
    grams = get_ngram(chars,3)
    assert grams == ["abc","bcd"]

def test_same_text():
    # 完全相同文本，相似度接近1
    s1 = "软件工程是一门研究软件开发"
    s2 = "软件工程是一门研究软件开发"
    sim = calc_similarity(s1, s2)
    assert sim > 0.99

def test_diff_text():
    # 完全无关文本，相似度很低
    s1 = "春天的花开满山坡"
    s2 = "计算机网络依靠TCP协议"
    sim = calc_similarity(s1, s2)
    assert sim < 0.1

def test_one_empty():
    # 其中一方为空，相似度0
    s1 = ""
    s2 = "人工智能是一门学科"
    sim = calc_similarity(s1, s2)
    assert sim == 0.0

def test_file_read_write(tmp_path):
    # 测试读写文件功能，pytest临时文件
    f_in = tmp_path / "tmp_in.txt"
    f_in.write_text("测试文本", encoding="utf-8")
    content = read_text(str(f_in))
    assert content == "测试文本"

    f_out = tmp_path / "tmp_out.txt"
    write_result(str(f_out), 0.7722)
    saved = f_out.read_text(encoding="utf-8")
    assert saved.strip() == "77.22"

def test_read_not_exist():
    # 测试读取不存在文件，捕获FileNotFoundError（异常场景，博客第6题）
    with pytest.raises(FileNotFoundError):
        read_text("not_exist_123456.txt")
