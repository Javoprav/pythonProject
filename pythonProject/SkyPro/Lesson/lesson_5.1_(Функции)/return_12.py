text = "The quick brown fox jumps over the lazy dog"

def text_length():
    x = ''
    for word in text:
      if word != ' ':
        x += word
    return len(x)
print(text_length())