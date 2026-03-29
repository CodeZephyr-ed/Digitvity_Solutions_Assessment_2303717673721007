import pandas as pd

df = pd.read_csv("deliveries.csv")
noagents = input("Enter number of agents (press Enter for default 3): ")
if noagents == "":
    noagents = 3
else:
    noagents = int(noagents)


priority_map = {"High": 3, "Medium": 2, "Low": 1}
df["priority_value"] = df["priority"].map(priority_map)

#this sorts first based on priority and then the largest distance
df = df.sort_values(by=["priority_value", "distance_km"], ascending=[False, False])
print("Sorted Data:\n")
print(df[["location_id", "priority", "distance_km"]])

agents = []
distances = []
for i in range(noagents):
    agents.append([])
    distances.append(0)

for i in range(len(df)):
    row = df.iloc[i]
    minindex = distances.index(min(distances))
    agents[minindex].append(row["location_id"])
    distances[minindex] += row["distance_km"]

for _ in range(10):
    maxindex = distances.index(max(distances))
    minindex = distances.index(min(distances))
    improved = False
    for location in agents[maxindex]:
        loc_distance = df[df["location_id"] == location]["distance_km"].values[0]
        new_max = distances[maxindex] - loc_distance
        new_min = distances[minindex] + loc_distance
        if abs(new_max - new_min) < abs(distances[maxindex] - distances[minindex]):
            agents[maxindex].remove(location)
            agents[minindex].append(location)
            distances[maxindex] -= loc_distance
            distances[minindex] += loc_distance
            improved = True
            break
    if not improved:
        break

df["Agent"] = ""
for i, locations in enumerate(agents):
    df.loc[df["location_id"].isin(locations), "Agent"] = "Agent_" + str(i+1)


df.to_csv("delivery_plan.csv", index=False)
print("Saved delivery_plan.csv")

rows = [{"Agent": "Agent:" + str(i+1), 
         "Total_Deliveries": len(locations), 
         "Total_Distance_km": round(distances[i], 2)}
        for i, locations in enumerate(agents)]
summary_df = pd.DataFrame(rows)
summary_df.to_csv("agent_summary.csv", index=False)
print("Saved agent_summary.csv")
print("\nAgent Summary:")
print(summary_df)