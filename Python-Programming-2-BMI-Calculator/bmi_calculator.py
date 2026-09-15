def read_positive_number(prompt):
    while True:
        value = input(prompt).strip()
        try:
            number = float(value)
            if number <= 0:
                print("Please enter a value greater than 0.")
                continue
            return number
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal"
    if bmi < 30:
        return "Overweight"
    return "Obese"


def main():
    print("=== BMI Calculator ===")
    print("This is a programming exercise based on the categories specified in the OIBSIP task brief.")
    weight = read_positive_number("Enter weight in kg: ")
    height = read_positive_number("Enter height in meters: ")
    bmi = weight / (height ** 2)
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {classify_bmi(bmi)}")


if __name__ == "__main__":
    main()
