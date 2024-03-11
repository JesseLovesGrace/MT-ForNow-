import pandas as pd
from snownlp import SnowNLP

# Load CSV data/ 加载CSV数据
data = pd.read_csv("C:\\Users\\jesse\\Desktop\\Master Thesis\\Experiment\\topic_labeled_data.csv")


# Define a function to calculate sentiment polarity
# 定义一个函数来计算情感极性
def calculate_sentiment(text):
    s = SnowNLP(text)
    return s.sentiments


# Apply sentiment analysis to the comment column
# 对评论列应用情感分析
# 将更新后的DataFrame保存到新的CSV文件中
data['Sentiment_Polarity'] = data['评论内容'].apply(calculate_sentiment)

# Save the updated DataFrame to a new CSV file
data.to_csv("C:\\Users\\jesse\\Desktop\\Master Thesis\\Experiment\\topic_labeled_data_with_sentiment.csv", index=False, encoding='utf-8-sig')

print("Sentiment analysis completed and saved to topic_labeled_data_with_sentiment.csv")
