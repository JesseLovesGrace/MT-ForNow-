import pandas as pd
import re
import nltk

# Download NLTK resources (if not already downloaded)
# 下载NLTK资源（如果尚未下载）
nltk.download('punkt')


# Define a function to clean comment content/定义函数来清洗评论内容
def clean_comment(comment):
    # Remove URLs/移除URL
    comment = re.sub(r'http\S+', '', comment)
    # Remove image links/移除图片链接
    comment = re.sub(r'\[图片\]', '', comment)
    # Remove HTML tags, such as <p>/移除HTML标签，如<p>
    comment = re.sub(r'<[^>]*>', '', comment)
    # Remove other irrelevant information/移除其他不相关信息
    # Add more cleaning steps as needed/根据需要添加更多清洗步骤

    return comment


# Read CSV file with the correct encoding/读取CSV文件，使用正确的编码
file_path = r'C:\Users\jesse\Desktop\Master Thesis\Experiment\杭州万象城抢劫金店.csv'
df = pd.read_csv(file_path, encoding='utf-8-sig')   # Use 'utf-8-sig' to handle BOM (Byte Order Mark)
# 使用'utf-8-sig'来处理BOM（字节顺序标记）

# Apply clean_comment function to the "Comment Content" column and tokenize
# 对“评论内容”列应用clean_comment函数并进行分词
df['评论内容'] = df['评论内容'].apply(clean_comment)
df['评论内容'] = df['评论内容'].apply(nltk.word_tokenize)  # 分词

# Save the updated DataFrame to a new CSV file/将更新后的DataFrame保存到新的CSV文件中
# Modify the output file path as needed/根据需要修改输出文件路径
output_file_path = r'C:\Users\jesse\Desktop\Master Thesis\Experiment\cleaned_tokenized_data.csv'
df.to_csv(output_file_path, index=False, encoding='utf-8-sig')

print("分词完成。更新后的数据保存到:", output_file_path)
print("Tokenization complete. Updated data saved to:", output_file_path)
