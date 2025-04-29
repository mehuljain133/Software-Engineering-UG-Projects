# Design Modeling: Translating the Requirements model into the Design Model, The DesignProcess, Design Concepts - Abstraction, Modularity and Functional Independence; ArchitecturalMapping using Data Flow. 

# --- Design Modeling Simulation ---

# --- 1. Translating the Requirements Model into the Design Model ---
class DesignModel:
    def __init__(self, name):
        self.name = name
        self.modules = []
    
    def add_module(self, module):
        self.modules.append(module)

    def display(self):
        print(f"\n--- Design Model: {self.name} ---")
        print("Modules: ")
        for module in self.modules:
            print(f"- {module}")

class RequirementsToDesign:
    def __init__(self):
        self.requirements = ["User Login", "Payment Processing", "Dashboard View"]
        self.design_model = DesignModel("Online Payment System Design")

    def translate_requirements(self):
        print("\nTranslating Requirements into Design Model...")
        for req in self.requirements:
            if req == "User Login":
                self.design_model.add_module("Authentication Module")
            elif req == "Payment Processing":
                self.design_model.add_module("Payment Gateway Module")
            elif req == "Dashboard View":
                self.design_model.add_module("Dashboard UI Module")
        self.design_model.display()


# --- 2. The Design Process ---
class DesignProcess:
    def __init__(self):
        self.steps = [
            "Step 1: Understand Requirements",
            "Step 2: Define System Components",
            "Step 3: Design Modules and Components",
            "Step 4: Implement Interfaces between Modules",
            "Step 5: Test and Refine Design"
        ]

    def display_process(self):
        print("\n--- The Design Process ---")
        for step in self.steps:
            print(step)


# --- 3. Design Concepts --- Abstraction, Modularity, Functional Independence ---
class DesignConcepts:
    def __init__(self):
        self.concepts = {
            "Abstraction": "Simplifying the design by hiding complex details and focusing on high-level functionalities.",
            "Modularity": "Dividing the system into smaller, manageable components (modules) that can be developed and maintained independently.",
            "Functional Independence": "Each module should perform a specific, well-defined function and be independent from other modules."
        }

    def display_concepts(self):
        print("\n--- Design Concepts ---")
        for concept, description in self.concepts.items():
            print(f"{concept}: {description}")


# --- 4. Architectural Mapping using Data Flow ---
class ArchitecturalMapping:
    def __init__(self):
        self.architecture = {
            "User Login": ["Authentication Module", "User Database"],
            "Payment Processing": ["Payment Gateway Module", "Bank API"],
            "Dashboard View": ["Dashboard UI Module", "User Data Service"]
        }

    def display_architecture(self):
        print("\n--- Architectural Mapping using Data Flow ---")
        for process, components in self.architecture.items():
            print(f"{process} flows through:")
            for component in components:
                print(f" -> {component}")
            print()


# --- Simulate Design Modeling ---
def simulate_design_modeling():
    print("===== DESIGN MODELING SIMULATION =====")

    # 1. Translating the Requirements Model into the Design Model
    design_translation = RequirementsToDesign()
    design_translation.translate_requirements()

    # 2. The Design Process
    design_process = DesignProcess()
    design_process.display_process()

    # 3. Design Concepts
    design_concepts = DesignConcepts()
    design_concepts.display_concepts()

    # 4. Architectural Mapping using Data Flow
    architectural_mapping = ArchitecturalMapping()
    architectural_mapping.display_architecture()


# Run the Design Modeling Simulation
simulate_design_modeling()

