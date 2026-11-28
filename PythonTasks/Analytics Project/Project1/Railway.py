
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------
# SCENARIO 1: BASIC DATA LOADING & CLEANING
# ------------------------------------------

# Q1: Load the railway gauge CSV file into a Pandas DataFrame
df = pd.read_csv("railway_gauges.csv")

# Q2: Display the first 5 rows and column names
print("\n--- SCENARIO 1 ---")
print("First 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns)

# Q3: Check missing values in each column
print("\nMissing Values:")
print(df.isnull().sum())

# Q4: Replace missing values with 0
df = df.fillna(0)

# Q5: Convert Broad Gauge, Metre Gauge, Narrow Gauge
# and Total columns into numeric types
columns = ["Broad Gauge", "Metre Gauge", "Narrow Gauge", "Total"]

for col in columns:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

print("\nCleaned Data:")
print(df.head())

print("\nData Types:")
print(df.dtypes)


# ------------------------------------------
# SCENARIO 2: SIMPLE VISUALIZATION - LINE GRAPH
# ------------------------------------------

# Q1: Extract Year and Total columns
print("\n--- SCENARIO 2 ---")

data = df[["Year", "Total"]]

print("Year and Total:")
print(data)

# Q2: Plot a line graph showing Total tracks over years
plt.figure(figsize=(12, 6))
plt.plot(data["Year"], data["Total"], marker="o")

# Q3: Add title, X-axis label and Y-axis label
plt.title("Total Railway Tracks Over Years")
plt.xlabel("Year")
plt.ylabel("Total Railway Tracks")

plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()

plt.savefig("total_tracks_line.png")
plt.show()

# Q4: Find the first year's total and last year's total
first_total = df["Total"].iloc[0]
last_total = df["Total"].iloc[-1]

print("\nFirst Year Total:", first_total)
print("Last Year Total:", last_total)

# Q5: Identify whether railway track growth is increasing or decreasing
if last_total > first_total:
    print("Trend: Increasing")
elif last_total < first_total:
    print("Trend: Decreasing")
else:
    print("Trend: No Change")


# ------------------------------------------
# SCENARIO 3: FILTERING + GROUPED BAR CHART
# ------------------------------------------

# Q1: Filter railway data for years after 2000
print("\n--- SCENARIO 3 ---")

df["Start_Year"] = df["Year"].astype(str).str[:4].astype(int)
recent_data = df[df["Start_Year"] > 2000].copy()

# Q2: Select Year, Broad Gauge, Metre Gauge and Narrow Gauge
gauge_data = recent_data[
    ["Year", "Broad Gauge", "Metre Gauge", "Narrow Gauge"]
]

print("\nRailway Data After 2000:")
print(gauge_data)

# Q3: Plot a grouped bar chart comparing all three gauges
gauge_data.set_index("Year")[
    ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]
].plot(kind="bar", figsize=(12, 6))

# Q4: Add legend and proper labels
plt.title("Railway Gauge Comparison After 2000")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.legend(title="Gauge Type")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("gauge_comparison_bar.png")
plt.show()

# Q5: Calculate totals and identify which gauge dominates in recent years
gauge_totals = recent_data[
    ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]
].sum()

print("\nTotal Gauge Length After 2000:")
print(gauge_totals)

dominant_gauge = gauge_totals.idxmax()
print("\nDominant Gauge:", dominant_gauge)


# ------------------------------------------
# SCENARIO 4: FEATURE ENGINEERING + PIE CHART
# ------------------------------------------

# Q1: Calculate total sum of each gauge across all years
print("\n--- SCENARIO 4 ---")

gauge_totals = df[
    ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]
].sum()

print("\nGauge Totals:")
print(gauge_totals)

# Q2: Create a new Series/DataFrame for gauge totals
gauge_df = pd.DataFrame({
    "Gauge": gauge_totals.index,
    "Total": gauge_totals.values
})

print("\nGauge DataFrame:")
print(gauge_df)

# Q3: Plot a pie chart showing percentage contribution
plt.figure(figsize=(8, 8))

plt.pie(
    gauge_df["Total"],
    labels=gauge_df["Gauge"],
    autopct="%1.2f%%",
    startangle=90
)

# Q4: Add percentage labels using autopct and display the chart
plt.title("Percentage Contribution of Railway Gauges")
plt.tight_layout()

plt.savefig("gauge_contribution_pie.png")
plt.show()

# Q5: Identify the highest contributing gauge
highest_gauge = gauge_totals.idxmax()
print("\nHighest Contributing Gauge:", highest_gauge)


# ------------------------------------------
# SCENARIO 5: ADVANCED ANALYSIS + MULTIPLE GRAPHS
# ------------------------------------------

print("\n--- SCENARIO 5 ---")

gauges = ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]

# Q1: Create % Broad Gauge, % Metre Gauge and % Narrow Gauge columns
df["% Broad Gauge"] = (df["Broad Gauge"] / df["Total"]) * 100
df["% Metre Gauge"] = (df["Metre Gauge"] / df["Total"]) * 100
df["% Narrow Gauge"] = (df["Narrow Gauge"] / df["Total"]) * 100

print("\nGauge Percentages:")
print(df[[
    "Year",
    "% Broad Gauge",
    "% Metre Gauge",
    "% Narrow Gauge"
]].round(2))

# Q2: Use NumPy np.diff() to calculate yearly growth of Total tracks
total = df["Total"].to_numpy()
growth = np.diff(total)

print("\nYearly Growth:")
print(growth)

# Find years with highest growth
max_index = np.argmax(growth)

print("\nHighest Growth:")
print("From Year:", df["Year"].iloc[max_index])
print("To Year:", df["Year"].iloc[max_index + 1])
print("Growth:", growth[max_index])

# Q3: Plot a line graph for all gauges
plt.figure(figsize=(12, 6))

plt.plot(df["Year"], df["Broad Gauge"],
         marker="o", label="Broad Gauge")

plt.plot(df["Year"], df["Metre Gauge"],
         marker="o", label="Metre Gauge")

plt.plot(df["Year"], df["Narrow Gauge"],
         marker="o", label="Narrow Gauge")

plt.title("Railway Gauge Trends Over Years")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.legend()
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()

plt.savefig("all_gauges_line.png")
plt.show()

# Q4: Plot a stacked bar chart and identify whether any gauge has declined
df.set_index("Year")[gauges].plot(
    kind="bar",
    stacked=True,
    figsize=(12, 6)
)

plt.title("Railway Gauge Composition Over Years")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.xticks(rotation=90)
plt.tight_layout()

plt.savefig("gauge_composition_stacked.png")
plt.show()

print("\nGauge Decline Analysis:")

for col in gauges:
    first = df[col].iloc[0]
    last = df[col].iloc[-1]

    if last < first:
        print(col, "has decreased overall")
    elif last > first:
        print(col, "has increased overall")
    else:
        print(col, "has remained unchanged")

# Q5: Final conclusion - Is the railway system shifting towards a single dominant gauge?
if (df["Broad Gauge"].iloc[-1] > df["Broad Gauge"].iloc[0]
    and df["Metre Gauge"].iloc[-1] < df["Metre Gauge"].iloc[0]):

    print("\nFinal Conclusion:")
    print("Railway system is shifting towards Broad Gauge.")
    print("Broad Gauge is becoming the dominant gauge.")

else:
    print("\nFinal Conclusion:")
    print("Gauge trends are mixed. Further analysis is required.")

print("\n--- DAY-17 TASKS COMPLETED ---")
