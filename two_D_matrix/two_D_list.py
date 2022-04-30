region = [
        # 0        # 1
        ["India", "US"],        # 0
        ["China", "Spain"],     # 1
        ["Germany", "France"]   # 2
    ]

rows, cols = len(region), len(region[0])
for r in range(rows):
    for c in range(cols):
        print(r, c)
        print(region[r][c])

for r in region:
    for country in r:
        print(country)
