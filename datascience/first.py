import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(filename,names = headers)

#working with missing data
df.replace("?",np.nan, inplace =True)

missing_data = df.isnull()

for coloum in missing_data.columns.values.tolist():
    print(coloum)
    print(missing_data[coloum].value_counts())
    print("")

avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
df["normalized-losses"].replace(np.nan,avg_norm_loss,inplace=True)


avg_bore = df["bore"].astype("float").mean(axis=0)
df["bore"].replace(np.nan,avg_bore,inplace=True)


avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)


avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)


missing_data1 = df.isnull()

for coloum in missing_data1.columns.values.tolist():
    print(coloum)
    print(missing_data1[coloum].value_counts())
    print("")


#to see which values are present in a particular coloum
df['num-of-doors'].value_counts()
#we can see that four doors are the most common type so we can use '.idxmax()' method to calculate for us the most common type automatically
print(df['num-of-doors'].value_counts().idxmax())
#it will give four
df['num-of-doors'].replace(np.nan,'four',inplace=True)

#we drop price row beacuse price is what we are going to predict if there is no price then how we check that our model is right or not
df.dropna(subset=['price'],axis=0,inplace=True)

#rest index after droping rows
df.reset_index(drop=True,inplace=True)
print(df.head())


# now we have to convert all of them in correct datatype
print(df.dtypes)

df[["bore", "stroke","price","peak-rpm"]] = df[["bore", "stroke","price","peak-rpm"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")

print(df.dtypes)


#now its time to standardization

# Convert mpg to L/100km by mathematical operation (235 divided by mpg)
df['city-L/100km'] = 235/df["city-mpg"]

# transform mpg to L/100km by mathematical operation (235 divided by mpg)
df["highway-mpg"] = 235/df["highway-mpg"]

# rename column name from "highway-mpg" to "highway-L/100km"
df.rename(columns={'"highway-mpg"':'highway-L/100km'}, inplace=True)

#now its time to normalized our data
#normalized means to convert data into similar range

df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()
df['height'] = df['height']/df['height'].max()
# show the scaled columns
print(df[["length","width","height"]].head())
