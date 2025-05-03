import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

train_data = pd.read_csv('./train.csv', sep=' ')
print(train_data)
test_data = pd.read_csv('./test.csv', sep=' ')

sns.countplot(data=train_data,x='label')
plt.title('train_data')
plt.show()

sns.countplot(data=test_data,x='label')
plt.title('test_data')
plt.show()
