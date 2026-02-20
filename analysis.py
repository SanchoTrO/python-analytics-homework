import pandas as pd
data = {"city": ["Kyiv", "Lviv", "Odesa"], "sales": [1200, 1000, 500]}
df = pd.DataFrame(data)
print("Продажі по містах(тимчасова версія):")
print(df)
print("Середнє значення:", df["sales"].mean())
