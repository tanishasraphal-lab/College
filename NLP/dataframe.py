import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Influencer": ["Alice", "Bob", "Charlie", "Emma"],
    "Followers": [250000, 180000, 320000, 280000]
})

print("Top Influencer:")
print(df.loc[df["Followers"].idxmax()])

plt.bar(df["Influencer"], df["Followers"])
plt.title("Facebook Influencers")
plt.xlabel("Influencer")
plt.ylabel("Followers")
plt.show()