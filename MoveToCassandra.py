import pandas as pd
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

json_file = pd.read_json('Data/11.json')

print(json_file)