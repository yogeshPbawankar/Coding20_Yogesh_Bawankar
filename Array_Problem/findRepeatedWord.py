def findRepeatedWord(words):
    words = words.split()
    max_word = ""
    max_count = 0
    
    for word in words:
        word_count = {}
        for char in word:
            word_count[char] = word_count.get(char, 0) + 1
            
        repeated_chars = sum(1 for count in word_count.values() if count > 1)
        
        if repeated_chars > max_count:
            max_count = repeated_chars
            max_word = word
    
    return max_word

line = "abcdef google microsoft helllooo"
print("Result:", findRepeatedWord(line))
