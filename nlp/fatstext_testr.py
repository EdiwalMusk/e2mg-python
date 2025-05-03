import fasttext
model = fasttext.train_unsupervised('D:\\02_workspace\\nlp\enwik9\\fil9')
print(model)