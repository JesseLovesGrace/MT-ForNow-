This is the note for my Probably-Gonna-Be Master Thesis. Fingers Crossed!

Topic: How Censorship in China influences people’s Political Expression-A Study on Zhihu’s Comments on Political Topics
Data Source: Web scraping from Zhihu on Comments (more is always better)

Steps of the Research

Stage 1: Data Collection and Cleaning
Platform: Zhihu, Weibo
	Step 1: Web Scraping Tool for Zhihu (check and done) and Weibo (Still developing)
	Step 2: Clean data (removing irrelevant information and tokenization)

Stage 2: Topic Modeling
  Step 1: Find out whether Laten Dirichlet Allocation (LDA) or Latent Semantic Analysis (LSA) is good for topic modeling (I’ll try both to see if one fits better than the other)
  Step 2:  Topic model

Stage 3: Ideological Analysis:
  Step 1: Find labeled data based on relevant literature and theories for model training (which can be challenging for Chinese corpus; therefore, I might need to label some part of the data to build the corpus manually. Need someone with political science background.)
	Step 2: Build ML model and train it (supervised learning)
	Step 3: Label the classified comments into ideological categories

Stage 4: Comparative Analysis:
Compare the comments on sensitive and censored political topics with those on non-sensitive social and other topics. Analyze differences in:
  1.	Sentiment
  2.	language use
  3.	topic prevalence
between the two sets of comments to identify how censorship influences people's expression on political topics.

Stage 5: Identify Coding Language and Strategies (If I can find any)

Stage 6: Statistical Analysis (Robust test):
  1.	Propensity Score Matching
  2.	Bayesian Inference: estimate the probability of authors belonging to different ideological groups based on their commenting behavior and language use. (Still trying to figure it out)
  3.	Structural Equation Modeling: model the relationships between ideological affiliation, commenting behavior, and discourse characteristics.

Stage 7: Interpretation and Conclusion


Methods Might Be Applied (not necessarily all are going to be applied):

1.	Sentiment Analysis 
2.	Qualitative Analysis (if I can find someone with political science background and speaks Chinese)
  a.	Content Analysis (The aim is to find the use of coded language, signs of self-censorship and etc.)
  b.	User Behavior Analysis (if we found someone interesting)
3.	Quantitative Analysis
  a.	Resampling Scheme
  b.	Calibration Reweighting
  c.	Principal Component Analysis (PCA)
  d.	Exploratory Factory Analysis (EFA)
  e.	Confirmatory Factor Analysis (CFA)
  f.	Percentage Correctly Predicted (PCP)

Ethical Consideration: 
Given the fact that this research may involve some topics considered sensitive by the Chinese government and may pose potential risks to specific online users involved, the research should respect the privacy and security of participants and adheres to ethical guidelines for studying politically sensitive topics.

Actuality of the Research:
  1.	Impact on Public Discourse: Examine how censorship shapes public discourse, potentially suppressing certain topics or viewpoints and impacting the diversity and quality of political dialogue.

  2.	Effects on Social Mobilization: Investigate how censorship influences patterns of social mobilization and collective action, including its impact on the ability of individuals and groups to organize, mobilize support, and advocate for change.

  3.	Influence on Public Opinion Formation: Explore how censorship affects public opinion formation and political attitudes, potentially altering perceptions and beliefs regarding political issues, government policies, and social controversies.

  4.	Implications for Media and Information Policy: Assess the broader implications of censorship for media and information policy, considering alternative approaches to regulating online speech while balancing national security and freedom of expression.

  5.	Comparative Analysis: Extend analysis beyond China to compare censorship's effects across authoritarian regimes, identifying similarities, differences, and strategies for circumventing or adapting to censorship.

  6.	Implications for Digital Rights Advocacy: Consider the implications of your findings for digital rights advocacy, identifying opportunities for policy interventions and technological innovations to mitigate the negative effects of censorship on political expression and information access.
