import sys

def greet(name="mundo"):
    return f"Hola, {name}!"

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "mundo"
    print(greet(name))
