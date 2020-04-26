import nltk
import re
nltk.download('stopwords')
nltk.download('tokensize')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 

stop_words = set(stopwords.words('english')) 
file1 = open("book.txt", encoding="utf-8") 
line = file1.read()# Use this to read file content as a stream: 
#line = line.decode("utf-8")
words = line.split() 
for r in words:
    r = re.sub(r'\W+', '', r)
    r = r.lower()
    r = r.replace("_", "", 100)
    if not r in stop_words: 
        appendFile = open('bookfilter.txt','a')
        appendFile.write(" "+r)
        appendFile.close() 
print("Task Complete")