import random
import string


def generate_password(length, selected_types):
    pools = {
        "uppercase": string.ascii_uppercase,
        "lowercase": string.ascii_lowercase,
        "numbers": string.digits,
        "symbols": string.punctuation,
    }
    alphabet = "".join(pools[name] for name in selected_types)
    return "".join(random.choice(alphabet) for _ in range(length))


def get_length():
    while True:
        raw = input("Password length (minimum 8): ").strip()
        try:
            length = int(raw)
            if length < 8:
                print("Length must be at least 8.")
            else:
                return length
        except ValueError:
            print("Please enter a whole number.")


def get_types():
    labels = {
        "1": "uppercase",
        "2": "lowercase",
        "3": "numbers",
        "4": "symbols",
    }
    print("Choose character types (select at least 2):")
    print("1. Uppercase  2. Lowercase  3. Numbers  4. Symbols")
    while True:
        choices = {item.strip() for item in input("Enter choices separated by commas: ").split(",")}
        selected = [labels[c] for c in choices if c in labels]
        if len(set(selected)) >= 2:
            return list(dict.fromkeys(selected))
        print("Please select at least 2 valid character types.")


def main():
    print("=== Random Password Generator ===")
    while True:
        length = get_length()
        selected = get_types()
        password = generate_password(length, selected)
        print(f"Generated password: {password}")
        again = input("Generate another? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
