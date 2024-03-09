import requests
import time
import pandas as pd
import os


# Function to transform timestamp to human-readable format
def trans_date(v_timestamp):
    time_array = time.localtime(v_timestamp)
    other_style_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return other_style_time


# Function to transform gender tag to human-readable format
def tran_gender(gender_tag):
    if gender_tag == 1:
        return 'male'
    elif gender_tag == 0:
        return 'female'
    else:
        return 'not defined'


# Define the answer ID
answer_id = 930193847

# Define the URL for fetching comments
url0 = f'https://www.zhihu.com/api/v4/comment_v5/answers/{answer_id}/root_comment?order_by=score&limit=20&offset='

# Define the headers for the request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Referer': 'https://www.zhihu.com/question/291278869/answer/930193847',
    'Cookie': '_zap=e0e06bd1-f135-4839-9c95-5bcd8c9b6447; d_c0=AHDZXZR97haPTtRWmtVprW1qJ2KInKq4Y-Y=|1686741951; __snaker__id=FFprrs1VNhxXIiKl; YD00517437729195%3AWM_NI=tDh4kTKhBTYakVx2jvb3gMfM7rU6XO9N9PtjjHOmSrUiyKd60OgwncxNjpnF3DNhjHMP8pZ3w1yzNXlzDpwnm51u02vsjsr2eOg9nYwTD9Wsato27a3mbio1fEFMkIc0V0g%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eebaf24781acabd0cb59a88a8eb6d15b839f9fb1c861a7899caed4449b958497bc2af0fea7c3b92ab89ca8d5ea6089b88eb5dc6ba98ab8d3e97ea2eda9aee547f5ae9bd7db45fb92f7b1f762aa98818ed27a97b7b7ace73ef491a998ed69bc92a691ed4ef19c8289e9448f90f891d939b5efb79bcd54b0a68c91f666afebff96b33ab6ada694f13aa791a9daed53b58c8cdad679a3aca1d3b66bf1b3ae8aee3ba69b8aaeea43a1f09ad1e637e2a3; YD00517437729195%3AWM_TID=ykwA%2B4kSWbpBEFBUUEPU0OGSYRDIee68; q_c1=dc63222d444c42c6b05ebe898a8e028e|1687003767000|1687003767000; q_c1=dc63222d444c42c6b05ebe898a8e028e|1693126237000|1687003767000; __utma=51854390.1113752316.1693126239.1693126239.1693126239.1; __utmv=51854390.100-1|2=registration_date=20230502=1^3=entry_date=20230502=1; z_c0=2|1:0|10:1708964656|4:z_c0|80:MS4xd2o5RVJnQUFBQUFtQUFBQVlBSlZUUjVydzJaSTBqZkE1bXdoc0dQNWdGbXFURlBzQjZwZ3FRPT0=|56bab5a8be19e433f519b184c200f4c487c2f9da25ed30641c65eafb7c712555; _xsrf=ba312381-a7d8-4032-98cf-53bdf894d200; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1709720633,1709740215,1709831653,1709906711; tst=r; SESSIONID=rUm1xuxLrtL8whP53VL9ByFUSrmRjrRVCpGJKJMd4pa; JOID=UlwRBE2Lya24eJHiGI3rfIVtMFgL_ZzDiAbgmlf_ueGDDv-2LfqlQ9p6leEa5-QmKyN466k0oD61aQLF7RaCJvY=; osd=W1EcC06CxKC3e5jvFYLodYhgP1sC8JHMiw_tl1j8sOyOAfy_IPeqQNN3mO4Z7ukrJCBx5qQ7oze4ZA3G5BuPKfU=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1710008295; KLBRSID=e42bab774ac0012482937540873c03cf|1710008296|1710006844'
}

# Make the GET request
r0 = requests.get(url0, headers=headers)
total_comments = r0.json()['comment_counts']
print(f'Total comments: {total_comments}')
##########################################################################################
# Still Getting: {'error': {'message': '请求参数异常，请升级客户端后重试。', 'code': 10003}}#
##########################################################################################

# Calculate the max page based on the total number of comments and limit per page
limit_per_page = 20
max_page = total_comments // limit_per_page + 1
print('Max page:', max_page)

authors = []
genders = []
answer_urls = []
author_homepages = []
author_pics = []
create_times = []
contents = []
child_tags = []

# Loop over pages of comments
for page in range(0, max_page):
    offset = page * limit_per_page
    url = url0 + str(offset)
    r = requests.get(url, headers=headers)
    comments = r.json()['data']

    for c in comments:  # Loop over comments in current page
        # Process the comment
        author = c['author']['member']['name']
        authors.append(author)
        gender_tag = c['author']['member']['gender']
        genders.append(tran_gender(gender_tag))
        # Add other attributes to respective lists

        if c['child_comments']:  # Check if there are child comments
            for child in c['child_comments']:  # Loop over child comments
                # Process the child comment
                child_author = child['author']['member']['name']
                authors.append(child_author)
                child_gender_tag = child['author']['member']['gender']
                genders.append(tran_gender(child_gender_tag))
                # Add other attributes to respective lists

# Create DataFrame and save to CSV
df = pd.DataFrame({
    'Answer url': answer_urls,
    'Page': [i + 1 for i in range(len(answer_urls))],
    'Author': authors,
    'Gender': genders,
    'Author_homepages': author_homepages,
    'Author_pics': author_pics,
    'Create_time': create_times,
    'Content': contents,
    'Child_tag': child_tags,
})

# Define the file path for saving the CSV file
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop_path, 'First_Test.csv')

# Save to CSV file
df.to_csv(file_path, mode='a+', index=False, header=True, encoding='utf_8_sig')
