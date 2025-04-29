# Software Metrics and Project Estimations: Function based Metrics, Software Measurement,Metrics for Software Quality; Software Project Estimation (FP based estimations, COCOMO IIModel); Project Scheduling (Timeline charts, tracking the schedule). 

import random
import matplotlib.pyplot as plt
import numpy as np

# --- 1. Function-based Metrics ---
class FunctionPointEstimation:
    def __init__(self, num_inputs, num_outputs, num inquiries, num files, num interfaces):
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.num_inquiries = num_inquiries
        self.num_files = num_files
        self.num_interfaces = num_interfaces

    def calculate_function_points(self):
        # Function point weights for each type of function
        weights = {
            "inputs": 4, 
            "outputs": 5, 
            "inquiries": 4, 
            "files": 7, 
            "interfaces": 5
        }
        
        function_points = (self.num_inputs * weights["inputs"] +
                           self.num_outputs * weights["outputs"] +
                           self.num_inquiries * weights["inquiries"] +
                           self.num_files * weights["files"] +
                           self.num_interfaces * weights["interfaces"])
        
        print(f"Estimated Function Points: {function_points}")
        return function_points


# --- 2. Software Measurement ---
class SoftwareMeasurement:
    def __init__(self, lines_of_code, cyclomatic_complexity):
        self.lines_of_code = lines_of_code
        self.cyclomatic_complexity = cyclomatic_complexity

    def display_measurements(self):
        print(f"Lines of Code: {self.lines_of_code}")
        print(f"Cyclomatic Complexity: {self.cyclomatic_complexity}")


# --- 3. Metrics for Software Quality ---
class SoftwareQualityMetrics:
    def __init__(self, defects_found, total_lines_of_code):
        self.defects_found = defects_found
        self.total_lines_of_code = total_lines_of_code

    def defect_density(self):
        density = self.defects_found / self.total_lines_of_code
        print(f"Defect Density: {density:.6f} defects per line of code")
        return density


# --- 4. Software Project Estimation (FP based and COCOMO II) ---
class ProjectEstimation:
    def __init__(self, function_points):
        self.function_points = function_points

    def fp_based_estimation(self):
        # Simple estimation model: effort = FP * avg hours per FP
        avg_hours_per_fp = 20  # Assume 20 hours per function point
        estimated_effort = self.function_points * avg_hours_per_fp
        print(f"Estimated Effort (FP Based): {estimated_effort} hours")
        return estimated_effort

    def cocomo_ii(self):
        # COCOMO II model - Example calculation
        scale_factor = 1.15  # Assume a scale factor
        effort = (self.function_points ** 1.05) * scale_factor  # Simplified COCOMO II formula
        time = effort / 200  # Assume a max productivity of 200 hours per month
        print(f"Estimated Effort (COCOMO II): {effort:.2f} person-months")
        print(f"Estimated Time (COCOMO II): {time:.2f} months")
        return effort, time


# --- 5. Project Scheduling (Timeline charts and tracking schedule) ---
class ProjectScheduling:
    def __init__(self, tasks, deadlines):
        self.tasks = tasks
        self.deadlines = deadlines

    def display_timeline(self):
        print("\n--- Project Timeline ---")
        for i in range(len(self.tasks)):
            print(f"Task: {self.tasks[i]} → Deadline: {self.deadlines[i]}")

    def track_progress(self):
        print("\n--- Tracking Progress ---")
        progress = [random.randint(0, 100) for _ in self.tasks]  # Random progress percentage
        for i, task in enumerate(self.tasks):
            print(f"Task: {task} → Progress: {progress[i]}%")
        return progress

    def plot_timeline(self):
        # Create a simple timeline chart
        progress = self.track_progress()
        plt.bar(self.tasks, progress)
        plt.xlabel('Tasks')
        plt.ylabel('Progress (%)')
        plt.title('Project Schedule Progress')
        plt.xticks(rotation=45, ha="right")
        plt.show()


# --- Simulate Software Metrics and Project Estimations ---
def simulate_software_metrics():
    print("===== SOFTWARE METRICS AND PROJECT ESTIMATIONS SIMULATION =====")

    # 1. Function-based Metrics (FP Estimation)
    fp_estimation = FunctionPointEstimation(10, 8, 6, 4, 2)  # Example inputs
    function_points = fp_estimation.calculate_function_points()

    # 2. Software Measurement (LOC and Cyclomatic Complexity)
    software_measurement = SoftwareMeasurement(1500, 10)
    software_measurement.display_measurements()

    # 3. Software Quality Metrics (Defect Density)
    quality_metrics = SoftwareQualityMetrics(20, 1500)
    quality_metrics.defect_density()

    # 4. Software Project Estimation
    project_estimation = ProjectEstimation(function_points)
    project_estimation.fp_based_estimation()
    project_estimation.cocomo_ii()

    # 5. Project Scheduling and Timeline
    tasks = ["Design", "Development", "Testing", "Deployment"]
    deadlines = ["2025-06-30", "2025-09-30", "2025-11-15", "2025-12-01"]
    project_scheduling = ProjectScheduling(tasks, deadlines)
    project_scheduling.display_timeline()
    project_scheduling.plot_timeline()


# Run the simulation
simulate_software_metrics()
