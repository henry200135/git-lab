from datetime import datetime

def greet(name="World", lang="en"):
    hour = datetime.now().hour
    if hour < 12:    prefix = "Good morning"
    elif hour < 18:  prefix = "Good afternoon"
    else:            prefix = "Good evening"
    return f"{prefix}, {name}!"

if __name__ == "__main__":
    print(greet())
# TODO
