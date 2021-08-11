import praw, re

r = praw.Reddit(client_id="xC1-EXGca9wdGQ",
                     client_secret="VZBr0-IX3xY1trGD1wg95AKkcbE",
                      redirect_uri= "http://127.0.0.1:5000/nithin-gok",
                     user_agent="testscript by /u/Nithinkirthick",
                     username="Nithinkirthick")


thread = r.submission(url="https://www.reddit.com/r/AskReddit/comments/hqs6cy/whats_something_you_hate_but_wished_you_loved/")  
print(thread.title)


