import pandas as pd
import re
import nltk

# 下载NLTK资源（如果尚未下载）
nltk.download('punkt')

# 定义函数来清洗评论内容
def clean_comment(comment):
    # 移除URL
    comment = re.sub(r'http\S+', '', comment)
    # 移除图片链接
    comment = re.sub(r'\[图片\]', '', comment)
    # 移除HTML标签，如<p>
    comment = re.sub(r'<[^>]*>', '', comment)
    # 移除其他不相关信息
    # 根据需要添加更多清洗步骤
    
    return comment

# 读取CSV文件，使用正确的编码
file_path = r'C:\Users\jesse\Desktop\Master Thesis\Experiment\杭州万象城抢劫金店.csv'
df = pd.read_csv(file_path, encoding='utf-8-sig')  # 使用'utf-8-sig'来处理BOM（字节顺序标记）

# 对“评论内容”列应用clean_comment函数并进行分词
df['评论内容'] = df['评论内容'].apply(clean_comment)
df['评论内容'] = df['评论内容'].apply(nltk.word_tokenize)  # 分词

# 将更新后的DataFrame保存到新的CSV文件中
# 根据需要修改输出文件路径
output_file_path = r'C:\Users\jesse\Desktop\Master Thesis\Experiment\cleaned_tokenized_data.csv'
df.to_csv(output_file_path, index=False, encoding='utf-8-sig')

print("分词完成。更新后的数据保存到:", output_file_path)
