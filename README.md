# Delivery Assignment Optimization

## Overview
This project distributes delivery tasks among agents efficiently based on priority and distance. The goal is to ensure high-priority deliveries are handled first while balancing the total distance assigned to each agent.

The program reads a CSV file of delivery locations, calculates a priority score, sorts the deliveries, and assigns them to multiple agents. It also generates a summary report for each agent.

---

## Dataset Description (`deliveries.csv`)

| Column | Description |
|--------|-------------|
| location_id | Unique ID of the delivery location (e.g., L001) |
| location_name | Name of the delivery area or hub |
| distance_km | Distance from the starting point in kilometers |
| priority | Delivery priority: High, Medium, Low |
| time_window | Scheduled delivery time window |
| package_weight_kg | Weight of the package in kilograms |
| customer_contact | Customer phone number |

**Example Rows:**

L001,Adyar Market,4.2,High,09:00-11:00,2.5,+91-9876543210  
L002,T Nagar Hub,6.8,High,08:30-10:30,5.0,+91-9876543211  
L003,Velachery Zone,9.1,Medium,10:00-13:00,3.2,+91-9876543212  

---

## Code Approach

1. **Input Number of Agents:**  
   User inputs the number of delivery agents (default is 3).

2. **Assign Priority Values:**  
   Each delivery is assigned a numeric priority (High=3, Medium=2, Low=1) to simplify sorting.

3. **Sort Deliveries:**  
   Deliveries are sorted by priority (descending) and distance (descending) to handle urgent and far deliveries first.

4. **Initial Assignment:**  
   Each delivery is assigned to the agent with the least total distance so far to balance workload.

5. **Workload Balancing:**  
   An iterative improvement step swaps deliveries between the agent with maximum distance and the agent with minimum distance to further balance total distances.

6. **Save Output Files:**  
   - `delivery_plan.csv` → Shows which agent is assigned to each location.  
   - `agent_summary.csv` → Summary per agent: total deliveries and total distance.

---

## Why This Approach?

- Prioritizes urgent deliveries while considering travel distance.  
- Greedy allocation ensures no single agent is overloaded.  
- Iterative swapping improves balance without complex optimization algorithms.  
- Outputs provide clear planning and reporting for operational use.

---

## How to Run

1. Ensure Python and pandas are installed.  
2. Place the `deliveries.csv` file in the same directory as the script.  
3. Run the script:
