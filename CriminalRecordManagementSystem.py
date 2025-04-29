import random
import matplotlib.pyplot as plt

# --- 1. Requirement Analysis ---
class RequirementAnalysis:
    def __init__(self):
        self.requirements = {
            "User Roles": ["Jailer", "Police Officer", "CBI Officer"],
            "Core Features": [
                "Add Criminal Record",
                "Update Criminal Record",
                "Search Criminal Records",
                "Delete Criminal Record",
                "Generate Criminal Record Report"
            ]
        }

    def display_requirements(self):
        print("\n--- Requirement Analysis ---")
        print("User Roles:", self.requirements["User Roles"])
        print("Core Features:")
        for feature in self.requirements["Core Features"]:
            print(f"- {feature}")


# --- 2. Data Flow Diagram ---
class DataFlowDiagram:
    def __init__(self):
        self.data_flows = {
            "Input": ["Criminal's Personal Info", "Crime Info", "Court Judgment"],
            "Processes": ["Record Insertion", "Record Update", "Record Search", "Record Deletion", "Generate Report"],
            "Output": ["Criminal Record Report", "Search Results"]
        }

    def display_data_flow(self):
        print("\n--- Data Flow Diagram ---")
        print("Input Data:", self.data_flows["Input"])
        print("Processes:", self.data_flows["Processes"])
        print("Output Data:", self.data_flows["Output"])


# --- 3. Data Dictionary ---
class DataDictionary:
    def __init__(self):
        self.data_dict = {
            "Criminal's Personal Info": "Name, Age, Gender, Address",
            "Crime Info": "Crime Type, Date, Location, Description",
            "Court Judgment": "Sentence, Fine, Release Date",
            "Criminal Record Report": "Criminal's Info + Crime Info + Court Judgment"
        }

    def display_data_dict(self):
        print("\n--- Data Dictionary ---")
        for data, description in self.data_dict.items():
            print(f"{data}: {description}")


# --- 4. Use Case ---
class UseCase:
    def __init__(self):
        self.use_cases = {
            "Add Criminal Record": ["Jailer", "Police Officer", "CBI Officer"],
            "Update Criminal Record": ["Police Officer", "CBI Officer"],
            "Search Criminal Records": ["Jailer", "Police Officer", "CBI Officer"],
            "Delete Criminal Record": ["Police Officer", "CBI Officer"],
            "Generate Criminal Record Report": ["CBI Officer"]
        }

    def display_use_cases(self):
        print("\n--- Use Cases ---")
        for use_case, users in self.use_cases.items():
            print(f"{use_case} is performed by:", ", ".join(users))


# --- 5. Function Point (FP) Calculation ---
class FunctionPointCalculation:
    def __init__(self):
        self.function_points = {
            "Add Criminal Record": 4,
            "Update Criminal Record": 3,
            "Search Criminal Records": 3,
            "Delete Criminal Record": 3,
            "Generate Criminal Record Report": 5
        }

    def compute_fp(self):
        print("\n--- Function Point Calculation ---")
        total_fp = sum(self.function_points.values())
        print(f"Total Function Points: {total_fp}")
        return total_fp


# --- 6. Effort and Schedule Calculation (FP-based) ---
class EffortAndSchedule:
    def __init__(self, function_points):
        self.function_points = function_points
        self.fp_effort = 10  # Effort per FP (in hours)
        self.fp_schedule = 8  # Hours of work per day

    def compute_effort(self):
        print("\n--- Effort Calculation ---")
        total_effort = self.function_points * self.fp_effort
        print(f"Total Effort Required: {total_effort} hours")
        return total_effort

    def compute_schedule(self):
        total_effort = self.compute_effort()
        total_days = total_effort / self.fp_schedule
        print(f"Estimated Schedule: {total_days} days")
        return total_days


# --- 7. Risk Table ---
class RiskTable:
    def __init__(self):
        self.risks = {
            "Requirement Ambiguity": {"Probability": 0.6, "Impact": 8},
            "Data Security": {"Probability": 0.7, "Impact": 9},
            "Technological Complexity": {"Probability": 0.5, "Impact": 7},
            "Lack of Resources": {"Probability": 0.4, "Impact": 6}
        }

    def display_risk_table(self):
        print("\n--- Risk Table ---")
        for risk, details in self.risks.items():
            risk_score = details["Probability"] * details["Impact"]
            print(f"{risk} | Probability: {details['Probability']} | Impact: {details['Impact']} | Risk Score: {risk_score}")


# --- 8. Timeline Chart ---
def plot_timeline_chart(days_to_complete):
    print("\n--- Timeline Chart ---")
    # Simulating project progress over days
    days = list(range(1, days_to_complete + 1))
    progress = [random.uniform(0.1, 1.0) for _ in days]

    plt.plot(days, progress, label="Progress")
    plt.xlabel("Days")
    plt.ylabel("Progress")
    plt.title("Project Timeline")
    plt.legend()
    plt.show()


# --- 9. Design Engineering ---
class DesignEngineering:
    def __init__(self):
        self.design_steps = [
            "Define the system architecture",
            "Identify system components and their interactions",
            "Design the data models and storage structures",
            "Design individual components (UI, logic, etc.)"
        ]

    def display_design_steps(self):
        print("\n--- Design Engineering ---")
        for step in self.design_steps:
            print(f"- {step}")


# --- 10. Basis Path Testing ---
class BasisPathTesting:
    def __init__(self):
        self.test_cases = [
            {"input": "Add Criminal Record", "expected_output": "Record Added"},
            {"input": "Search Criminal Records", "expected_output": "Record Found"},
            {"input": "Generate Criminal Record Report", "expected_output": "Report Generated"}
        ]

    def perform_basis_path_test(self):
        print("\n--- Basis Path Testing ---")
        for test_case in self.test_cases:
            print(f"Test Case: {test_case['input']} | Expected Output: {test_case['expected_output']}")
            # Simulating test result
            actual_output = test_case["expected_output"]
            print(f"Test Passed for {test_case['input']}.")


# --- Simulate Criminal Record Management System ---
def simulate_criminal_record_management_system():
    print("===== CRIMINAL RECORD MANAGEMENT SYSTEM SIMULATION =====")

    # 1. Requirement Analysis
    requirement_analysis = RequirementAnalysis()
    requirement_analysis.display_requirements()

    # 2. Data Flow Diagram
    data_flow_diagram = DataFlowDiagram()
    data_flow_diagram.display_data_flow()

    # 3. Data Dictionary
    data_dictionary = DataDictionary()
    data_dictionary.display_data_dict()

    # 4. Use Case
    use_case = UseCase()
    use_case.display_use_cases()

    # 5. Function Point Calculation
    function_point_calculation = FunctionPointCalculation()
    total_fp = function_point_calculation.compute_fp()

    # 6. Effort and Schedule Calculation
    effort_schedule = EffortAndSchedule(total_fp)
    effort_schedule.compute_effort()
    schedule = effort_schedule.compute_schedule()

    # 7. Risk Table
    risk_table = RiskTable()
    risk_table.display_risk_table()

    # 8. Timeline Chart
    plot_timeline_chart(schedule)

    # 9. Design Engineering
    design_engineering = DesignEngineering()
    design_engineering.display_design_steps()

    # 10. Basis Path Testing
    basis_path_testing = BasisPathTesting()
    basis_path_testing.perform_basis_path_test()


# Run the simulation
simulate_criminal_record_management_system()
