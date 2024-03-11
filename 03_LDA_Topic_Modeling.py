import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from gensim import corpora, models
import gensim

# 加载CSV数据
data = pd.read_csv("C:\\Users\\jesse\\Desktop\\Master Thesis\\Experiment\\cleaned_tokenized_data.csv")

# 提取评论内容
comments = data["评论内容"]

# 创建文档-词项矩阵（DTM）
vectorizer = CountVectorizer()
dtm = vectorizer.fit_transform(comments)

# 将DTM转换为Gensim格式
corpus = gensim.matutils.Sparse2Corpus(dtm.T)

# 训练LDA模型
num_topics = 5  # 指定主题数量
lda_model = models.LdaModel(corpus, num_topics=num_topics,
                            id2word=dict((v, k) for k, v in vectorizer.vocabulary_.items()))

# 获取每条评论的最可能主题
topic_labels = [lda_model[comment] for comment in corpus]

# 在DataFrame中添加一个新列，带有主题标签
data["Topic"] = topic_labels

# 使用UTF-8编码将更新后的DataFrame保存到新的CSV文件中
data.to_csv("C:\\Users\\jesse\\Desktop\\Master Thesis\\Experiment\\topic_labeled_data.csv",
            index=False, encoding='utf-8-sig')

print("主题标签已添加并保存到topic_labeled_data.csv文件中")
