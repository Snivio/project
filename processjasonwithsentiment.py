import json
from textblob import TextBlob
import re

a = open('my_posts2.json', 'r')
for i in a:
    k = json.loads(i)
    for q in k:
        result = re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", k["description"])
        analysis = TextBlob(result)
        if analysis.sentiment.polarity > 0:
            print "creat-time:", k["created_time"], "\npost: ", result, "\n"
        else:
            print "normal post\n"

