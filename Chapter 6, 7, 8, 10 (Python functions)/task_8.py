words = ["apple", "banana", "cherry", "apricot", "blueberry"]
target_letter = "a"

filtered_words = list(filter(lambda word: word.startswith(target_letter), words))

print(filtered_words)
