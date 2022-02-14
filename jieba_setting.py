import jieba
from collections import Counter


def setting(all_title_text):
    # 設定jieba
    # 使用繁體中文詞庫
    jieba.set_dictionary('./Data/dict.txt.big')

    # 自定義字典，把一些專門字詞or術語加入
    jieba.load_userdict('./Data/userDict.txt')

    # 使用預設的精確模式
    jieba.cut(all_title_text, cut_all=False, HMM=True)

    # 將斷詞以list呈現
    word_list = jieba.lcut(all_title_text)

    # 利用 collection 的 Counter 計算頻率
    dict_text = Counter(word_list)

    return dict_text


    