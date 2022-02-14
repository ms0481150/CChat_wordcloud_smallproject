import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as img
from wordcloud import WordCloud

def show_frequency(dict_text):
    df_frequency = pd.DataFrame.from_dict(dict_text, orient="index").reset_index().rename(columns={'index':'單字', 0:'次數'})
    df_frequency = df_frequency.sort_values(by="次數", ascending=False)
    df_frequency
    return df_frequency

def show_pie_plot(df_frequency):
    plt.rcParams['axes.unicode_minus'] = False
    df = df_frequency.set_index("單字").head(30)
    df.plot(kind="pie", subplots=True, legend=False, figsize=(5,5))
    plt.show()

def show_wordcloud(dict_text):
    cloud = WordCloud(font_path="./Data/竹風體W4.ttc", scale=16).generate_from_frequencies(dict_text)
    cloud.to_file('output.png')
    image = img.imread('output.png')
    plt.imshow(image)
