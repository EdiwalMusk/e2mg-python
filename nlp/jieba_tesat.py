import jieba.posseg as pseg
print(pseg.lcut('我爱北京天安门'))

import hanlp
tagger = hanlp.load(hanlp.pretrained.pos.CTB5_POS_RNN_FASTTEXT_ZH)
r = tagger(['我', '的', '希望', '是', '希望', '和平'])
print(r)