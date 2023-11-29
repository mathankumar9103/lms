import pandas as pd
import pydash

df = pd.read_csv("IPL.csv")

data = df.to_dict(orient="records")
print("")

choice = True

while choice:
    ch = int(input("Enter your choice:"))

    if ch == 1:
        try:
            mat = 0
            player = []

            for i in data:
                if i[City] >