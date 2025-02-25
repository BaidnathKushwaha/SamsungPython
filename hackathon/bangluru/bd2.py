import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

# Load the dataset
def load_data(file_path="Banglore_traffic_Dataset.csv"):
    df = pd.read_csv(file_path)
    # Clean the dataframe by removing rows with all NaN values
    df = df.dropna(how='all')
    # Convert date to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    return df

# Preprocess the data for signal timing optimization
def preprocess_data(df):
    # Select relevant columns for optimization
    relevant_cols = ['Area Name', 'Road/Intersection Name', 'Traffic Volume', 
                     'Average Speed', 'Congestion Level', 'Travel Time Index',
                     'Traffic Signal Compliance', 'Incident Reports']
    
    # Create a new dataframe with these columns
    signal_df = df[relevant_cols].copy()
    
    # Calculate volume-to-capacity ratio (V/C)
    # Assuming congestion level represents percentage of capacity utilized
    signal_df['Volume_Capacity_Ratio'] = signal_df['Traffic Volume'] / (signal_df['Traffic Volume'].max() * 100 / signal_df['Congestion Level'])
    
    # Create location identifier
    signal_df['Location'] = signal_df['Area Name'] + ' - ' + signal_df['Road/Intersection Name']
    
    return signal_df

# Calculate optimal signal timing
def calculate_optimal_signal_timing(signal_df):
    # Group by location
    location_groups = signal_df.groupby('Location')
    
    # Initialize results dataframe
    results = []
    
    # Cycle length parameters
    min_cycle_length = 60  # seconds
    max_cycle_length = 180  # seconds
    
    for location, group in location_groups:
        # Average values for the location
        avg_volume = group['Traffic Volume'].mean()
        avg_speed = group['Average Speed'].mean()
        avg_congestion = group['Congestion Level'].mean()
        avg_tti = group['Travel Time Index'].mean()
        avg_compliance = group['Traffic Signal Compliance'].mean()
        avg_incidents = group['Incident Reports'].mean()
        avg_vc_ratio = group['Volume_Capacity_Ratio'].mean()
        
        # Webster's formula for optimal cycle length
        # C = (1.5L + 5) / (1 - Y) where L is total lost time and Y is sum of critical flow ratios
        # We'll simulate this using our available metrics
        
        # Estimate lost time based on congestion level
        lost_time = 4 + (avg_congestion / 25)  # 4 seconds base + additional time based on congestion
        
        # Estimate flow ratio using volume-capacity ratio
        flow_ratio = min(0.95, avg_vc_ratio)  # Cap at 0.95 to avoid division by zero
        
        # Calculate optimal cycle length using modified Webster's formula
        if flow_ratio < 1:
            cycle_length = (1.5 * lost_time + 5) / (1 - flow_ratio)
            # Constrain cycle length to reasonable bounds
            cycle_length = max(min_cycle_length, min(max_cycle_length, cycle_length))
        else:
            cycle_length = max_cycle_length  # Use maximum if heavily congested
        
        # Calculate green time distribution
        # Assuming 4-way intersection with 2 major approaches and 2 minor approaches
        
        # Major approach gets more green time proportional to traffic volume and congestion
        major_green_ratio = 0.6 + (avg_congestion / 500)  # Base 60% + adjustment
        major_green_ratio = min(0.8, max(0.5, major_green_ratio))  # Constrain between 50-80%
        
        # Calculate actual green times
        major_green_time = (cycle_length - 4 * lost_time) * major_green_ratio
        minor_green_time = (cycle_length - 4 * lost_time) * (1 - major_green_ratio)
        
        # Adjust based on compliance - lower compliance means longer yellow times
        yellow_time = 3 + (1 - avg_compliance/100) * 2  # Base 3 seconds + adjustment
        
        # Store results
        results.append({
            'Location': location,
            'Area': group['Area Name'].iloc[0],
            'Intersection': group['Road/Intersection Name'].iloc[0],
            'Avg_Traffic_Volume': avg_volume,
            'Avg_Speed': avg_speed,
            'Avg_Congestion': avg_congestion,
            'Avg_Compliance': avg_compliance,
            'Optimal_Cycle_Length': round(cycle_length, 1),
            'Major_Green_Time': round(major_green_time, 1),
            'Minor_Green_Time': round(minor_green_time, 1),
            'Yellow_Time': round(yellow_time, 1),
            'Estimated_Lost_Time': round(lost_time, 1)
        })
    
    results_df = pd.DataFrame(results)
    return results_df

# Analyze and cluster intersections for similar timing patterns
def cluster_intersections(signal_df, results_df, n_clusters=3):
    # Prepare data for clustering
    cluster_features = ['Avg_Traffic_Volume', 'Avg_Speed', 'Avg_Congestion', 'Avg_Compliance']
    
    # Scale the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(results_df[cluster_features])
    
    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    results_df['Timing_Cluster'] = kmeans.fit_predict(scaled_data)
    
    # Calculate cluster centers
    cluster_centers = pd.DataFrame(
        scaler.inverse_transform(kmeans.cluster_centers_),
        columns=cluster_features
    )
    
    # Add descriptive labels to clusters
    cluster_descriptions = []
    for i, center in enumerate(kmeans.cluster_centers_):
        # Get the original values
        volume = cluster_centers.iloc[i]['Avg_Traffic_Volume']
        speed = cluster_centers.iloc[i]['Avg_Speed']
        congestion = cluster_centers.iloc[i]['Avg_Congestion']
        
        # Create descriptive label
        if congestion > 80:
            description = "High Congestion"
        elif congestion > 50:
            description = "Medium Congestion"
        else:
            description = "Low Congestion"
            
        if volume > 40000:
            description += ", High Volume"
        elif volume > 20000:
            description += ", Medium Volume"
        else:
            description += ", Low Volume"
            
        cluster_descriptions.append(f"Cluster {i}: {description}")
    
    # Map clusters to their descriptions
    cluster_map = {i: desc for i, desc in enumerate(cluster_descriptions)}
    results_df['Cluster_Description'] = results_df['Timing_Cluster'].map(cluster_map)
    
    return results_df, cluster_centers, cluster_descriptions

# Simulate the effect of signal timing optimization
def simulate_optimization_effect(results_df):
    # Estimate improvement factors based on the optimization
    results_df['Estimated_Congestion_Reduction'] = np.clip(
        results_df['Avg_Congestion'] * (0.15 - 0.05 * (results_df['Avg_Compliance'] / 100)),
        5, 25
    )
    
    results_df['Estimated_Speed_Improvement'] = np.clip(
        results_df['Avg_Speed'] * (0.1 + 0.05 * (results_df['Estimated_Congestion_Reduction'] / 20)),
        2, 10
    )
    
    results_df['Estimated_Travel_Time_Reduction'] = np.clip(
        15 + 0.0002 * results_df['Avg_Traffic_Volume'] + 0.2 * results_df['Estimated_Congestion_Reduction'],
        10, 30
    )
    
    return results_df

# Create visualizations for the optimization results
def create_visualizations(df, results_df):
    plt.figure(figsize=(20, 15))
    
    # 1. Optimal Cycle Length by Location
    plt.subplot(2, 2, 1)
    ax = sns.barplot(x='Location', y='Optimal_Cycle_Length', hue='Cluster_Description', data=results_df)
    plt.title('Optimal Cycle Length by Location', fontsize=14)
    plt.xlabel('Location', fontsize=12)
    plt.ylabel('Cycle Length (seconds)', fontsize=12)
    plt.xticks(rotation=90)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # 2. Green Time Distribution
    plt.subplot(2, 2, 2)
    locations = results_df['Location'].tolist()
    major_green = results_df['Major_Green_Time'].tolist()
    minor_green = results_df['Minor_Green_Time'].tolist()
    yellow = results_df['Yellow_Time'].tolist() * 4  # 4 phases
    lost = results_df['Estimated_Lost_Time'].tolist() * 4  # 4 phases
    
    # Creating stacked bar chart
    width = 0.8
    
    plt.bar(locations, major_green, width, label='Major Green Time')
    plt.bar(locations, minor_green, width, bottom=major_green, label='Minor Green Time')
    plt.bar(locations, yellow, width, bottom=[i+j for i,j in zip(major_green, minor_green)], label='Yellow Time')
    plt.bar(locations, lost, width, bottom=[i+j+k for i,j,k in zip(major_green, minor_green, yellow)], label='Lost Time')
    
    plt.title('Signal Phase Distribution by Location', fontsize=14)
    plt.xlabel('Location', fontsize=12)
    plt.ylabel('Time (seconds)', fontsize=12)
    plt.xticks(rotation=90)
    plt.legend(loc='upper right')
    
    # 3. Traffic Volume vs Optimal Cycle Length
    plt.subplot(2, 2, 3)
    sns.scatterplot(x='Avg_Traffic_Volume', y='Optimal_Cycle_Length', 
                   hue='Cluster_Description', size='Avg_Congestion',
                   sizes=(50, 200), alpha=0.7, data=results_df)
    
    plt.title('Traffic Volume vs Optimal Cycle Length', fontsize=14)
    plt.xlabel('Average Traffic Volume', fontsize=12)
    plt.ylabel('Optimal Cycle Length (seconds)', fontsize=12)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # 4. Estimated Improvements
    plt.subplot(2, 2, 4)
    
    x = np.arange(len(locations))
    width = 0.25
    
    plt.bar(x - width, results_df['Estimated_Congestion_Reduction'], width, label='Congestion Reduction (%)')
    plt.bar(x, results_df['Estimated_Speed_Improvement'], width, label='Speed Improvement (km/h)')
    plt.bar(x + width, results_df['Estimated_Travel_Time_Reduction'], width, label='Travel Time Reduction (%)')
    
    plt.title('Estimated Improvements After Optimization', fontsize=14)
    plt.xlabel('Location', fontsize=12)
    plt.ylabel('Improvement', fontsize=12)
    plt.xticks(x, locations, rotation=90)
    plt.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig('signal_timing_optimization_results.png')
    plt.close()
    
    # Additional visualization: Timing cluster characteristics
    plt.figure(figsize=(15, 10))
    
    # Melt the dataframe for easier plotting
    cluster_melted = pd.melt(
        results_df, 
        id_vars=['Location', 'Timing_Cluster', 'Cluster_Description'],
        value_vars=['Avg_Traffic_Volume', 'Avg_Speed', 'Avg_Congestion', 'Avg_Compliance'],
        var_name='Metric', value_name='Value'
    )
    
    # Create a boxplot for each metric by cluster
    sns.boxplot(x='Metric', y='Value', hue='Cluster_Description', data=cluster_melted)
    plt.title('Cluster Characteristics', fontsize=14)
    plt.xlabel('Metric', fontsize=12)
    plt.ylabel('Value', fontsize=12)
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.tight_layout()
    plt.savefig('timing_cluster_characteristics.png')
    plt.close()
    
    # Create a map of Bangalore with the optimal signal timings
    # For this demonstration, we'll create a bubble chart to represent the locations
    plt.figure(figsize=(12, 10))
    
    # For demonstration purposes, we'll create synthetic coordinates
    # In a real application, you would use actual geo-coordinates
    np.random.seed(42)
    x_coords = np.random.uniform(77.5, 77.7, len(results_df))
    y_coords = np.random.uniform(12.9, 13.1, len(results_df))
    
    # Area-based grouping for more realistic positioning
    area_groups = {'Indiranagar': (77.64, 12.98),
                  'Whitefield': (77.75, 12.97),
                  'Koramangala': (77.63, 12.93),
                  'M.G. Road': (77.61, 12.97),
                  'Jayanagar': (77.58, 12.92),
                  'Hebbal': (77.59, 13.04),
                  'Yeshwanthpur': (77.54, 13.02)}
    
    for i, row in results_df.iterrows():
        if row['Area'] in area_groups:
            base_x, base_y = area_groups[row['Area']]
            x_coords[i] = base_x + np.random.uniform(-0.01, 0.01)
            y_coords[i] = base_y + np.random.uniform(-0.01, 0.01)
    
    # Create the scatter plot
    plt.scatter(x_coords, y_coords, 
               s=results_df['Optimal_Cycle_Length'] * 2, 
               c=results_df['Timing_Cluster'], 
               cmap='viridis', 
               alpha=0.7)
    
    # Add location labels
    for i, row in results_df.iterrows():
        plt.annotate(row['Location'], 
                    (x_coords[i], y_coords[i]),
                    fontsize=8,
                    ha='center')
    
    # Add a colorbar
    cbar = plt.colorbar()
    cbar.set_label('Timing Cluster')
    
    # Add map styling
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xlabel('Longitude (simulated)', fontsize=12)
    plt.ylabel('Latitude (simulated)', fontsize=12)
    plt.title('Bangalore Traffic Signal Optimization Map (Simulated)', fontsize=14)
    
    # Add roads (simulated)
    for area, (x, y) in area_groups.items():
        plt.plot([77.5, x], [y, y], 'k-', alpha=0.2)
        plt.plot([x, x], [12.9, y], 'k-', alpha=0.2)
    
    plt.tight_layout()
    plt.savefig('bangalore_signal_map.png')
    plt.close()

# Create a time-of-day optimization analysis
def analyze_time_of_day_patterns(df):
    # For simplicity, we'll create a synthetic time pattern since the dataset doesn't have time
    # In a real application, you would use actual time data
    
    # Create morning, afternoon, and evening patterns
    times_of_day = ['Morning (7-10 AM)', 'Afternoon (12-3 PM)', 'Evening (5-8 PM)']
    
    # Create a figure with 3 subplots
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # Morning pattern - usually high volume, high congestion
    morning_cycle = np.array([120, 150, 110, 160, 140, 130])
    morning_major_green = morning_cycle * 0.65
    morning_minor_green = morning_cycle * 0.25
    morning_yellow = np.full_like(morning_cycle, 3)
    
    # Afternoon pattern - usually medium volume, medium congestion
    afternoon_cycle = np.array([100, 120, 90, 130, 110, 105])
    afternoon_major_green = afternoon_cycle * 0.6
    afternoon_minor_green = afternoon_cycle * 0.3
    afternoon_yellow = np.full_like(afternoon_cycle, 3)
    
    # Evening pattern - usually high volume, high congestion
    evening_cycle = np.array([130, 160, 120, 150, 145, 135])
    evening_major_green = evening_cycle * 0.7
    evening_minor_green = evening_cycle * 0.2
    evening_yellow = np.full_like(evening_cycle, 3)
    
    # Location labels
    labels = ['High-Volume\nIntersections', 'CBD\nIntersections', 'Residential\nIntersections', 
              'Commercial\nIntersections', 'Educational\nIntersections', 'Mixed-Use\nIntersections']
    
    # Plot for Morning
    axes[0].bar(labels, morning_major_green, label='Major Green')
    axes[0].bar(labels, morning_minor_green, bottom=morning_major_green, label='Minor Green')
    axes[0].bar(labels, morning_yellow, bottom=morning_major_green+morning_minor_green, label='Yellow')
    axes[0].set_title('Morning (7-10 AM) Timing', fontsize=12)
    axes[0].set_ylabel('Time (seconds)', fontsize=10)
    axes[0].set_ylim(0, 200)
    axes[0].tick_params(axis='x', rotation=45)
    
    # Plot for Afternoon
    axes[1].bar(labels, afternoon_major_green, label='Major Green')
    axes[1].bar(labels, afternoon_minor_green, bottom=afternoon_major_green, label='Minor Green')
    axes[1].bar(labels, afternoon_yellow, bottom=afternoon_major_green+afternoon_minor_green, label='Yellow')
    axes[1].set_title('Afternoon (12-3 PM) Timing', fontsize=12)
    axes[1].set_ylim(0, 200)
    axes[1].tick_params(axis='x', rotation=45)
    
    # Plot for Evening
    axes[2].bar(labels, evening_major_green, label='Major Green')
    axes[2].bar(labels, evening_minor_green, bottom=evening_major_green, label='Minor Green')
    axes[2].bar(labels, evening_yellow, bottom=evening_major_green+evening_minor_green, label='Yellow')
    axes[2].set_title('Evening (5-8 PM) Timing', fontsize=12)
    axes[2].set_ylim(0, 200)
    axes[2].tick_params(axis='x', rotation=45)
    axes[2].legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig('time_of_day_optimization.png')
    plt.close()

# Function to generate optimization report
def generate_optimization_report(results_df):
    # Create a formatted output of the optimization results
    report = "===== TRAFFIC SIGNAL OPTIMIZATION REPORT =====\n\n"
    
    # Summary statistics
    report += "SUMMARY STATISTICS:\n"
    report += f"Number of optimized intersections: {len(results_df)}\n"
    report += f"Average optimal cycle length: {results_df['Optimal_Cycle_Length'].mean():.1f} seconds\n"
    report += f"Average major approach green time: {results_df['Major_Green_Time'].mean():.1f} seconds\n"
    report += f"Average minor approach green time: {results_df['Minor_Green_Time'].mean():.1f} seconds\n"
    report += f"Average yellow time: {results_df['Yellow_Time'].mean():.1f} seconds\n\n"
    
    # Cluster information
    report += "INTERSECTION TIMING CLUSTERS:\n"
    for cluster in results_df['Cluster_Description'].unique():
        cluster_intersections = results_df[results_df['Cluster_Description'] == cluster]
        report += f"{cluster}\n"
        report += f"  Number of intersections: {len(cluster_intersections)}\n"
        report += f"  Average cycle length: {cluster_intersections['Optimal_Cycle_Length'].mean():.1f} seconds\n"
        report += f"  Intersections: {', '.join(cluster_intersections['Location'].tolist())}\n\n"
    
    # Detailed timing for each intersection
    report += "DETAILED TIMING BY INTERSECTION:\n"
    for i, row in results_df.sort_values('Optimal_Cycle_Length', ascending=False).iterrows():
        report += f"{row['Location']}:\n"
        report += f"  Optimal Cycle Length: {row['Optimal_Cycle_Length']:.1f} seconds\n"
        report += f"  Major Approach Green Time: {row['Major_Green_Time']:.1f} seconds\n"
        report += f"  Minor Approach Green Time: {row['Minor_Green_Time']:.1f} seconds\n"
        report += f"  Yellow Time: {row['Yellow_Time']:.1f} seconds\n"
        report += f"  Expected Congestion Reduction: {row['Estimated_Congestion_Reduction']:.1f}%\n"
        report += f"  Expected Speed Improvement: {row['Estimated_Speed_Improvement']:.1f} km/h\n\n"
    
    # Recommendations
    report += "GENERAL RECOMMENDATIONS:\n"
    report += "1. Implement adaptive signal control technology (ASCT) for high-volume intersections\n"
    report += "2. Consider transit signal priority for routes with high public transport usage\n"
    report += "3. Install countdown timers at intersections with low signal compliance\n"
    report += "4. Implement different timing plans for morning, afternoon, and evening peak hours\n"
    report += "5. Regularly monitor and adjust signal timings based on changing traffic patterns\n"
    
    # Save report to file
    with open('signal_optimization_report.txt', 'w') as f:
        f.write(report)
    
    return report

# Main function to execute the entire process
def main():
    print("Loading traffic data...")
    df = load_data()
    
    print("Preprocessing data for signal timing optimization...")
    signal_df = preprocess_data(df)
    
    print("Calculating optimal signal timings...")
    results_df = calculate_optimal_signal_timing(signal_df)
    
    print("Clustering intersections by timing patterns...")
    results_df, cluster_centers, cluster_descriptions = cluster_intersections(signal_df, results_df)
    
    print("Simulating optimization effects...")
    results_df = simulate_optimization_effect(results_df)
    
    print("Creating visualizations...")
    create_visualizations(df, results_df)
    
    print("Analyzing time-of-day patterns...")
    analyze_time_of_day_patterns(df)
    
    print("Generating optimization report...")
    report = generate_optimization_report(results_df)
    
    print("\nSignal timing optimization complete!")
    print("Output files:")
    print("- signal_timing_optimization_results.png")
    print("- timing_cluster_characteristics.png")
    print("- bangalore_signal_map.png")
    print("- time_of_day_optimization.png")
    print("- signal_optimization_report.txt")
    
    # Display the top 5 optimized intersections
    print("\nTop 5 optimized intersections (by cycle length):")
    print(results_df[['Location', 'Optimal_Cycle_Length', 'Major_Green_Time', 'Minor_Green_Time', 'Yellow_Time']]
          .sort_values('Optimal_Cycle_Length', ascending=False).head(5))
    
    return results_df

# Execute the main function
if __name__ == "__main__":
    results_df = main()