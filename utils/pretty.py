def pretty_underline(text:str, underline: str ="="):
    try:
        print(len(text.splitlines()[-1]) * underline)
    except:
        print()

def pretty_print(text: str, underline: str = "="):
    print(text)
    pretty_underline(text, underline)