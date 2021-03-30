##%
import json
import pandas as pd

file1='Sarcasm_Headlines_Dataset.json'
#with open(file1, 'r') as f:
#    datastore=json.load(f)
news = pd.read_json('Sarcasm_Headlines_Dataset.json',lines=True)
news.head()

##%%
