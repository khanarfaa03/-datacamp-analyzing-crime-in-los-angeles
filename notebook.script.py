# 1. Which hour has the highest frequency of crimes?
# Convert 'TIME OCC' to integer representing the hour (e.g., '1200' -> 12, '0330' -> 3)
crimes['hour'] = crimes['TIME OCC'].str[:2].astype(int)
peak_crime_hour = crimes['hour'].value_counts().idxmax()

# 2. Which area has the largest frequency of night crimes (10pm to 359am / hours 22 to 3)?
night_crimes = crimes[(crimes['hour'] >= 22) | (crimes['hour'] < 4)]
peak_night_crime_location = night_crimes['AREA NAME'].value_counts().idxmax()

# 3. Identify the number of crimes committed against victims of different age groups
age_bins = [0, 17, 25, 34, 44, 54, 64, np.inf]
age_labels = ['0-17', '18-25', '26-34', '35-44', '45-54', '55-64', '65+']

crimes['age_bracket'] = pd.cut(crimes['Vict Age'], bins=age_bins, labels=age_labels)
victim_ages = crimes['age_bracket'].value_counts()
