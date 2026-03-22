#Day 3 - loops Practice
# Simple word trainer - practice typing common pyhton keywbords

words = ["def", "return", "if", "else", "elif", "for", "while", "import", "from", "as", "function", "variable", "loop", "condition", "string"]
correct = 0

print("=== Python Word Trainer ===")
print("Type each word correctly!\n")

for word in words:
    answer = input (f"Type this word: {word} -> ")
    if answer == word:
        print("Correct!\n")
        correct += 1
    else: 
        print(f"Wrong! The correct word was: {answer}\n")

print(f"=== Results ===")
print(f"Score: {correct}/{len(words)}")
print(f"Acocuracy: {correct/len(words)*100:.1f}%")
