# Analyzing Crime in Los Angeles 🚔📊

An Exploratory Data Analysis (EDA) of Los Angeles Police Department (LAPD) crime data using Python and Pandas. This project uncovers temporal patterns, high-risk nighttime locations, and victim demographic distributions to help guide data-driven decision-making.

---

## 💡 Key Analysis & Insights

1. **Peak Crime Hour:** Extracted hours from military timestamps to identify the most active time of day for overall crimes.
2. **Nighttime Crime Hotspots:** Evaluated crime frequency occurring between 10:00 PM and 3:59 AM across all 21 LAPD patrol areas to determine the most vulnerable locations.
3. **Victim Demographic Breakdown:** Categorized victim ages into standard demographic brackets (`0-17`, `18-25`, `26-34`, `35-44`, `45-54`, `55-64`, `65+`) using `pd.cut()` to analyze age distribution.

---

## 🐍 Python Implementation Code

```python
import pandas as pd
import numpy as np

# Load crime dataset
crimes = pd.read_csv("crimes.csv", dtype={"TIME OCC": str})

# -------------------------------------------------------------------
# 1. Peak Crime Hour
# -------------------------------------------------------------------
# Extract the hour from 'TIME OCC' (e.g., '1200' -> 12, '0330' -> 3)
crimes["hour"] = crimes["TIME OCC"].str[:2].astype(int)
peak_crime_hour = crimes["hour"].value_counts().idxmax()

# -------------------------------------------------------------------
# 2. Nighttime Crime Location
# -------------------------------------------------------------------
# Filter for night hours: 10 PM (22) to 3:59 AM (3)
night_crimes = crimes[(crimes["hour"] >= 22) | (crimes["hour"] 
# -datacamp-analyzing-crime-in-los-angeles
Exploratory Data Analysis (EDA) of Los Angeles Police Department (LAPD) crime data using Python and Pandas. Identifies peak crime hours, high-risk nighttime locations, and victim demographic distributions across age brackets.
