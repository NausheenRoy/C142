import pandas as pd
import numpy as np

df1=pd.read_csv("articles.csc")
df2=df1

df1 = df1[df1['eventType'] == 'CONTENT SHARED']
df1.head()

df1.shape

def find_total_events(df1_row):
  total_likes = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "LIKE")].shape[0]
  total_views = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "VIEW")].shape[0]
  total_bookmarks = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "BOOKMARK")].shape[0]
  total_follows = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "FOLLOW")].shape[0]
  total_comments = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "COMMENT CREATED")].shape[0]
  return total_likes + total_views + total_bookmarks + total_follows + total_comments

df1["total_events"] = df1.apply(find_total_events, axis=1)

df1.head()

df1 = df1.sort_values(['total_events'], ascending=[True])

df1.head()

output = find_total_events[['title']].head(20).values.tolist()
