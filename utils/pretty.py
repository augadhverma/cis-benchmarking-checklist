def pretty_underline(text:str, underline: str ="="):
    print(len(text.splitlines()[-1]) * underline)

def pretty_print(text: str, underline: str = "="):
    print(text)
    pretty_underline(text, underline)