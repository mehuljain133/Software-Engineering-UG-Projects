# Software Testing: Strategic Approach to Software Testing, Unit Testing, Integration Testing,Validation Testing, System Testing; Black-Box and White Box Testing, Basis Path Testing

import random
import matplotlib.pyplot as plt

# --- 1. Strategic Approach to Software Testing ---
class SoftwareTestingStrategy:
    def __init__(self):
        self.testing_levels = [
            "Unit Testing: Testing individual units or components of the software.",
            "Integration Testing: Testing the interaction between units or components.",
            "Validation Testing: Ensuring the software meets the end user's requirements.",
            "System Testing: Testing the entire system as a whole."
        ]

    def display_testing_strategy(self):
        print("\n--- Strategic Approach to Software Testing ---")
        for level in self.testing_levels:
            print(level)


# --- 2. Unit Testing ---
class UnitTesting:
    def __init__(self, function_to_test):
        self.function_to_test = function_to_test

    def perform_unit_test(self):
        print("\n--- Unit Testing ---")
        test_cases = [1, 2, 3, 4, 5]
        results = [self.function_to_test(tc) for tc in test_cases]
        for i, result in enumerate(results):
            print(f"Test Case {i + 1}: Input={test_cases[i]} | Output={result}")
        return results


# Example function for unit testing
def sample_function(x):
    return x * 2


# --- 3. Integration Testing ---
class IntegrationTesting:
    def __init__(self, component1, component2):
        self.component1 = component1
        self.component2 = component2

    def perform_integration_test(self):
        print("\n--- Integration Testing ---")
        result1 = self.component1()
        result2 = self.component2()
        print(f"Component 1 output: {result1}")
        print(f"Component 2 output: {result2}")
        print(f"Integrated system output: {result1 + result2}")


# Example components for integration testing
def component1():
    return 5

def component2():
    return 10


# --- 4. Validation Testing ---
class ValidationTesting:
    def __init__(self, expected_output):
        self.expected_output = expected_output

    def perform_validation_test(self, actual_output):
        print("\n--- Validation Testing ---")
        if actual_output == self.expected_output:
            print("Test Passed: Software meets the user's requirements.")
        else:
            print(f"Test Failed: Expected {self.expected_output}, but got {actual_output}")


# Example validation for software
validation_test = ValidationTesting(expected_output=15)


# --- 5. System Testing ---
class SystemTesting:
    def __init__(self, system_components):
        self.system_components = system_components

    def perform_system_test(self):
        print("\n--- System Testing ---")
        print("Running system tests on the following components:")
        for component in self.system_components:
            print(f"- {component}")
        print("System test passed: All components are functioning correctly.")


# Example system with multiple components
system_components = ["Login Module", "Payment Gateway", "Database", "User Interface"]
system_test = SystemTesting(system_components)


# --- 6. Black-Box Testing ---
class BlackBoxTesting:
    def __init__(self, function_to_test):
        self.function_to_test = function_to_test

    def perform_black_box_test(self):
        print("\n--- Black-Box Testing ---")
        test_cases = [1, 2, 3, 4, 5]
        expected_results = [2, 4, 6, 8, 10]
        for i, input_val in enumerate(test_cases):
            actual_result = self.function_to_test(input_val)
            print(f"Input: {input_val} | Expected Output: {expected_results[i]} | Actual Output: {actual_result}")
            assert actual_result == expected_results[i], f"Test failed for input {input_val}."


# --- 7. White-Box Testing ---
class WhiteBoxTesting:
    def __init__(self, function_to_test):
        self.function_to_test = function_to_test

    def perform_white_box_test(self):
        print("\n--- White-Box Testing ---")
        test_cases = [1, 2, 3, 4, 5]
        for test_case in test_cases:
            print(f"Testing with input: {test_case} | Output: {self.function_to_test(test_case)}")
        print("White-box testing completed successfully.")


# --- 8. Basis Path Testing ---
class BasisPathTesting:
    def __init__(self, function_to_test):
        self.function_to_test = function_to_test

    def perform_basis_path_test(self):
        print("\n--- Basis Path Testing ---")
        # For simplicity, assume we are testing a function with multiple paths
        paths = ["Path 1", "Path 2", "Path 3", "Path 4"]
        test_case_paths = [1, 2, 3, 4, 5]

        for i, path in enumerate(paths):
            result = self.function_to_test(test_case_paths[i])
            print(f"Testing {path} | Input: {test_case_paths[i]} | Output: {result}")
        print("Basis path testing completed successfully.")


# --- Simulate Software Testing ---
def simulate_software_testing():
    print("===== SOFTWARE TESTING SIMULATION =====")

    # 1. Strategic Approach to Software Testing
    strategy = SoftwareTestingStrategy()
    strategy.display_testing_strategy()

    # 2. Unit Testing
    unit_testing = UnitTesting(sample_function)
    unit_testing.perform_unit_test()

    # 3. Integration Testing
    integration_testing = IntegrationTesting(component1, component2)
    integration_testing.perform_integration_test()

    # 4. Validation Testing
    actual_output = 15
    validation_test.perform_validation_test(actual_output)

    # 5. System Testing
    system_test.perform_system_test()

    # 6. Black-Box Testing
    black_box_testing = BlackBoxTesting(sample_function)
    black_box_testing.perform_black_box_test()

    # 7. White-Box Testing
    white_box_testing = WhiteBoxTesting(sample_function)
    white_box_testing.perform_white_box_test()

    # 8. Basis Path Testing
    basis_path_testing = BasisPathTesting(sample_function)
    basis_path_testing.perform_basis_path_test()


# Run the simulation
simulate_software_testing()
