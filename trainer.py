import json
import random
import os

# Load N1 vocabulary
with open("vocab_n1.json", "r", encoding="utf-8") as f:
    vocab = json.load(f)

# Load or create progress file
if os.path.exists("progress.json"):
    with open("progress.json", "r", encoding="utf-8") as f:
        progress = json.load(f)
else:
    progress = {"total_attempts": 0, "correct_answers": 0, "history": []}

print("🧠 JLPT N1 Vocabulary Trainer")
print("Type 'quit' to stop.\n")

while True:
    item = random.choice(vocab)
    word = item["word"]
    reading = item["reading"]
    meaning = item["meaning"]

    print(f"Word: {word} ({reading})")
    answer = input("Meaning: ")

    if answer.lower() == "quit":
        break

    progress["total_attempts"] += 1

    if answer.lower() == meaning.lower():
        print("✅ Correct!\n")
        progress["correct_answers"] += 1
        progress["history"].append({"word": word, "result": "correct"})
    else:
        print(f"❌ Wrong. Correct answer: {meaning}\n")
        progress["history"].append({"word": word, "result": "wrong"})

# Save progress
with open("progress.json", "w", encoding="utf-8") as f:
    json.dump(progress, f, ensure_ascii=False, indent=4)

accuracy = (progress["correct_answers"] / progress["total_attempts"]) * 100 if progress["total_attempts"] else 0

print("📊 Study Summary")
print(f"Total attempts: {progress['total_attempts']}")
print(f"Correct answers: {progress['correct_answers']}")
print(f"Accuracy: {accuracy:.2f}%")
print("Progress saved to progress.json")