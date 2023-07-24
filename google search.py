# import libraries

import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

# connect to google
trends = TrendReq()

# keywords(building request)
trends.build_payload(kw_list=["India"])

#dataframe by region
data = trends.interest_by_region()
data = data.sort_values(by="India", ascending=False)
data = data.head(15)
print(data)

# related topics
print(trends.related_topics().get("Python"))

# related queries
