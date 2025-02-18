acres_per_segment = 16 
tomato_yield_30 = 10 
tomato_yield_70 = 12  
potato_yield = 10  
cabbage_yield = 14  
sunflower_yield = 0.7  
sugarcane_yield = 45 
tomato_price = 7  
potato_price = 20  
cabbage_price = 24  
sunflower_price = 200  
sugarcane_price = 4000
tomato_land = acres_per_segment
tomato_yield_30_percent = 0.30 * tomato_land * tomato_yield_30  
tomato_yield_70_percent = 0.70 * tomato_land * tomato_yield_70  
total_tomato_yield = tomato_yield_30_percent + tomato_yield_70_percent
total_tomato_sales = total_tomato_yield * 1000 * tomato_price
total_potato_yield = potato_yield * acres_per_segment
total_potato_sales = total_potato_yield * 1000 * potato_price
total_cabbage_yield = cabbage_yield * acres_per_segment
total_cabbage_sales = total_cabbage_yield * 1000 * cabbage_price
total_sunflower_yield = sunflower_yield * acres_per_segment
total_sunflower_sales = total_sunflower_yield * 1000 * sunflower_price
total_sugarcane_yield = sugarcane_yield * acres_per_segment
total_sugarcane_sales = total_sugarcane_yield * sugarcane_price
total_sales = total_tomato_sales + total_potato_sales + total_cabbage_sales + total_sunflower_sales + total_sugarcane_sales
total_chemical_free_sales = total_tomato_sales + total_cabbage_sales + total_sunflower_sales + total_sugarcane_sales
total_non_chemical_free_sales = total_potato_sales
total_sales_realization = total_chemical_free_sales + total_non_chemical_free_sales
print(f"Overall sales from 80 acres: Rs. {total_sales:,.2f}")
print(f"Sales realization from chemical-free farming at the end of 11 months: Rs. {total_sales_realization:,.2f}")

