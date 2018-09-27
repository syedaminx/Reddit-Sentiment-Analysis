# Reddit Sentiment Analysis 

This project was created to be able to find comments in subreddit that are related to a specific keyword or keywords, and perform sentiment analysis on them. In addition, this program will also visualize the most common words in the Reddit comments/posts in a word-cloud to help you get a better understanding of what is being said about your keyword. The comments will be saved in a .csv file and the word-cloud will be outputted in a .png file.

### Prerequisites

The following packages are required to run this program.

* [PRAW](https://github.com/praw-dev/praw)
* [TextBlob](https://textblob.readthedocs.io/en/dev/)
* [datetime](https://docs.python.org/3/library/datetime.html)
* [pandas](https://pandas.pydata.org/pandas-docs/stable/)
* [matplotlib](https://matplotlib.org/)
* [word_cloud](https://github.com/amueller/word_cloud)

### Running the program

After downloading the *reddit_sentiment_analysis.py* file, I would recommend running it through [Jupyter Notebook](http://jupyter.org/). However, this is optional.  

Next, you will need to [create an app on Reddit](https://ssl.reddit.com/prefs/apps/). When creating your application, choose **script** as the application type. You must provide a redirect url when going through this process, "http://reddit.com" will work just fine. 

In the *reddit_sentiment_analysis.py* file, input your information into the following lines:

```
reddit = praw.Reddit(client_id='', 
                     client_secret='', 
                     username='', 
                     password='', 
                     user_agent='')
```

The *client_id* and *client_secret* are listed on the Reddit website, for more reference on where these fields are located click [here](https://imgur.com/a/t6Uc655). The *username* and *password* are the same as what you use to sign in to your Reddit account. The *user_agent* field is up to you, I prefer to use something like "sentimentv1."


After populating those fields, you may now input what you want to search Reddit for. 

```
subreddit = 'Stocks'

keyword = 'Tesla'

time_filter_ = 'week'
```

Here, I am specifying that I would like to search the [Stocks](https://www.reddit.com/r/stocks/) subreddit for the keyword "Tesla" and that I would like to limit the search to posts from the past week. 

Once this has been inputted, you can run the file, which will retrieve the data from Reddit, run the sentiment analysis and output the aforementioned .png and .csv files in the directory where the *reddit_sentiment_analysis.py* is saved.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
