"""A multi-language greeting module."""
GREETINGS = {"en": "Hello", "zh": "你好", "ja": "こんにちは"}

def greet(name="World", lang="en"):
    greeting = GREETINGS.get(lang, GREETINGS["en"])
    return f"{greeting}, {name}!"

if __name__ == "__main__":
    print(greet())
    print(greet("Git", "zh"))
