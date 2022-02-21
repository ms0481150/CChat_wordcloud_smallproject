import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as img
from wordcloud import WordCloud, STOPWORDS

def show_frequency(dict_text):
    df_frequency = pd.DataFrame.from_dict(dict_text, orient="index").reset_index().rename(columns={'index':'單字', 0:'次數'})
    df_frequency = df_frequency.sort_values(by="次數", ascending=False)
    df_frequency    
    return df_frequency

def show_pie_plot(df_frequency):
    #plt.rcParams['axes.unicode_minus'] = False
    df = df_frequency.set_index("單字").head(10)
    df.plot(kind="pie", subplots=True, legend=True, figsize=(10,5))
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.show()


def show_wordcloud(dict_text):

    cloud = WordCloud(
                    background_color='black',                              #   背景顏色
                    #max_words=200,                                        #   最大分詞數量
                    #mask=None,                                            #   背景圖案(輪廓)
                    #max_font_size=None,                                   #   顯示字體的最大值
                    #stopwords=st,                                         #   實測這裡跟jieba都不會作動，所以手寫除去
                    font_path="./Data/竹風體W4.ttc",                       #   帶入中文字型(.TTF)
                    #random_state=None,                                    #   隨機碼生成各分詞顏色
                    prefer_horizontal=1,                                   #   調整分詞中水平和垂直的比例
                    scale=16                                               #   匯出的圖片大小
                    ).generate_from_frequencies(dict_text)      

    cloud.to_file('output.png')
    image = img.imread('output.png')
    plt.imshow(image)
