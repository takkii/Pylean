import os
import re
import traceback
import pandas as pd
from os.path import expanduser
from sklearn import svm, metrics
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# ------------------------------- KEYWORD -------------------------------------------------------------------------


home = expanduser("~")

d1 = os.path.expanduser("~/GitHub/public/Pylean")

if os.path.exists(d1):
    python_input = open(os.path.expanduser("~/GitHub/public/Pylean/input/hyakunin.txt"))
else:
    print("Don't forget, Install dein plugin manager github repo takkii/ruby-dictionary3.")

index_py = list(python_input.readlines())
pypy = pd.Series(index_py)
sort_py = pypy.sort_index()
data_ruby = list(map(lambda s: s.rstrip(), sort_py))

tfidf = TfidfVectorizer()
tfidf_vec = tfidf.fit_transform(data_ruby)

col = tfidf.get_feature_names()
print(pd.DataFrame(tfidf_vec.toarray(), columns=col))

python_input.close()
