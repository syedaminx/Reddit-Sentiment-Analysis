import praw
from textblob import TextBlob
import datetime
import pandas as pd
from pandas import DataFrame
get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
from wordcloud import WordCloud

current_date = datetime.datetime.today().strftime('%Y-%m-%d')

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     username='',
                     password='',
                     user_agent='')

#insert subreddit to search here, if you want to search all of reddit, insert "all"
subreddit = 'Stocks'
#insert keyword to search here, this will usually be brand or product
keyword = 'Tesla'
#choose how long you want your search parameters to be, it can be: 'all', 'week', 'day', 'hour', 'month', 'year'
time_filter_ = 'week'

overall_subjectivity = 0.0
overall_polarity = 0.0
number_of_sentiments = 0.0

subred_search_param = reddit.subreddit(subreddit).search(keyword, time_filter = time_filter_)

post_dict = { "created":[],
              "comment body":[],
              "polarity":[],
              "subjectivity": [],
              "url": []}

for submission in subred_search_param:
    for comment in submission.comments:
        post_dict["created"].append(datetime.datetime.fromtimestamp(comment.created))
        post_dict["comment body"].append(comment.body)
        comment_analysis = TextBlob(comment.body)
        post_dict["polarity"].append(comment_analysis.polarity)
        post_dict["subjectivity"].append(comment_analysis.subjectivity)
        overall_subjectivity = overall_subjectivity + comment_analysis.subjectivity
        overall_polarity = overall_polarity + comment_analysis.polarity
        post_dict["url"].append("https://reddit.com/"+comment.permalink)
        number_of_sentiments = number_of_sentiments + 1.0

average_subjectivity = overall_subjectivity/number_of_sentiments
average_polarity = overall_polarity/number_of_sentiments

print('The average subjectivity value is ' + str(average_subjectivity))
print('The average polarity value is ' + str(average_polarity))
print(number_of_sentiments)

frame = pd.DataFrame.from_dict(post_dict, orient='index')
frame = frame.transpose()

frame.to_csv("{}_{}_{}_RSA.csv".format(current_date, keyword, subreddit), index=False)

frame

comment_text = str(post_dict['comment body'])

wordcloud = WordCloud(max_font_size=40,max_words=40).generate(comment_text)
plt.figure(figsize=(20,10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("{}_{}_{}_RSA.png".format(current_date, keyword, subreddit))
plt.show()
