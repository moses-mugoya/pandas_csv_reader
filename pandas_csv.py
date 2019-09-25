import pandas as pd
df = pd.read_csv("mock_data.csv")
males = 0
females = 0
cd = df[df['gender']!= "Male"]
cde = df['gender']
for c in cde:
    if c == "Male":
        males += 1
    else:
        females += 1

print("The males are "+str(males))
print("The females are "+str(females))


