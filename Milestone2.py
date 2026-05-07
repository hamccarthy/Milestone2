# ---------------------------------------------------
# Milestone 2
# Research Question:
# Is there a difference in health outcomes between
# patients who have regular primary care visits and
# those who do not?
# ---------------------------------------------------

import csv

# ----------------------------
# Step 1: Load data
# ----------------------------

visits = []
health = []

# Open CDC BRFSS dataset
with open("brfss.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # only use rows with data
        if row["CHECKUP1"] != "" and row["GENHLTH"] != "":
            visits.append(int(row["CHECKUP1"]))
            health.append(int(row["GENHLTH"]))

print("Total records loaded:", len(visits))

# ----------------------------
# Step 2: Clean / organize groups
# ----------------------------

regular_group = []
no_regular_group = []

for i in range(len(visits)):
    # 1 = visited doctor in past year
    if visits[i] == 1:
        regular_group.append(health[i])
    else:
        no_regular_group.append(health[i])

# ----------------------------
# Step 3: Calculate averages
# ----------------------------

def average(numbers):
    return sum(numbers) / len(numbers)

avg_regular = average(regular_group)
avg_none = average(no_regular_group)

print("\nAverage Health Scores (lower = better):")
print("Regular visits:", avg_regular)
print("No regular visits:", avg_none)

# ----------------------------
# Step 4: Simple comparison conclusion
# ----------------------------

if avg_regular < avg_none:
    print("\nConclusion: Regular primary care visits are associated with better health outcomes.")
else:
    print("\nConclusion: No clear improvement in health outcomes was found.")

# ----------------------------
# Step 5: Simple text-based visualization
# ----------------------------

print("\nSimple Comparison Chart")
print("------------------------")
print("Regular Visits     :", "*" * int(avg_regular * 10))
print("No Regular Visits  :", "*" * int(avg_none * 10))