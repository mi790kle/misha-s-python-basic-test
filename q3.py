def camel_to_hyphen(text:str) -> str:
    text = list(text)
    for symbol in text:
        if symbol.isupper():
            text[text.index(symbol)] = symbol.lower()
            text.insert(text.index(symbol.lower()), "-")
    return "".join(text)

print(camel_to_hyphen("myVariableName"))