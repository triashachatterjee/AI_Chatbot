import pandas as pd
import json

# Correct path with raw string
csv_file = r"D:\My Docs\Documents\AI_Chatbot\config\Disease_symptom_and_patient_profile_dataset.csv"
df = pd.read_csv(csv_file)

# Initialize chatbot format
chatbot_data = {"symptoms": {}}

# Get symptom columns dynamically (those with "Yes"/"No" answers)
symptom_columns = ["Fever", "Cough", "Fatigue", "Difficulty Breathing"]

for _, row in df.iterrows():
    disease = row["Disease"].strip()
    
    for symptom_col in symptom_columns:
        if row[symptom_col].strip().lower() == "yes":
            symptom = symptom_col.lower()
            
            if symptom not in chatbot_data["symptoms"]:
                chatbot_data["symptoms"][symptom] = {
                    "conditions": [],
                    "severity": "Unknown",
                    "advice": "Consult a doctor if symptoms persist."
                }
            
            if disease not in chatbot_data["symptoms"][symptom]["conditions"]:
                chatbot_data["symptoms"][symptom]["conditions"].append(disease)

# Save to JSON
json_file = "symptoms_data.json"
with open(json_file, "w") as f:
    json.dump(chatbot_data, f, indent=4)

print(f" Chatbot data saved to {json_file}")
