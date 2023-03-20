import os
from os.path import expanduser
import warnings
warnings.simplefilter('ignore', FutureWarning)

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# ------------------------------- KEYWORD -------------------------------------------------------------------------


home = expanduser("~")

d1 = os.path.expanduser("~/GitHub/Pylean")

if os.path.exists(d1):
    python_input = open(os.path.expanduser("~/GitHub/Pylean/input/hyakunin.txt"),'r',encoding="utf-8_sig")
else:
    print("Don't forget, pylean folder path.")

index_py = list(python_input.readlines())
pypy = pd.Series(index_py)
sort_py = pypy.sort_index()
data_ruby = list(map(lambda s: s.rstrip(), sort_py))

tfidf = TfidfVectorizer()
tfidf_vec = tfidf.fit_transform(data_ruby)

col = tfidf.get_feature_names()
print(pd.DataFrame(tfidf_vec.toarray(), columns=col))

python_input.close()
