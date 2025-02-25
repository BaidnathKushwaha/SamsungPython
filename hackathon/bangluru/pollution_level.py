import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


data = pd.read_csv('Banglore_traffic_Dataset.csv')


data = data.dropna(subset=['Environmental Impact'])


plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("viridis")


fig = plt.figure(figsize=(20, 15))
fig.suptitle('Pollution Levels Analysis in Bangalore Traffic', fontsize=20, fontweight='bold')


ax1 = plt.subplot(2, 2, 1)
area_pollution = data.groupby('Area Name')['Environmental Impact'].mean().sort_values(ascending=False)
sns.barplot(x=area_pollution.values, y=area_pollution.index, ax=ax1)
ax1.set_title('Average Pollution Levels by Area', fontsize=16)
ax1.set_xlabel('Environmental Impact Score', fontsize=12)
ax1.set_ylabel('Area Name', fontsize=12)


ax2 = plt.subplot(2, 2, 2)
sns.scatterplot(x='Traffic Volume', y='Environmental Impact', data=data, ax=ax2, alpha=0.7, hue='Area Name')
ax2.set_title('Traffic Volume vs. Pollution Levels', fontsize=16)
ax2.set_xlabel('Traffic Volume', fontsize=12)
ax2.set_ylabel('Environmental Impact', fontsize=12)
ax2.legend(loc='upper left', bbox_to_anchor=(1, 1))

# 3. Pollution levels over time (if date information is available)
if 'Date' in data.columns:
    ax3 = plt.subplot(2, 2, 3)
    
    if not pd.api.types.is_datetime64_any_dtype(data['Date']):
        data['Date'] = pd.to_datetime(data['Date'])
    
   
    date_pollution = data.groupby('Date')['Environmental Impact'].mean()
    sns.lineplot(x=date_pollution.index, y=date_pollution.values, ax=ax3, marker='o')
    ax3.set_title('Average Pollution Levels Over Time', fontsize=16)
    ax3.set_xlabel('Date', fontsize=12)
    ax3.set_ylabel('Environmental Impact Score', fontsize=12)


ax4 = plt.subplot(2, 2, 4)
weather_pollution = data.groupby('Weather Conditions')['Environmental Impact'].mean().sort_values(ascending=False)
sns.barplot(x=weather_pollution.values, y=weather_pollution.index, ax=ax4)
ax4.set_title('Average Pollution Levels by Weather Condition', fontsize=16)
ax4.set_xlabel('Environmental Impact Score', fontsize=12)
ax4.set_ylabel('Weather Conditions', fontsize=12)

plt.figure(figsize=(14, 10))

numeric_cols = data.select_dtypes(include=[np.number]).columns
correlation = data[numeric_cols].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', linewidths=0.5, fmt=".2f")
plt.title('Correlation Between Traffic Metrics and Pollution', fontsize=18)

# Let's also create a function to find high pollution hotspots
def identify_pollution_hotspots(data, threshold_percentile=90):
    """Identify locations with critically high pollution levels."""
    threshold = np.percentile(data['Environmental Impact'], threshold_percentile)
    hotspots = data[data['Environmental Impact'] >= threshold].copy()
    
  
    location_counts = hotspots.groupby(['Area Name', 'Road/Intersection Name']).size().reset_index(name='Frequency')
    location_avg = hotspots.groupby(['Area Name', 'Road/Intersection Name'])['Environmental Impact'].mean().reset_index(name='Avg_Impact')
    
    
    hotspot_analysis = pd.merge(location_counts, location_avg, on=['Area Name', 'Road/Intersection Name'])
    return hotspot_analysis.sort_values('Avg_Impact', ascending=False)


hotspots = identify_pollution_hotspots(data)
if not hotspots.empty:
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Avg_Impact', y=hotspots.apply(lambda x: f"{x['Area Name']} - {x['Road/Intersection Name']}", axis=1), 
                hue='Frequency', data=hotspots, palette='YlOrRd')
    plt.title('Pollution Hotspots in Bangalore', fontsize=18)
    plt.xlabel('Average Environmental Impact', fontsize=14)
    plt.ylabel('Location', fontsize=14)
    plt.tight_layout()


plt.tight_layout()
plt.savefig('bangalore_pollution_analysis.png', dpi=300, bbox_inches='tight')

# Display information about the analysis
print("Analysis of Pollution Levels in Bangalore Traffic:")
print(f"Total data points analyzed: {len(data)}")
print(f"Average pollution level across the city: {data['Environmental Impact'].mean():.2f}")
print(f"Areas with highest average pollution:")
for area, value in area_pollution.head(3).items():
    print(f"  - {area}: {value:.2f}")
print("\nIdentified pollution hotspots:")
if not hotspots.empty:
    for _, row in hotspots.head(5).iterrows():
        print(f"  - {row['Area Name']} ({row['Road/Intersection Name']}): {row['Avg_Impact']:.2f}")
plt.show()
