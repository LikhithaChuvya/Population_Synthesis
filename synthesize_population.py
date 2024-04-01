import pandas as pd
import random

# Read the sample data
sample_data = pd.read_csv("Data.csv")

# Population characteristics
population_characteristics = {
    "Sex": {"Male": 25324, "Female": 24676},
    "Age_group": {"Below 22 years": 17955, "22-60 years": 29642, "Above 60 years": 2403},
    "Highest_education_level": {"No formal education": 7490, "Primary education": 5655,
                                "Secondary education": 24400, "Graduation and above": 12455}
}

# Calculate probabilities for each category
total_population = sum(population_characteristics["Sex"].values())
sex_probabilities = {category: count / total_population for category, count in population_characteristics["Sex"].items()}

total_population = sum(population_characteristics["Age_group"].values())
age_group_probabilities = {category: count / total_population for category, count in population_characteristics["Age_group"].items()}

total_population = sum(population_characteristics["Highest_education_level"].values())
education_level_probabilities = {category: count / total_population for category, count in population_characteristics["Highest_education_level"].items()}

# Generate synthetic population
synthetic_population = []
for _ in range(50000):
    sex = random.choices(list(sex_probabilities.keys()), weights=list(sex_probabilities.values()))[0]
    age_group = random.choices(list(age_group_probabilities.keys()), weights=list(age_group_probabilities.values()))[0]
    education_level = random.choices(list(education_level_probabilities.keys()), weights=list(education_level_probabilities.values()))[0]
    synthetic_population.append({"Sex": sex, "Age_group": age_group, "Highest_education_level": education_level})

# Save synthetic population as a CSV file
synthetic_population_df = pd.DataFrame(synthetic_population)
synthetic_population_df.to_csv("synthetic_population.csv", index=False)

# Compute frequencies for the generated synthetic population
sex_frequencies = {"Male": 0, "Female": 0}
age_group_frequencies = {"Below 22 years": 0, "22-60 years": 0, "Above 60 years": 0}
education_level_frequencies = {"No formal education": 0, "Primary education": 0, "Secondary education": 0, "Graduation and above": 0}

for agent in synthetic_population:
    sex = agent["Sex"]
    age_group = agent["Age_group"]
    education_level = agent["Highest_education_level"]
    sex_frequencies[sex] += 1
    age_group_frequencies[age_group] += 1
    education_level_frequencies[education_level] += 1

# Save output frequencies in a text file
with open("output_frequencies.txt", "w") as file:
    file.write("Sex:\n")
    for category, count in sex_frequencies.items():
        file.write(f"{category}: {count}\n")

    file.write("\nAge_group:\n")
    for category, count in age_group_frequencies.items():
        file.write(f"{category}: {count}\n")

    file.write("\nHighest_education_level:\n")
    for category, count in education_level_frequencies.items():
        file.write(f"{category}: {count}\n")
