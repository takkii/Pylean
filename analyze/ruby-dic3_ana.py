from os.path import expanduser

import dask.dataframe as dd
import os
import pandas as pd
from pandas import DataFrame

# ------------------------------- KEYWORD -------------------------------------------------------------------------


home = expanduser("~")

d1 = os.path.expanduser("~/.cache/dein/repos/github.com/takkii/go_straight/dict/")
d2 = os.path.expanduser("~/.config/nvim/.cache/dein/repos/github.com/takkii/go_straight/dict/")
d3 = os.path.expanduser("~/.config/nvim/repos/github.com/takkii/go_straight/dict/")

if os.path.isdir(d1):
    ruby_method = open(os.path.expanduser(
        "~/.cache/dein/repos/github.com/takkii/go_straight/dict/ruby_dict"))
elif os.path.isdir(d1):
    ruby_method = open(os.path.expanduser(
        "~/.config/nvim/repos/github.com/takkii/go_straight/dict/ruby_dict"))
elif os.path.isdir(d3):
    ruby_method = open(os.path.expanduser(
        "~/.config/nvim/.cache/dein/repos/github.com/takkii/go_straight/dict/ruby_dict"))
else:
    print("Please, Check the path of go_straight.")

index_ruby = ruby_method.readlines()
Seri = pd.Series(index_ruby)
sort_ruby = Seri.sort_index()
data_ruby = DataFrame(sort_ruby)
ddf = dd.from_pandas(data=data_ruby, npartitions=1)
data = ddf.compute()
print(data)
ruby_method.close()

# ------------------------------- KEYWORD -------------------------------------------------------------------------
