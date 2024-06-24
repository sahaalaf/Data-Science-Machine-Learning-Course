import pandas as pd
data = {
    "ShirtNum": [56, 18, 16, 45, 17],
    "Name": ["Babar Azam", "Virat Kohli", "Muhammad Rizwan", "Rohit Sharma", "Ab Devillers"],
    "Runs": [13772, 26799, 10878, 22700, 19890],
    "Matches": [210, 398, 287, 163, 356]
}
df = pd.DataFrame(data)
print(df)
print(df.loc[0])