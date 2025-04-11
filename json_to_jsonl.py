import json

with open("symptoms_data.json", "r") as f:
    symptoms = json.load(f)["symptoms"]

with open("symptom_training_data.jsonl", "w") as out_file:
    for symptom, info in symptoms.items():
        user_input = f"I have {symptom}"
        assistant_response = f"{symptom.capitalize()} could mean {', '.join(info['conditions'])}. Severity: {info['severity']}. Advice: {info['advice']}"
        
        entry = {
            "messages": [
                {"role": "system", "content": "You are a helpful medical assistant."},
                {"role": "user", "content": user_input},
                {"role": "assistant", "content": assistant_response}
            ]
        }

        out_file.write(json.dumps(entry) + "\n")

print("symptom_training_data.jsonl is ready for fine-tuning.")
