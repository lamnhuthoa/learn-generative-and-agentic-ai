import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey there! My name is Henry"
tokens = enc.encode(text)

print("Tokens:", tokens) # Tokens: [25216, 1354, 0, 3673, 1308, 382, 27755]

decoded = enc.decode([25216, 1354, 0, 3673, 1308, 382, 27755])
print("Decoded:", decoded) # Decoded: Hey there! My name is Henry