def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

def calculate_sle(asset_value, exposure_factor):
    return asset_value * exposure_factor

def calculate_ale(sle, aro):
    return sle * aro

def main():
    print("Welcome to the Risk Assessment Calculator!")

    # Asset Value Calculation
    asset_value = get_float_input("Please enter the value of your asset: $")

    # Initial Exposure Factor Calculation
    initial_exposure_factor = get_float_input("Please enter your exposure factor: ")
    print("Your Exposure Factor before a safeguard is: ", initial_exposure_factor)
    sle_before_safeguard = calculate_sle(asset_value, initial_exposure_factor)

    # Exposure Factor Calculation After Safeguard
    exposure_factor_after_safeguard = get_float_input("Please enter your exposure factor after implementing a safeguard: ")
    print("Your Exposure Factor after implementing the safeguard is: ", exposure_factor_after_safeguard)
    sle_after_safeguard = calculate_sle(asset_value, exposure_factor_after_safeguard)

    # Annual Rate of Occurrence
    aro = get_float_input("What is the expected annual rate of occurrence?: ")
    print("Your expected annual rate of occurrence is: ", aro)

    # Annual Cost of Safeguard
    annual_cost_of_safeguard = get_float_input("What is the annual cost of your safeguard?: $")
    print("Your annual cost of your safeguard is: $", annual_cost_of_safeguard)

    # Annual Loss Expectancy calculations
    ale_before_safeguard = calculate_ale(sle_before_safeguard, aro)
    ale_after_safeguard = calculate_ale(sle_after_safeguard, aro)

    print("Your Annual Loss Expectancy before your safeguard is: $", ale_before_safeguard,
          "and your Annual Loss Expectancy after implementing your safeguard is: $", ale_after_safeguard)

    value_of_safeguard = ale_before_safeguard - ale_after_safeguard - annual_cost_of_safeguard
    print("The Value of your safeguard is: $", value_of_safeguard)

if __name__ == "__main__":
    main()