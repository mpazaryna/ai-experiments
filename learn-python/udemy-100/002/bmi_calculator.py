def calculate_bmi(height: float, weight: float, is_metric: bool = True) -> int:
    """
    Calculate BMI based on the user's preferred system of measurement.

    Parameters:
    - height: The height of the person.
              If metric system, it's in meters.
              If imperial system, it's in inches.

    - weight: The weight of the person.
              If metric system, it's in kilograms.
              If imperial system, it's in pounds.

    - is_metric: A boolean indicating if the provided height and weight
                 are in metric system. Default is True.

    Returns:
    - An integer representing the calculated BMI.
    """

    # If the user chose the imperial system, convert height and weight to metric.
    if not is_metric:
        height /= 39.37  # Convert height from inches to meters
        weight *= 0.453592  # Convert weight from pounds to kilograms

    # Calculate BMI using the formula
    bmi = weight / height**2
    return int(bmi)


def bmi_classification(bmi: int) -> str:
    """
    Determine and return the BMI classification for a given BMI score.

    Parameter:
    - bmi: An integer representing the calculated BMI.

    Returns:
    - A string with the corresponding BMI classification.
    """
    if bmi < 16:
        return "Underweight (Severe thinness)"
    elif 16 <= bmi < 17:
        return "Underweight (Moderate thinness)"
    elif 17 <= bmi < 18.5:
        return "Underweight (Mild thinness)"
    elif 18.5 <= bmi < 25:
        return "Normal range"
    elif 25 <= bmi < 30:
        return "Overweight (Pre-obese)"
    elif 30 <= bmi < 35:
        return "Obese (Class I)"
    elif 35 <= bmi < 40:
        return "Obese (Class II)"
    else:
        return "Obese (Class III)"


def main():
    # Prompt the user to choose between metric and imperial system.
    measurement_choice = input(
        "Which system of measurement do you prefer? Enter 'metric' or 'imperial': "
    ).lower()

    # If the user chose metric system, get height in meters and weight in kilograms.
    if measurement_choice == "metric":
        height = float(input("Enter your height in m: "))
        weight = float(input("Enter your weight in kg: "))
        bmi_as_int = calculate_bmi(height, weight, is_metric=True)

    # If the user chose imperial system, get height in inches and weight in pounds.
    elif measurement_choice == "imperial":
        height = float(input("Enter your height in inches: "))
        weight = float(input("Enter your weight in pounds: "))
        bmi_as_int = calculate_bmi(height, weight, is_metric=False)

    # If the user entered an invalid choice, display an error message.
    else:
        print("Invalid choice!")
        return

    # Get the BMI classification based on the calculated BMI.
    classification = bmi_classification(bmi_as_int)

    # Display the calculated BMI and its classification.
    print(f"Your BMI is {bmi_as_int}. Classification: {classification}")


# Entry point of the program
if __name__ == "__main__":
    main()
