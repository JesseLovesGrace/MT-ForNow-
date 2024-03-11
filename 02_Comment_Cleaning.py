import pandas as pd
import re

# Define a function to clean the comment content
def clean_comment(comment):
    # Remove URLs
    comment = re.sub(r'http\S+', '', comment)
    # Remove picture links
    comment = re.sub(r'\[图片\]', '', comment)
    # Remove HTML tags such as <p>
    comment = re.sub(r'<[^>]*>', '', comment)
    # Remove other irrelevant information
    # Add more cleaning steps as needed
    
    return comment

# Read the CSV file with the correct encoding
file_path = r'C:\Users\jesse\Desktop\Master Thesis\Experiment\杭州万象城抢劫金店.csv'
df = pd.read_csv(file_path, encoding='utf-8-sig')  # Use 'utf-8-sig' to handle BOM (Byte Order Mark)

# Apply the clean_comment function to the "评论内容" column
df['评论内容'] = df['评论内容'].apply(clean_comment)

# Save the cleaned data to a new CSV file with the correct encoding
output_file_path = r'C:\Users\jesse\Desktop\Master Thesis\Experiment\cleaned_data.csv'
df.to_csv(output_file_path, index=False, encoding='utf-8-sig')  # Use 'utf-8-sig' to preserve original encoding

print("Data cleaning completed. Cleaned data saved to:", output_file_path)
