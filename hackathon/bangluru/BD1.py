import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime, timedelta

# Create sample data for Bangalore parking space management
# This simulates data that might be collected from parking sensors or traffic monitors

# Define areas in Bangalore known for high traffic
areas = [
    'MG Road', 'Koramangala', 'Indiranagar', 'Whitefield', 
    'Electronic City', 'Jayanagar', 'HSR Layout', 'BTM Layout'
]

# Generate random data for parking occupancy
np.random.seed(42)  # For reproducibility
num_days = 7  # One week of data
hours_per_day = 24

# Create date range for the past week
end_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
start_date = end_date - timedelta(days=num_days)
date_range = pd.date_range(start=start_date, end=end_date, freq='H')[:-1]  # Exclude last hour

# Create empty dataframe
data = []

# Generate realistic parking data
for area in areas:
    # Different areas have different baseline occupancy rates
    base_occupancy = np.random.randint(40, 80)
    
    for timestamp in date_range:
        hour = timestamp.hour
        day = timestamp.dayofweek
        
        # Weekday patterns (higher during work hours)
        if day < 5:  # Weekday
            if 9 <= hour <= 11:  # Morning rush
                occupancy = base_occupancy + np.random.randint(15, 30)
            elif 12 <= hour <= 14:  # Lunch time
                occupancy = base_occupancy + np.random.randint(10, 25)
            elif 17 <= hour <= 20:  # Evening rush
                occupancy = base_occupancy + np.random.randint(20, 35)
            elif 22 <= hour <= 23 or 0 <= hour <= 5:  # Night
                occupancy = max(0, base_occupancy - np.random.randint(20, 40))
            else:  # Regular hours
                occupancy = base_occupancy + np.random.randint(-10, 10)
        else:  # Weekend
            if 10 <= hour <= 19:  # Shopping/entertainment hours
                occupancy = base_occupancy + np.random.randint(10, 25)
            else:  # Other hours
                occupancy = max(0, base_occupancy - np.random.randint(10, 30))
        
        # Calculate available spaces (assuming 100 spaces per area)
        total_spaces = 100
        available_spaces = max(0, total_spaces - occupancy)
        
        # Add some randomness for realism
        occupancy = min(100, max(0, occupancy + np.random.randint(-5, 5)))
        available_spaces = total_spaces - occupancy
        
        data.append({
            'timestamp': timestamp,
            'area': area,
            'day_of_week': timestamp.strftime('%A'),
            'hour': hour,
            'occupancy_percentage': occupancy,
            'available_spaces': available_spaces,
            'total_spaces': total_spaces
        })

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV (you would typically load this from an external source)
df.to_csv('bangalore_parking_data.csv', index=False)
print("Sample data created and saved to 'bangalore_parking_data.csv'")

# Now let's analyze and visualize the data

# 1. Average parking occupancy by area
area_occupancy = df.groupby('area')['occupancy_percentage'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x=area_occupancy.index, y=area_occupancy.values, palette='viridis')
plt.title('Average Parking Occupancy by Area in Bangalore', fontsize=16)
plt.xlabel('Area', fontsize=12)
plt.ylabel('Average Occupancy (%)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, v in enumerate(area_occupancy.values):
    plt.text(i, v + 1, f"{v:.1f}%", ha='center', fontsize=10)

plt.tight_layout()
plt.savefig('bangalore_parking_by_area.png')
plt.show()

# 2. Parking occupancy by day of week
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_occupancy = df.groupby('day_of_week')['occupancy_percentage'].mean()
day_occupancy = day_occupancy.reindex(day_order)

plt.figure(figsize=(12, 6))
sns.barplot(x=day_occupancy.index, y=day_occupancy.values, palette='muted')
plt.title('Average Parking Occupancy by Day of Week in Bangalore', fontsize=16)
plt.xlabel('Day of Week', fontsize=12)
plt.ylabel('Average Occupancy (%)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, v in enumerate(day_occupancy.values):
    plt.text(i, v + 1, f"{v:.1f}%", ha='center', fontsize=10)

plt.tight_layout()
plt.savefig('bangalore_parking_by_day.png')
plt.show()

# 3. Hourly parking patterns
hourly_occupancy = df.groupby('hour')['occupancy_percentage'].mean()

plt.figure(figsize=(14, 6))
sns.barplot(x=hourly_occupancy.index, y=hourly_occupancy.values, palette='cool')
plt.title('Average Parking Occupancy by Hour of Day in Bangalore', fontsize=16)
plt.xlabel('Hour of Day', fontsize=12)
plt.ylabel('Average Occupancy (%)', fontsize=12)
plt.xticks(range(24))
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, v in enumerate(hourly_occupancy.values):
    plt.text(i, v + 1, f"{v:.1f}%", ha='center', fontsize=9)

plt.tight_layout()
plt.savefig('bangalore_parking_by_hour.png')
plt.show()

# 4. Heatmap of parking occupancy by hour and day
pivot_data = df.pivot_table(
    index='day_of_week', 
    columns='hour', 
    values='occupancy_percentage', 
    aggfunc='mean'
)
pivot_data = pivot_data.reindex(day_order)

plt.figure(figsize=(16, 8))
sns.heatmap(pivot_data, cmap='YlGnBu', annot=True, fmt=".1f", linewidths=.5)
plt.title('Parking Occupancy Heatmap by Day and Hour in Bangalore', fontsize=16)
plt.xlabel('Hour of Day', fontsize=12)
plt.ylabel('Day of Week', fontsize=12)
plt.tight_layout()
plt.savefig('bangalore_parking_heatmap.png')
plt.show()

# 5. Compare weekday vs weekend occupancy
df['is_weekend'] = df['day_of_week'].isin(['Saturday', 'Sunday'])
weekend_comparison = df.groupby(['hour', 'is_weekend'])['occupancy_percentage'].mean().unstack()

plt.figure(figsize=(14, 6))
weekend_comparison[False].plot(label='Weekday', color='blue', linewidth=2)
weekend_comparison[True].plot(label='Weekend', color='orange', linewidth=2)
plt.title('Weekday vs Weekend Parking Occupancy in Bangalore', fontsize=16)
plt.xlabel('Hour of Day', fontsize=12)
plt.ylabel('Average Occupancy (%)', fontsize=12)
plt.legend(fontsize=12)
plt.grid(linestyle='--', alpha=0.7)
plt.xticks(range(24))
plt.tight_layout()
plt.savefig('bangalore_weekday_weekend_comparison.png')
plt.show()

print("Analysis complete. All visualizations have been generated.")