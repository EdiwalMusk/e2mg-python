import jieba
content = '工薪酬犯法'
l = jieba.lcut(content, cut_all=False)
print(l)
