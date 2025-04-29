# Introduction: Software Engineering - A Layered Approach; Software Process – ProcessFramework, Umbrella Activities; Process Models – Waterfall Model, Incremental Model, andEvolutionary process Model (Prototyping, Spiral Model); Introduction to Agile – AgilityPrinciples, Agile Model – Scrum. 

import time

# --- Layered Approach ---
class SoftwareEngineering:
    def display_layers(self):
        print("\n--- Software Engineering: Layered Approach ---")
        layers = ["Quality Focus", "Process", "Methods", "Tools"]
        for layer in layers:
            print(f"✓ {layer}")


# --- Software Process & Umbrella Activities ---
class SoftwareProcess:
    def display_framework(self):
        print("\n--- Process Framework Activities ---")
        steps = ["Communication", "Planning", "Modeling", "Construction", "Deployment"]
        for step in steps:
            print(f"-> {step}")
            time.sleep(0.3)

    def display_umbrella_activities(self):
        print("\n--- Umbrella Activities ---")
        umbrellas = [
            "Project Tracking", "Risk Management", "Quality Assurance",
            "Configuration Management", "Documentation", "Reviews", "Metrics"
        ]
        for act in umbrellas:
            print(f"- {act}")
            time.sleep(0.2)


# --- Software Process Models ---
class ProcessModels:
    def waterfall(self):
        print("\n[Waterfall Model Simulation]")
        steps = ["Requirements →", "Design →", "Implementation →", "Testing →", "Deployment"]
        print(" ".join(steps))

    def incremental(self):
        print("\n[Incremental Model Simulation]")
        for i in range(1, 4):
            print(f"Increment {i}: Build + Test + Deliver")
            time.sleep(0.5)

    def prototyping(self):
        print("\n[Prototyping Model Simulation]")
        print("Step 1: Create prototype")
        print("Step 2: Get user feedback")
        print("Step 3: Refine prototype")
        print("Step 4: Final system")

    def spiral(self):
        print("\n[Spiral Model Simulation]")
        phases = ["Planning", "Risk Analysis", "Engineering", "Evaluation"]
        for round in range(1, 3):
            print(f"Cycle {round}: " + " → ".join(phases))
            time.sleep(0.5)


# --- Agile Model & Scrum ---
class AgileScrum:
    def __init__(self):
        self.backlog = ["Login Module", "Dashboard UI", "API Integration", "Testing"]
        self.sprint_backlog = []
        self.done = []

    def show_principles(self):
        print("\n--- Agile Principles (Simplified) ---")
        principles = [
            "Customer satisfaction through early delivery",
            "Welcome changing requirements",
            "Deliver working software frequently",
            "Close, daily collaboration",
            "Motivated individuals + trust",
            "Face-to-face conversation",
            "Working software = progress"
        ]
        for p in principles:
            print(f"- {p}")
            time.sleep(0.2)

    def run_scrum(self):
        print("\n[Scrum Simulation - Sprint Planning]")
        self.sprint_backlog = self.backlog[:2]
        print("Sprint Backlog:", self.sprint_backlog)
        
        print("\n[Daily Scrum - Tasks in Progress]")
        for task in self.sprint_backlog:
            print(f"Working on: {task}")
            time.sleep(0.5)
            self.done.append(task)

        print("\n[Sprint Review - Completed Tasks]")
        for task in self.done:
            print(f"✓ {task}")


# --- Simulate Everything ---
def simulate_software_engineering():
    print("===== SOFTWARE ENGINEERING SIMULATION =====")

    # Layered Approach
    se = SoftwareEngineering()
    se.display_layers()

    # Process Framework
    sp = SoftwareProcess()
    sp.display_framework()
    sp.display_umbrella_activities()

    # Process Models
    pm = ProcessModels()
    pm.waterfall()
    pm.incremental()
    pm.prototyping()
    pm.spiral()

    # Agile and Scrum
    agile = AgileScrum()
    agile.show_principles()
    agile.run_scrum()


# Run Simulation
simulate_software_engineering()
