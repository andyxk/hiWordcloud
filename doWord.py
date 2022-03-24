# -*-coding:utf-8-*-
# @author: "旅行凯"
# @Time: 2021-12-04 19:23
# @File: doWord.py

#导入模块文件
import wordcloud
import jieba

f = open("演示小说.txt","r",encoding="utf-8")   #已读的，模式打开小说
txt = f.read()
f.close()
# d = path.dirname(__file__)
# mask = np.array(Image.open(path.join(d, "monky.jpg")))

w=wordcloud.WordCloud(background_color="white",width=2000, height=1200, font_path="font/micsoftYH.ttc")

w.generate(" ".join(jieba.lcut(txt)))
w.to_file("dpcq.png")



