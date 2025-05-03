import hanlp
tokenizer = hanlp.load('CTB6_CONVSEG')
t = tokenizer("工信处女干事")
print(t)

recognizer = hanlp.load(hanlp.pretrained.ner.MSRA_NER_BERT_BASE_ZH)

a = recognizer(list('业乔汽车科技有限公司总经理于政委和张晨晨大家准备开会了。'))
print(a)

recognizer = hanlp.load(hanlp.pretrained.ner.CONLL03_NER_BERT_BASE_CASED_EN)
a = recognizer(["is", "tom", "sam", "Obama"])

print(a)
